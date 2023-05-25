import duckdb
import pandas as pd
import itertools
import BitVector as b



# define custom sorting function
def sort_tuple(t):
	return [t.index(col) for col in list(df.columns)]

def sort_key(cols,elem):
		return cols.index(elem[0])


def get_combinations(cols):
	combinations = []
	for i in range(1, len(cols)+1):
		combinations += itertools.combinations(cols, i)
	return combinations 

def get_bitmap(cols,tup):
	bv0=b.BitVector(size=len(cols))
	for x,v in tup:
	 	i=cols.index(x)
	 	bv0[i]=1
	return bv0

def get_ancestors(tup,nodes, combinations):
	l=[]
	for c in combinations:
			t= tuple(x for x in tup if x[0] not in c)
			if (t!=tup):
				if t in nodes:
					l.append(t)
	return l  

def get_parents(tup,nodes,combinations):
	ancestors=get_ancestors(tup,nodes,combinations)
	ansc=dict()
	for ancestor in ancestors:
		l=len(ancestor)
		if l not in ansc:
			ansc[l]=[]
		ansc[l].append(ancestor)
	if len(ansc)==0:
		return []
	m=max(ansc.keys())
	return ansc[m]  

def get_direct_parents(ancestors):
	ansc=dict()
	for ancestor in ancestors:
		l=ancestor.get_count()
		if l not in ansc:
			ansc[l]=[]
		ansc[l].append(ancestor)
	if len(ansc)==0:
		return []
	m=max(ansc.keys())
	return ansc[m]  	



class Node:
	# change cols to a class variable

	def get_bitmap(self):
		bv0=b.BitVector(size=len(self.cols))
		for x,v in self.tup:
	 		i=self.cols.index(x)
	 		bv0[i]=1
		return bv0

	def __init__(self,cols,tup,val, indx):
		self.tup=tup
		self.cols=cols
		self.val=val
		self.indx=indx
		
		self.bitmap=self.get_bitmap()


	def __str__(self):
		return str(self.tup)+" "+str(self.bitmap)+" "+str(self.val)+"    "+str(self.indx)
	
	def get_count(self):
		return self.bitmap.count_bits() 

	def is_parent(self,parent):	
		bv=self.bitmap & parent.bitmap
		if bv.count_bits() == 0:
			return False

		ht=dict()
		for x,v in self.tup:
			i=self.cols.index(x)
			if bv[i]==1:
				ht[x]=v

		for x,v in parent.tup:
			if x in ht:
				if ht[x] != v:
	 				return False
		return True


def build_graph(df):
	edges=[]
	nodes=[]
	
	value_cols=["c"]
	nan_cols=set()
	cols=list(df.columns)
	for index, row in df.iterrows():
		s=dict()
		for col, val in row.items():
			if col not in value_cols:
				if str(val)!="nan":
					#s.append(str(val))
					s[col]=str(val)
				else:
					nan_cols.add(col)
		atuple=tuple(sorted(s.items(), key=lambda x: sort_key(cols,x)))		
		nodes.append(Node(cols,atuple, row['c'], index))
		
	for n in nodes:
	 	for p in nodes:
	 		ancestors=[]
	 		if n.is_parent(p):
	 			ancestors.append(p)
	 		#get direct parent
	 		parents=get_direct_parents(ancestors)
	 		## add edges
	 		for d in parents:
	 			edges.append((n.indx,d.indx,n.val))
	 			

	edges=list(set(edges))	

	return nodes, edges	
		
	#combinations=get_combinations(list(nan_cols))
	#print("--------")
	#print(nan_cols)
	#print("--------")
	#print(combinations)
	#print(">>>>>>>>>>>>>><<<<<<<<<<<<<<")

	#for index, row in df.iterrows:
		#s=dict()
		#for col, val in row.items():
		#	if col not in value_cols:
		#		if str(val)!="nan":
		#			s[col]=str(val)
					
		#atuple=tuple(sorted(s.items(), key=lambda x: sort_key(df,x))) 
		#atuple=nodes[index]
		#parents=get_parents2(atuple,nodes)
		#if index==1:
		#		print("Tuple")
		#		print(atuple)
		#		print("Parents")
		#		for pp in parents:
		#			print(pp)
		#		print("nodes")
		#		for n in nodes:
		#			print(n)
		#target=nodes.index(atuple)
		#print(str(atuple)+" "+str(target))
		#for p in parents:
		#	if p in nodes:
		#		src=nodes.index(p)
		#		val=row['c']
		#		edges.append((src,target,val))




def get_labels(nodes):
	str_nodes=[]
	for n in nodes:
		s=""
		for x in n.tup:
			s=s+("_"+x[1])
		str_nodes.append(s[1:])
	return str_nodes


def get_edges(edges):
	srcs=[edge[0] for edge in edges]
	targets=[edge[1] for edge in edges]
	vals=[edge[2] for edge in edges]
	return srcs, targets, vals


