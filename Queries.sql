create table data_1 as select * from raw_data;

| 2   | NotRetainYear1to2Binary                  | nan      |
-- | 60  | InitialMajorSTEM
13  | NeverGraduatedAnywhere



alter table data_1 add column transfer_credits varchar(10);
update data_1 set transfer_credits = null;
update  data_1 set transfer_credits= '0-19' where c75;
update  data_1 set transfer_credits= '20-39' where c76;
update  data_1 set transfer_credits= '40-59' where c77;
update  data_1 set transfer_credits= '60-' where c78;

-- how many show up in each attribute 75-78 (number of transfer credits)

| college | transfer_credits | count_star() |
|---------|------------------|--------------|
| adelphi | 0-19             | 16           |
| adelphi | 20-39            | 87           |
| adelphi | 40-59            | 89           |
| adelphi | 60-              | 125          |
| hofstra | 0-19             | 299          |
| hofstra | 20-39            | 189          |
| hofstra | 40-59            | 176          |
| hofstra | 60-              | 220          |
/*
select college, transfer_credits, c2, c60, c13, (c22 or c23), count (*)
from data_1
where transfer_credits is not null
group by college, transfer_credits, c2, c60, c13, (c22 or c23);

pivot (
select college, transfer_credits, c2, c60, c13, (c22 or c23), count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits, grouping sets (  c2, c60, c13, (c22 or c23), (c2, c60),  (c2, c60, c13 ), (c2, c60, c13, (c22 or c23)  ))
)
on 
 college, transfer_credits ;
*/
/*
 pivot (
select college, transfer_credits, c2, c60, c13, (c22 or c23) T, count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits, c2, c60, c13,  (c22 or c23) 
)
on 
 c2, c60, c13, T using sum(cnt);
*/
 pivot (
select college, transfer_credits, c2, c60, c13, (c22 or c23) T, count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits, c2, c60, c13,  (c22 or c23) 
order by college, transfer_credits
)
on  c2, c60, c13, T using sum(cnt) ; 

 pivot (
select college,  c2, c60, c13, (c22 or c23) T, count (*) cnt
from data_1
where transfer_credits is not null
group by college,  c2, c60, c13,  (c22 or c23) 
order by college
)
on  c2, c60, c13, T using sum(cnt) ; 

 pivot (
select college, transfer_credits,  count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits
order by college, transfer_credits
)
on  transfer_credits using sum (cnt);



 pivot (
select college, transfer_credits, c2, count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits, c2
order by college, transfer_credits
)
on  transfer_credits using sum (cnt);



 pivot (
select college, transfer_credits, c60, count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits, c60
order by college, transfer_credits
)
on  transfer_credits using sum (cnt);



 pivot (
select college, transfer_credits, c13, count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits, c13
order by college, transfer_credits
)
on  transfer_credits using sum (cnt);



 pivot (
select college, transfer_credits, (c22 or c23), count (*) cnt
from data_1
where transfer_credits is not null
group by college, transfer_credits, (c22 or c23)
order by college, transfer_credits
)
on  transfer_credits using sum (cnt);

B
how many in each attribute 184-190 (transfer GPA)

.output
alter table data_1 add column transfer_gpa varchar(10);
update data_1 set transfer_gpa = null;
update  data_1 set transfer_gpa= 'NA' where c184;
update  data_1 set transfer_gpa= '0-2' where c185;
update  data_1 set transfer_gpa= '2-2_6' where c186;
update  data_1 set transfer_gpa= '2_6-3' where c187;
update  data_1 set transfer_gpa= '3-3_3' where c188;
update  data_1 set transfer_gpa= '3_3-3_6' where c189;
update  data_1 set transfer_gpa= '3_6-4' where c190;
.mode csv
.output qb0.csv
 pivot (
select college, transfer_gpa, c2, c60, c13, (c22 or c23) T, count (*) cnt
from data_1

group by college, transfer_gpa, c2, c60, c13,  (c22 or c23) 
order by college, transfer_gpa
)
on  c2, c60, c13, T using sum(cnt) ; 

.output qb1.csv
 pivot (
select college,  c2, c60, c13, (c22 or c23) T, count (*) cnt
from data_1

group by college,  c2, c60, c13,  (c22 or c23) 
order by college
)
on  c2, c60, c13, T using sum(cnt) ; 

