import numpy as np
import pandas as pd
import random as rd
import csv
from datetime import datetime,timedelta
#config
NO_OF_DAYS=35
ra=rd.seed(35)
rows=[]
for i in range(NO_OF_DAYS):
    insta_min=rd.randint(1,1000)
    study_min=rd.randint(1,1000)
    youtube_min=rd.randint(1,1000)
    whatapp_min=rd.randint(1,1000)
    youtube_shorts_time=rd.randint(1,1000)
    youtube_watch_time=rd.randint(1,1000)
    li=[insta_min,study_min,youtube_min,youtube_watch_time,youtube_shorts_time]
    rows.append(li)
with open("digital_data.csv","w",newline='',encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["insta_min","study_min","youtube_min","watch_time","youtube_shorts_time"])
    writer.writerows(rows)
