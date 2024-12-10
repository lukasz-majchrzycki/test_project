import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lbs_to_kg = 0.45359237
feet_to_m = 0.3048
inch_to_m = 25.4/1000

def getFeet(height):
    return float( height[0:height.find("'")] )

def getInch(height):
    return float( height[height.find("'")+1:-1].replace(",", ".")  ) 

w = lambda x: (float( x.replace(" lbs.", "")) * lbs_to_kg )
h = lambda x: (getFeet(x) * feet_to_m + getInch(x) * inch_to_m  )

BMIdf = pd.read_csv('BMI.csv',  sep=";", converters={"Weight": w, "Height": h})