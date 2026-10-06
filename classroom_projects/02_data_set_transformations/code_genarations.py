import pandas as pd
import numpy as ny
df=pd.read_csv("day02_usage.csv")
# Day,Chat,Video,Study,Games
chat_array=df["Chat"].to_numpy()
video_array=df["Video"].to_numpy()
Study_array=df["Study"].to_numpy()
Games_array=df["Games"].to_numpy()
print(f"The no of days{len(chat_array)}")
print(f"the total minutes of each app {chat_array.sum()} {video_array.sum()},{Study_array.sum()} {Games_array.sum()}\n")
print(f"the average minutes of each app {chat_array.mean():.1f} ,{Study_array.mean():.1f} ,{Games_array.mean():.1f} ,{video_array.mean():.1f}")
diff_studyAndGame=Study_array-Games_array;
print(f"the best day {diff_studyAndGame.argmax()+1} and worst day {diff_studyAndGame.argmin()+1}")
max_day_array=[]
for i in range(len(Study_array)):
    temp=ny.array([Study_array[i],Games_array[i],chat_array[i],video_array[i]])
    idx=temp.argmax()
    temp2=["study","Games","chat","Video"]
    print(f"The max of day {i+1} is {temp2[idx]}")
total_array=Study_array+Games_array+video_array+chat_array
average_study_array=(Study_array/total_array)*100
average_video_array=video_array/total_array *100
average_games_array=Games_array/total_array *100
average_chat_array=chat_array/total_array *100

