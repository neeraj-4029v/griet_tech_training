import csv
APP="instagram"
list=[]
with open("digital_behaviour.csv","r",encoding='utf-8') as f:
    reader=csv.DictReader(f)
    for all_apps in reader:
        list.append(int(all_apps["Instagram_Minutes"]))
print(list[0:7])
total=sum(list[0:7])
print(total)
avg=total/7
print(avg)
max=max(list[0:7])
min=min(list[0:7])
print(max," ",min)
count=0
for min in list[0:7]:
    if(avg<min):
        count+=1
print(count)
print(f"APPName:{APP}\n The 7 Days of \nTotal:{total}\nAverage:{avg}\nMaximum:{max}\nMinimum:{min}\nabove the Average:{count}")