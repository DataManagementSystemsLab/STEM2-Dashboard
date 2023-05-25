import re
import json
import sys
import json


def parse_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    print("Done reading")
    data = {}
    data[1]=[]
    data[2]=[]
    data[3]=[]
    data[4]=[]
    data[5]=[]
    state = 1
    indx=0
    for indx in range(len(lines)):
        line=lines[indx]
        next_line=""
        if indx<len(lines)-1:
            next_line=lines[indx+1]
        if "Reducing table." in line and state < 2:
                state = 2
        elif "Starting reduction." in line:
                state = 3
        elif state == 3 and "Reduction finished." in line:
                state = 3.5
        elif 'RealSupport' in line and  '->' in line:
                state = 4
        elif 'Total Support' in  line:
                state=5

        #print(line)
        #print(" line     "+line+"--------------")
        #print(" next line  "+next_line+">>>>>>>>>>>>>>>>>")
        if 'conf' in next_line and state==4:
            #print(" line     "+line+"----------------")
            #print(" next line  "+next_line+">>>>>>>>>>>>>>><<<<<<<<")
            line=line  + ';'+next_line
            #print ("line"+line)
        data[int(state)].append(line.strip())
   
    return data



def build_regs():
    r=dict()
    r["using"]=re.compile(r".*Using (?P<k>(\w|\s)+)(\s)*:\s*(?P<v>.*)")
    r["mode"]=re.compile(r".*Running in (?P<mode>(\w)+) mode.*")
    r["implication"]=re.compile(r".*(\.|;)(?P<from>.*)->(?P<to>(\d|\s)*);")
    r["reduces"]=re.compile(r"(?P<k>(\d+\s?)+) << reduces (?P<v>(\d+\s?)+) for column (?P<c>\d+)")
    r["totalsupport"]=re.compile(r"(?P<key>\d+)\s*->\s*(?P<tsupport>(\d|\.)+)")
    r["equivalence"]=re.compile(r"(?P<m1>.*)<=>(?P<m2>.*)")
    filters=dict()
    filters["using"]=["using"]
    filters["mode"]=["running","in","mode"]
    filters["implication"]=["->","Support"]
    filters["reduces"]=["reduces","column"]
    filters["totalsupport"]=["->"]
    filters["equivalence"]=["<=>"]
    return r,filters


def get_fields(data, filters, regs):
   
    res=dict()
 
    res["value"]=data=re.sub(r'\n|\t',' ',data)
    #print('=========>>' + data +'<<<<<<<<')
    for k,v in  filters.items():
        #print(k)
        #print (v)
        match=True
        for i in v:
            if i not in data:
                match=False
                break
        if match==False:
            continue        
        reg=regs[k]
        #print(reg)
        m=reg.match(data)
        
        if m!= None:
            #print("MATCHING")
            res["type"]=k
            for k1,v1 in m.groupdict().items():
                #print("<<<<<<<<<<"+k1 + "  "+v1)
                res[k1.strip()]=v1.strip()
            
            if k=="implication":
                kvs=data.split(';')
                for kv in kvs:
                    try:
                        if '=' in kv:
                            t=kv.split('=')
                            tk=t[0].strip()
                            tv=t[1].strip()
                            res[tk]=tv
                    except:
                        print (t)    
            return res
    return res


def to_dict(file_path):
      json_data=dict()
      json_data["filename"]=file_path
      data=parse_file(file_path)
      print("Done parsing")
      regs,filters=build_regs()
      for k,v in data.items():
            json_data[k]=list()
            for item in  v:
                json_data[k].append(get_fields(item,filters,regs))
                        
      return json_data          


f1="/Users/User/Desktop/ToDo/output.txt"
f2="/Users/User/Desktop/ToDo/dbasis_output.txt"
f3="/Users/User/Desktop/dbasis/data/golden-tests/Large_set_Dbasis_May24_2016.txt"


if __name__ == "__main__":
    dictionary=to_dict(sys.argv[1])
    json_object = json.dumps(dictionary, indent = 4)
    outputfile=sys.argv[1]+".json"
    with open(outputfile, "w") as outfile:
        outfile.write(json_object)
#import parse as  p
#j1=p.to_json(p.f1)

#.*(\.|;)(?P<b>.*)->(?P<a>(\d|\s)*);