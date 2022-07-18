import pandas as pd
import matplotlib.pyplot as plt

print("Non-preemptive FCFS Scheduling with Arrival Time")
def TurnAroundTime(BT, n, AT, TAT=[], CT=[]):
    TAT = [sum(BT[0:i + 1]) - AT[i] for i in range(n)]
    return TAT, sum(TAT) / n


def WaitingTime(TAT, BT, n):
    WT = [TAT[i] - BT[i] for i in range(n)]
    return WT, sum(WT) / n


def MakeDIctionary(AT, BT, n, d={}):
    for index in range(n):
        l = [AT[index], BT[index]]
        d[keys[index]] = l
    d = sorted(d.items(), key=lambda x: x[1][0]
    AT = [i[1][0] for i in d]
    BT = [i[1][1] for i in d]
    return d, AT, BT


n = int(input("Enter number of process: "))
keys = ["P" + str(i + 1) for i in range(n)]
BT = [
    int(input(f"Enter Burst Time(ms) for process {x+1}:- ")) for x in range(n)
]
AT = [
    int(input(f"Enter Arrival Time(ms) for process {x+1}:- "))
    for x in range(n)
]
d, AT, BT = MakeDIctionary(AT, BT, n)
TAT, ATAT = TurnAroundTime(BT, n, AT)
WT, AWT = WaitingTime(TAT, BT, n)
keys = [d[i][0] for i in range(n)]
data = {"Name": keys, "BT": BT, "AT": AT, "TAT": TAT, "WT": WT}
df = pd.DataFrame(data)
print(df)


def visualizeFCFS(Process_Name, BT):
    x = pd.DataFrame({"c": [BT[0]]}, index=["Process"])
    for i in range(len(BT)):
        x[Process_Name[i]] = BT[i]
    x.drop('c', inplace=True, axis=1)
    x.plot.barh(stacked=True)


print(f"Average Turn Around Time: {ATAT}")
print(f"Average Waiting time: {AWT}")
visualizeFCFS(keys, BT)