.output qb2.csv
 pivot (
select college, transfer_gpa,  count (*) cnt
from data_1

group by college, transfer_gpa
order by college, transfer_gpa
)
on  transfer_gpa using sum (cnt);

.output qb3.csv


 pivot (
select college, transfer_gpa, c2, count (*) cnt
from data_1

group by college, transfer_gpa, c2
order by college, transfer_gpa
)
on  transfer_gpa using sum (cnt);

.output qb4.csv

 pivot (
select college, transfer_gpa, c60, count (*) cnt
from data_1

group by college, transfer_gpa, c60
order by college, transfer_gpa
)
on  transfer_gpa using sum (cnt);

.output qb5.csv

 pivot (
select college, transfer_gpa, c13, count (*) cnt
from data_1

group by college, transfer_gpa, c13
order by college, transfer_gpa
)
on  transfer_gpa using sum (cnt);


.output qb6.csv


 pivot (
select college, transfer_gpa, (c22 or c23), count (*) cnt
from data_1

group by college, transfer_gpa, (c22 or c23)
order by college, transfer_gpa
)
on  transfer_gpa using sum (cnt);

/* select c99, c100, c101, c102, c103, c104, count(*) from raw_data  group by GROUPING SETS (c99, c100, c101, c102, c103, c104, ());;

  184-190

  
Sure! Here's the list you requested:


c83, c84, c85, c86
c184, c185, c186, c187, c188, c189, c190


| 151 | GenChem1GradeA           | nan      |
| 152 | GenChem1GradeB           | nan      |
| 153 | GenChem1GradeC           | nan      |
| 154 | GenChem1GradeD           | nan      |
| 155 | GenChem1GradeF           | nan      |
| 156 | GenChem1GradeW           | nan      |
| 157 | GenChem1GradeBplusB      | nan      |
| 158 | GenChem1GradeBminusCplus | nan      |
| 159 | GenChem1GradeCCminus     | nan      |
| 160 | GenChem1GradeDplusD      | nan      |
| 161 | GenChem1GradeDFW         | nan      |

*/

 update  rdata set genchem1= 'A' where c151;
 update  rdata set genchem1= 'B' where c152;
 update  rdata set genchem1= 'C' where c153;
 update  rdata set genchem1= 'D' where c154;
 update  rdata set genchem1= 'F' where c155;
 update  rdata set genchem1= 'W' where c156;
 update  rdata set genchem1= 'B+' where c157;
 update  rdata set genchem1= 'B-' where c158;
update  rdata set genchem1= 'C-' where c159;
update  rdata set genchem1= 'D+' where c160;

| 162 | GenChem2GradeA           | nan      |
| 163 | GenChem2GradeB           | nan      |
| 164 | GenChem2GradeC           | nan      |
| 165 | GenChem2GradeD           | nan      |
| 166 | GenChem2GradeF           | nan      |
| 167 | GenChem2GradeW           | nan      |
| 168 | GenChem2GradeBplusB      | nan      |
| 169 | GenChem2GradeBminusCplus | nan      |
| 170 | GenChem2GradeCCminus     | nan      |
| 171 | GenChem2GradeDplusD      | nan      |
| 172 | GenChem2GradeDFW         | nan      |



 update  rdata set genchem2= 'A' where c162;
 update  rdata set genchem2= 'B' where c163;
 update  rdata set genchem2= 'C' where c164;
 update  rdata set genchem2= 'D' where c165;
 update  rdata set genchem2= 'F' where c166;
 update  rdata set genchem2= 'W' where c167;
 update  rdata set genchem2= 'B+' where c168;
 update  rdata set genchem2= 'B-' where c169;
update  rdata set genchem2= 'C-' where c170;
update  rdata set genchem2= 'D+' where c171;

| 173 | OrgChem1GradeA           | nan      |
| 174 | OrgChem1GradeB           | nan      |
| 175 | OrgChem1GradeC           | nan      |
| 176 | OrgChem1GradeD           | nan      |
| 177 | OrgChem1GradeF           | nan      |
| 178 | OrgChem1GradeW           | nan      |
| 179 | OrgChem1GradeBplusB      | nan      |
| 180 | OrgChem1GradeBminusCplus | nan      |
| 181 | OrgChem1GradeCCminus     | nan      |
| 182 | OrgChem1GradeDplusD      | nan      |
| 183 | OrgChem1GradeDFW         | nan      |



 update  rdata set orgchem1= 'A' where c173;
 update  rdata set orgchem1= 'B' where c174;
 update  rdata set orgchem1= 'C' where c175;
 update  rdata set orgchem1= 'D' where c176;
 update  rdata set orgchem1= 'F' where c177;
 update  rdata set orgchem1= 'W' where c178;
 update  rdata set orgchem1= 'B+' where c179;
 update  rdata set orgchem1= 'B-' where c180;
