import json
import duckdb
from flatten_json import flatten
import pandas

f = open ('data.txt.json', "r")
  
# Reading from file
data = json.loads(f.read())
f_data=flatten(data)



conn = duckdb.connect()

d=conn.execute('''
    SELECT 
        * 
    FROM read_json_auto('data.txt.json',json_format='auto')
''').df()


# connect to an in-memory database
my_df = pandas.DataFrame.from_dict(f_data)

# create the table "my_table" from the DataFrame "my_df"
duckdb.sql("CREATE TABLE my_table AS SELECT * FROM my_df")

# insert into the table "my_table" from the DataFrame "my_df"
duckdb.sql("INSERT INTO my_table SELECT * FROM my_df")

duckdb.sql('SELECT *   from my_df')