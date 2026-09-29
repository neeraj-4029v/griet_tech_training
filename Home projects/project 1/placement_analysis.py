import numpy as np
import pandas as pd
import csv 
py_score=[]
ap_score=[]
sql_score=[]
comm_score=[]
with open("placement_readiness.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        py_score.append(int(row["python_Score"]))
        ap_score.append(int(row["Aptitude_Score"]))
        sql_score.append(int(row["SQL_Score"]))
        comm_score.append(int(row["Communication_Score"]))
Python_score_arr=np.array(py_score)
Aptitude_score_arr=np.array(ap_score)
SQL_score_arr=np.array(sql_score)
Communication_score_arr=np.array(comm_score)
print(f"The Average Python score:{Python_score_arr.mean()}")
print(f"the Highest and lowest Aptitude score are :{Aptitude_score_arr.max()} and {Aptitude_score_arr.min()}")
print(f"the students above 70 in communication are:{sum(Communication_score_arr>75)}")
for id in range(len(Python_score_arr)):
    max_value=max(Python_score_arr[id],Aptitude_score_arr[id],SQL_score_arr[id],Communication_score_arr[id])
    min_value=min(Python_score_arr[id],Aptitude_score_arr[id],SQL_score_arr[id],Communication_score_arr[id])
    print(f"the differrence of student {id} is {max_value-min_value}")




