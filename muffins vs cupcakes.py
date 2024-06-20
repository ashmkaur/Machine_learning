#packages for data analysis
import numpy as np  # array calc..
import pandas as pd # dataframes

from sklearn import svm

#visulize your data
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)
#%matplotlib inline
recipes= pd.read_csv('Cupcakes vs Muffins.csv')
# print(recipes.head())

# plot our data

sns.lmplot(x='Flour', y='Sugar', data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})




