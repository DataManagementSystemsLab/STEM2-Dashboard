import json

#filename=".json"



con = duckdb.connect('implications.db')

con.execute('''
    CREATE TABLE implications (
    	"path" varchar(100),
        "from" INTEGER[],
        "conf" FLOAT,
        "to" INTEGER,
        "support" INTEGER,
        "realsupport" INTEGER,
        "source" TEXT
    )
''')

def add_implication(con, path )

	with open(path, 'r') as file:
    	# Load the contents of the file into a dictionary
    		data = json.load(file)

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
			con.execute(f"INSERT INTO implications VALUES ({path},{data['f']}, {data['c']}, {data['t']}, {data['support']}, {data['real']}, 'dict')")

		

