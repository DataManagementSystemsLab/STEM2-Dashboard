import pandas as pd
import duckdb

# Load Excel file into a Pandas DataFrame
df = pd.read_excel('col_names.xlsx', sheet_name='Sheet1')

# Connect to DuckDB and create a table
con = duckdb.connect(database='dbbasis.db')
con.execute("CREATE TABLE col_mapping (col INTEGER, name TEXT, category TEXT);")

# Insert the data from the DataFrame into the DuckDB table
con.execute('BEGIN')
for index, row in df.iterrows():
    values = row.values.tolist()
    con.execute("INSERT INTO col_mapping VALUES (?, ?, ?)", values)
con.execute('COMMIT')

# Close the connection
con.close()