update  rdata set orgchem1= 'C-' where c181;
update  rdata set orgchem1= 'D+' where c182;


(c129 or c130 or c131 or c132 or c133 or c134 or c135 or c136 or c137 or c138 or c139)

| 129 | IntroBio1GradeA           | nan      |
| 130 | IntroBio1GradeB           | nan      |
| 131 | IntroBio1GradeC           | nan      |
| 132 | IntroBio1GradeD           | nan      |
| 133 | IntroBio1GradeF           | nan      |
| 134 | IntroBio1GradeW           | nan      |
| 135 | IntroBio1GradeBplusB      | nan      |

| 136 | IntroBio1GradeBminusCplus | nan      |
| 137 | IntroBio1GradeCCminus     | nan      |
| 138 | IntroBio1GradeDplusD      | nan      |
| 139 | IntroBio1GradeDFW         | nan      |

| 140 | IntroBio2GradeA           | nan      |
| 141 | IntroBio2GradeB           | nan      |
| 142 | IntroBio2GradeC           | nan      |
| 143 | IntroBio2GradeD           | nan      |
| 144 | IntroBio2GradeF           | nan      |
| 145 | IntroBio2GradeW           | nan      |
| 146 | IntroBio2GradeBplusB      | nan      |
| 147 | IntroBio2GradeBminusCplus | nan      |
| 148 | IntroBio2GradeCCminus     | nan      |
| 149 | IntroBio2GradeDplusD      | nan      |
| 150 | IntroBio2GradeDFW         | nan      |


 update  rdata set introBio2= 'A' where c140;
 update  rdata set introBio2= 'B' where c141;
 update  rdata set introBio2= 'C' where c142;
 update  rdata set introBio2= 'D' where c143;
 update  rdata set introBio2= 'F' where c144;
 update  rdata set introBio2= 'W' where c145;
 update  rdata set introBio2= 'B+' where c146;
 update  rdata set introBio2= 'B-' where c147;
update  rdata set introBio2= 'C-' where c148;
update  rdata set introBio2= 'D+' where c149;


D , (genchem1 is null) ,count(*) from rdata group by (orgchem1 is null), (genchem1 is null), (genchem2 is null), (introbio1 is null), (introbio2 is null);;

select count(*) from rdata where (orgchem1 is not null) or (genchem1 is not null) or (genchem2 is not null) or (introbio1 is not null) or (introbio2 is not null);


select  (orgchem1 is null), (genchem1 is null), (genchem2 is null), (introbio1 is null), (introbio2 is null) , count(*)
from rdata group by grouping sets ( (orgchem1 is null), (genchem1 is null), (genchem2 is null), (introbio1 is null), (introbio2 is null));

select   (orgchem1  in ('A','B','B+','C','C-','C+','B-'))   orgchem1P,
(genchem1  in ('A','B','B+','C','C-','C+','B-'))   genchem1P,
(genchem2  in ('A','B','B+','C','C-','C+','B-'))   genchem2P,
(introbio1  in ('A','B','B+','C','C-','C+','B-'))   introbio1P,
(introbio2  in ('A','B','B+','C','C-','C+','B-'))   introbio2P
 , count(*)
from rdata group by grouping sets ( 
    (orgchem1  in ('A','B','B+','C','C-','C+','B-')),  
(genchem1  in ('A','B','B+','C','C-','C+','B-')),
(genchem2  in ('A','B','B+','C','C-','C+','B-')),
(introbio1  in ('A','B','B+','C','C-','C+','B-')),
(introbio2 in ('A','B','B+','C','C-','C+','B-')))



select  
  count(*)
from rdata where 
    (orgchem1  in ('A','B','B+','C','C-','C+','B-')) or
(genchem1  in ('A','B','B+','C','C-','C+','B-')) or
(genchem2  in ('A','B','B+','C','C-','C+','B-')) or 
(introbio1  in ('A','B','B+','C','C-','C+','B-')) or
(introbio2 in ('A','B','B+','C','C-','C+','B-'))


