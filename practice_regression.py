from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""     
- s1      tc, total serum cholesterol
- s2      ldl, low-density lipoproteins
- s3      hdl, high-density lipoproteins
- s4      tch, total cholesterol / HDL
- s5      ltg, possibly log of serum triglycerides level
- s6      glu, blood sugar level
- Target  Column 11 is a quantitative measure of disease progression one year after baseline
"""
diabetes = load_diabetes(as_frame=True)

df = diabetes.frame
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print(len(y.unique()))
