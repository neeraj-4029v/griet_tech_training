import numpy as ny
import csv
insta_list=[]
study_list=[]
with open("digital_behaviour.csv","r",encoding='utf-8') as f:
    reader=csv.DictReader(f)
    for row in reader:
        insta_list.append(row["Instagram_Minutes"])
        study_list.append(row["Study_Minutes"])
insta_array=ny.array(insta_list[0:7],dtype='i')
study_array=ny.array(study_list[0:7],dtype='i')
print(insta_array,'\n',study_array)
total_insta=ny.sum(insta_array)#insta_array.sum()
total_study=ny.sum(study_array)#study_array.sum()
avg_insta=insta_array.mean()
avg_study=study_array.mean()
max_insta=insta_array.max()
max_study=study_array.max()
min_insta=insta_array.min()
min_study=study_array.min()
help(insta_array)
First_day_insta=insta_array[0]
First_day_study=study_array[0]
last_day_insta=insta_array[-1]
last_day_study=study_array[-1]
firstThreeDay_insta=insta_array[0:3]
firstThreeDay_study=study_array[0:3]
lastThreeDay_insta=insta_array[-2::]
lastThreeDay_study=study_array[-2::]
twotofour_study=study_array[1:4]
twoto4_insta=insta_array[1:4]
#insta_array=[val/60 for val in insta_array]
#study_array=[val/60 for val in study_array]
insta_array_hours=insta_array/60
study_array_hours=study_array/60
diff_array=insta_array-study_array
#[val >100 for val in insta_array]
#[val >100 for val in study_array]
Greater_than_100_insta=insta_array>100
Greater_than_100_study=study_array>100
#print(Greater_than_100_insta,"\n",Greater_than_100_study)
Greater_study=study_array[Greater_than_100_study]
Greater_insta=insta_array[Greater_than_100_insta]
count_insta=insta_array[insta_array>100].sum()
count_study=study_array[study_array>100].sum()
Above_avg_insta=insta_array[insta_array>avg_insta]
Above_avg_study=study_array[study_array>avg_study]




