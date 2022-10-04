
"""
@author: Ztark
"""
import pandas as pd
import math
from random import choice

def importData(path):
    df = pd.read_excel(path, engine="odf")
    return df.values.tolist()

def choosePeople(number,data):
    chosen = list()
    data2 = data.copy()
    for i in range(number):
        P = choice(data2)
        data2.remove(P)
        chosen.append(P)
    return chosen

def magicNumber(data,factor):
    return 1+math.floor(len(data)/factor)

if __name__ == "__main__":
    base_path = "data.ods"
    factor = 3
    
    datalist = importData(base_path)
    L = choosePeople(magicNumber(datalist,factor),datalist)
    for i in range(len(L)):
        print(f"[{i+1}] {L[i][0]}")
