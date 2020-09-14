from datetime import datetime
from time import *
starttime=time()
t=ctime(starttime)
# print(asctime(localtime(time())))
print(t)
sleep(2)
dt=datetime
dt1=datetime.now()
print(dt1)
dt=datetime.today()
print(dt)
print(dt.day,dt.date(),dt.month,dt.year)

