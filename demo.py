import duckdb
import pandas as pd
import itertools
import util

conn=duckdb.connect('dbbasis.db')

q2='''select   college,  major,ft, c1,c2,c3,count(*) c from raw_data 
group by
GROUPING SETS (( college, major , ft,c1,c2,c3),  (college) )
order by college, ft, major
'''

df2=conn.execute(q2).df()
n2,e2=util.build_graph(df2)
L2=util.get_labels(n2)
S2,T2,V2=util.get_edges(e2)