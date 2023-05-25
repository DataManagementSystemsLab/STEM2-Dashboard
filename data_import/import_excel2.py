import openpyxl
import duckdb

# Open the XLSX file
wb = openpyxl.load_workbook('dbbasis.xlsx')

# Create a new DuckDB database
conn = duckdb.connect('dbbasis.db')

# Create a new table in the database for all sheets
c = conn.cursor()

fields = []
fields.insert(0, "sheet_title varchar(30)")
fields.insert(1, "row_no int")
fields.insert(2, "col_no int")

fields.insert(3, "val BOOLEAN")


c.execute(f'CREATE TABLE vals ({",".join(f"{field} " for field in fields)})')

# Loop through all sheets in the workbook
for ws in wb:
    if "total" in ws.title.lower():
        continue
    row_count=0    
    for row in list(ws.iter_rows(min_row=2, values_only=True)):
        # Convert the fields to Booleans (1 or 0)
        
        row_count=row_count+1

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
            c.execute(sql)
# Commit changes and close database connection
conn.commit()
conn.close()
