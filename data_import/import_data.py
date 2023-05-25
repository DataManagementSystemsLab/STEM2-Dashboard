import json
import duckdb
import os
import parse
class DataImport:
	def __init__(self, dbname):
		self.conn = duckdb.connect(dbname)

	def create_tables(self):
		implications='''
						CREATE TABLE IF NOT Exists implication (
								"id" integer,
								"from" INTEGER[],
								"conf" FLOAT,
								"to" INTEGER,
								"support" INTEGER,
								"realsupport" INTEGER
									);'''

		files='''
						CREATE TABLE IF NOT Exists file (
								"id" integer,
								"path" varchar(150),
								"filename" varchar(30),
								"source" varchar(20),
								"comment" text
									);'''
		seq= '''
		CREATE SEQUENCE IF NOT Exists  seq_files START 1;
		'''				
		self.conn.execute(implications)
		self.conn.execute(files)
		self.conn.execute(seq)
		self.conn.commit()

	
	def get_files(self, path, ext=".txt"):
		l_files = []

		for root, dirs, files in os.walk(path):
			for file in files:
				if file.endswith(ext):
					l_files.append(os.path.join(root, file))

		return l_files

	def add_implication(self, path, data=None):

		if data is None:
			with open(path, 'r') as file:
				data = json.load(file)

		dir_name = os.path.dirname(path)
		file_name = os.path.basename(path)

		result = self.conn.execute("SELECT nextval('seq_files') as n;").fetchdf()
		pid=result['n'][0]

	
		self.conn.execute(f"INSERT INTO file(id, path, filename) VALUES ({pid},'{dir_name}','{file_name}');")
		if 4 in data:
			d=data[4]
		elif '4' in data:
			d=data['4']
		for x in d:
			if 'from' in x:
				y=dict()
				y['f']=x['from'].split(' ')
				y['c']=x['conf']
				y['t']=x['to']
				y['support']=x['support']
				y['real']=x['RealSupport']
				print(y)
				sqlcommand=f"INSERT INTO implication VALUES ({pid},{y['f']}, {y['c']}, {y['t']}, {y['support']}, {y['real']});"
				print(sqlcommand)
				self.conn.execute(sqlcommand)
				
		self.conn.commit()

	def import_txt(self, path, subset=False):
		txts=self.get_files(path,".txt")
		if subset:
			txts=txts[:10]
		for txt in txts:
			print(txt)
			data=parse.to_dict(txt)
			self.add_implication(txt,data)	
