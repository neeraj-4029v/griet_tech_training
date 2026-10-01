import csv
import random as rd
list=[]
rd.seed()
for i in range(100):
    student_id=i
    branch=rd.choice(["CSE","ECE","IT","MECH"])
    python_Score=rd.randint(10,100)
    SQL_Score=rd.randint(10,100)
    Aptitude_Score=rd.randint(10,100)
    Communication_Score=rd.randint(10,100)
    Project_completed=rd.randint(0,11)
    Mock_Interviwes_Attended=rd.randint(0,11)
    list.append([student_id,branch,python_Score,SQL_Score,Aptitude_Score,Communication_Score,Project_completed,Mock_Interviwes_Attended])
with open("placement_readiness.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(['student_id','branch','python_Score','SQL_Score','Aptitude_Score','Communication_Score','Project_completed','Mock_Interviwes_Attended'])
    writer.writerows(list)


