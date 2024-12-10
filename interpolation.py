import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)
ser = pd.Series(np.arange(1, 8, 0.25) **2   + np.random.randn(28)*3 )
ser2=ser.copy()

missing = np.array([4, 13, 14, 15, 16, 17, 18, 20])
ser.iloc[missing] = np.nan
methods = ["linear", "quadratic", "cubic", 'spline']

df = pd.DataFrame({m: ser.interpolate(method=m, order=2) for m in methods})

df["data"]=ser
df["missing"]=ser2

nanFilter = df.query("data.notnull()" )
df.loc[ nanFilter.index,  "missing"] = np.nan

df[["data", "linear", "quadratic", "cubic", "spline", "missing"]].plot(style=['o', '-', '-', '-', '-', 'X'])
plt.show()