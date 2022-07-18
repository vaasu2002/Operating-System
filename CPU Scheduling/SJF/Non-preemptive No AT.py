# Non-preemptive SJF(SHORTEST JOB FIRST) Scheduling with Arrival Time
print("Non-preemptive SJF Scheduling without Arrival Time")
import pandas as pd
import matplotlib.pyplot as plt
def MakeDIctionary_SJF(AT,BT,n,Process_Name,d={}):
    for index in range(n):
        l = [BT[index],AT[index]]
        d[Process_Name[index]] = l
    d = sorted(d.items(), key=lambda x: x[1][0])
    AT = [i[1][0] for i in d]
    BT = [i[1][1] for i in d]
    return d,AT
def TurnAroundTime(BT,n,AT,TAT=[],CT=[]):
    TAT = [sum(BT[0:i+1])-AT[i] for i in range(n)]
    return TAT,sum(TAT)/n
def WaitingTime(TAT,BT,n):
    WT = [TAT[i]-BT[i] for i in range(n)]
    return WT,sum(WT)/n

n = int(input("Enter number of process: "))
Process_Name = ["P"+str(i+1) for i in range(n)]
BT = [int(input(f"Enter Burst Time(ms) for process {x+1}:- ")) for x in range(n)]
AT=[0 for i in range(n)]
d,BT = MakeDIctionary_SJF(AT,BT,n,Process_Name)
print(d)
TAT,ATAT = TurnAroundTime(BT,n,AT)
WT,AWT = WaitingTime(TAT,BT,n)
Process_Name = [i[0] for i in d]
data = {"Name" : Process_Name,
        "BT" : BT,
        "AT" : AT,
        "TAT" : TAT,
        "WT" : WT}
df = pd.DataFrame(data)
print(df)
def visualizeSJF(Process_Name,BT):
    x = pd.DataFrame({"c":[BT[0]]},index=["Process"])
    for i in range(len(BT)):
        x[Process_Name[i]] = BT[i]
    x.drop('c',inplace=True,axis=1)
    x.plot.barh(stacked=True)
visualizeSJF(Process_Name,BT)
print(f"Average Turn Around Time: {ATAT}")
print(f"Average Waiting time: {AWT}")
