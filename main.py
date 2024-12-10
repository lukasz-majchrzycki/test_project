import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lbs_to_kg = 0.45359237
feet_to_m = 1.0
inch_to_m = 25.4/1000

def getFeet(height):
    return float( height[0:height.find("'")] )

def getInch(height):
    return float( height[height.find("'")+1:-1].replace(",", ".")  ) 

w = lambda x: (float( x.replace(" lbs.", "")) * lbs_to_kg )
h = lambda x: (getFeet(x) * feet_to_m + getInch(x) * inch_to_m  )

BMIdf = pd.read_csv('BMI.csv',  sep=";", converters={"Weight": w, "Height": h})

BMIdf["BMI"] = BMIdf["Weight"]/BMIdf["Height"]**2
BMI_categories = pd.DataFrame({
    "name" : ["Underweight", "Healthy Weight", "Overweight", "Class 1 Obesity", "Class 2 Obesity", "Severe Obesity"],
    "min": [0, 18.5, 25.0, 30.0, 35.0, 40.0],
    "max": [18.5, 25.0, 30.0, 35.0, 40.0, 1000.0]
})
bins = [0] + BMI_categories["max"].tolist()
labels = BMI_categories["name"].tolist()

BMIdf["BMI_category"] = pd.cut(BMIdf["BMI"], bins=bins, labels=labels, right=False)

BMIdf["BMI_category"].hist()
plt.xticks(rotation=60)
plt.show()