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
df=pd.read_csv("placement_readiness.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
print(df[df["python_Score"]>75])
df=df.sort_values(by="Aptitude_Score",ascending=False)
df_top_10_by_Python=df.sort_values(by="python_Score",ascending=False).head(10)
print(df_top_10_by_Python)
print(df[df["python_Score"]>df["Communication_Score"]])
df["Total_Score"]=df["python_Score"]+df["Communication_Score"]+df["Aptitude_Score"]+df["SQL_Score"]
df["Average_Score"]=df["Total_Score"]/4
df["Weakest_skill_Score"]=df[["python_Score","Communication_Score","Aptitude_Score","SQL_Score"]].min(axis=1)
df["Readiness_Score"]=df["Average_Score"]+(df["Project_completed"]*2)+(df["Mock_Interviwes_Attended"])
df["Readiness_Score"]=df["Readiness_Score"].where(df["Readiness_Score"]<=100,100)
df["Readiness_band"]=pd.cut(df["Readiness_Score"],bins=[0,60,75,100],labels=['Needs Work','Almost ready','ready'])
ff.to_csv("placement_readiness.csv")






