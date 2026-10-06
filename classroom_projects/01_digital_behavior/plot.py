import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use("Agg")
df=pd.read_csv("my_analysis.csv")
plt.figure(figsize=(50,50))
plt.bar([f"D{i+1}" for i in range(len(df))],df["Total_Screen_Time"],color="Steelblue")
plt.title("My Screen Time by Day")
plt.xlabel("Day")
plt.ylabel("Total Screen Time")
plt.xticks(rotation=45)
plt.savefig("classroom_projects/01_digital_behavior/visual_rep/total_time.png",dpi=1000)
plt.show()
plt.close()
plt.figure(figsize=(50,50))
total_app={
    "Instagram":df["Instagram_Minutes"].sum(),
    "Whatsapp":df["WhatsApp_Minutes"].sum(),
    "Youtube":df["YouTube_Minutes"].sum(),
    "LinkedIn":df["LinkedIn_Minutes"].sum()
}
plt.bar(total_app.keys(),total_app.values(),color="Red")
plt.title("Total Time by App")
plt.xlabel("App")
plt.ylabel("minutes")
plt.xticks(rotation=45)
plt.savefig("classroom_projects/01_digital_behavior/visual_rep/by_app.png",dpi=1000)
plt.show()
plt.close()
plt.figure(figsize=(50,50))
plt.plot([f"d{i+1}" for i in range(len(df))],df["Study_Minutes"],marker='s',label="study",color="orange")
plt.plot([f"d{i+1}" for i in range(len(df))],df["Total_Screen_Time"],marker='s',label="Screen",color="red")
plt.title("Screen vs study")
plt.xlabel("Day")
plt.ylabel("Total Screen Time")
plt.xticks(rotation=45)
plt.savefig("classroom_projects/01_digital_behavior/visual_rep/ScreenVsStudy.png",dpi=1000)
plt.show()
plt.close()
plt.figure(figsize=(50,50))
plt.pie(total_app.values(),labels=total_app.keys(),colors=['red','orange','blue','purple'],autopct='%3.1f%%',startangle=90)
plt.savefig("classroom_projects/01_digital_behavior/visual_rep/pie.png",dpi=1000)
plt.show()


