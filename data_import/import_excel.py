import openpyxl
import duckdb
import pandas as pd


wb = openpyxl.load_workbook('data/dbbasis.xlsx')

conn = duckdb.connect('dbbasis.db')

fields = [f"c{i} BOOLEAN" for i in range(1, 219)]
fields.insert(0, "sheet_title varchar(30)")
fields.insert(1, "row_no int")
conn.execute(f'CREATE TABLE raw_data ({",".join(f"{field} " for field in fields)})')

fields = []
fields.insert(0, "sheet_title varchar(30)")
fields.insert(1, "row_no int")
fields.insert(2, "col_no int")
fields.insert(3, "val BOOLEAN")
conn.execute(f'CREATE TABLE vals ({",".join(f"{field} " for field in fields)})')

conn.commit()

# Loop through all sheets in the workbook
for ws in wb:
	if "total" in ws.title.lower():
		continue

	row_count=0   
	for row in list(ws.iter_rows(min_row=2, values_only=True)):
		# Convert the fields to Booleans (1 or 0)
		row_count=row_count+1
		srow = [int(field) if isinstance(field, bool) else field for field in row]
		srow.insert(0,ws.title)
		srow.insert(1,row_count)
		formatted_list = [f"'{field}'" if isinstance(field, str) else str(field) for field in srow]
		sql=f'INSERT INTO raw_data VALUES ('+','.join(formatted_list)+");"
		print(sql)
		conn.execute(sql)

		col_count=0
		for field in row:
			col_count=col_count+1
			srow=[]	
			srow.insert(0,ws.title)
			srow.insert(1,row_count)
			srow.insert(2, col_count)
			val=int(field)
			srow.insert(3, val)
			formatted_list = [f"'{field}'" if isinstance(field, str) else str(field) for field in srow]
			sql=f'INSERT INTO vals VALUES ('+','.join(formatted_list)+");"
			print(sql)
			conn.execute(sql)
# Commit changes and close database connection
conn.commit()



# Load Excel file into a Pandas DataFrame
df = pd.read_excel('data/col_names.xlsx', sheet_name='Sheet1')

conn.execute("CREATE TABLE col_mapping (col INTEGER, name TEXT, category TEXT);")

# Insert the data from the DataFrame into the DuckDB table
conn.execute('BEGIN')
for index, row in df.iterrows():
    values = row.values.tolist()
    conn.execute("INSERT INTO col_mapping VALUES (?, ?, ?)", values[:3])
conn.execute('COMMIT')

# Close the connection
conn.close()

