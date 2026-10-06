import pandas as pd
import numpy as ny
df=pd.read_csv("day02_usage.csv")
# Day,Chat,Video,Study,Games
chat_array=df["Chat"].to_numpy()
video_array=df["Video"].to_numpy()
Study_array=df["Study"].to_numpy()
Games_array=df["Games"].to_numpy()
print(f"The no of days{len(chat_array)}")
print(f"the total minutes {chat_array.sum()+video_array.sum()+Study_array.sum()+Games_array.sum()} and the average minutes per day{(chat_array.sum()+video_array.sum()+Study_array.sum()+Games_array.sum())/3:1}")
diff_studyAndGame=Study_array-Games_array;
print(f"the best day {diff_studyAndGame.argmax()+1} and worst day {diff_studyAndGame.argmin()+1}")
