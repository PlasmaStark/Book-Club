
"""
@author: Ztark
"""
import pandas as pd
import math
from random import choice

# import data from a .ods file having this format:
# - column 1 : names
# - header : yes (1 row)
# - no other data
# return a list of all partecipants
def importData(path):
    df = pd.read_excel(path, engine="odf")
    return df.values.tolist()

# choose at random an adequate number of people
def choosePeople(number,data):
    chosen = list()
    data2 = data.copy()
    for i in range(number):
        P = choice(data2)
        data2.remove(P)
        chosen.append(P)
    return chosen

# find the adequate number of people to return (empirical!)
def magicNumber(data,factor):
    return 1+math.floor(len(data)/factor)

if __name__ == "__main__":
    base_path = "data.ods"
    factor = 3
    
    datalist = importData(base_path)
    L = choosePeople(magicNumber(datalist,factor),datalist)
    for i in range(len(L)):
        print(f"[{i+1}] {L[i][0]}")
