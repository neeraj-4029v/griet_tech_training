import pandas as pd
import Matplotlib 

df=pd.read_csv("digital_behaviour.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df[["Instagram_Minutes","YouTube_Minutes"]].describe())
print(df["Instagram_Minutes"])
print(df[["Instagram_Minutes","Date"]])
print(df["Instagram_Minutes"].sum())
print(df["Study_Minutes"].mean())
print(df["YouTube_Minutes"].max())
print(df[df["Instagram_Minutes"]>100][["Instagram_Minutes","Study_Minutes"]])
print(df[df["Instagram_Minutes"]>180])
print(df[df["Instagram_Minutes"]>df["Study_Minutes"]])
print(df[df["Instagram_Minutes"]>df["Instagram_Minutes"].mean()])
df=df.sort_values(by=["Instagram_Minutes"],ascending=False)
print(df.head(5))
print(df.sort_values(by=["Study_Minutes"],ascending=True).head(5))
df["Total_Screen_Time"]=df["Instagram_Minutes"]+df["WhatsApp_Minutes"]+df["YouTube_Minutes"]+df["LinkedIn_Minutes"]
df["Screen_hours"]=df["Total_Screen_Time"]/60
df["Digital_Balance"]=df['Study_Minutes']/df["Total_Screen_Time"]
df["Day_Type"]="Normal"
df.loc[df["Total_Screen_Time"]>300,["Day_Type"]]="Heavy"
app_total={
    "instagram":df["Instagram_Minutes"].sum(),
    "youtube":df["YouTube_Minutes"].sum(),
    "linkedin":df["LinkedIn_Minutes"].sum(),
    "whatsApp":df["WhatsApp_Minutes"].sum()
}

print(max(app_total,key=app_total.get))
print((df["Day_Type"]=="Heavy").sum())
print(df["Study_Minutes"].max())
print(df[(df["Total_Screen_Time"])==(df["Total_Screen_Time"].max())]["Study_Minutes"].sum())
print(df["Digital_Balance"].mean())
print(df["Total_Screen_Time"].idxmax())
df.to_csv("my_analysis.csv")





