import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd   
import numpy as np 

y={"fontsize":10,"color":"r"}
var = np.linspace(1,10,20).reshape(4,5)

sns.heatmap(var,vmax=10,cmap="gist_heat",annot=True,
            annot_kws=y,linewidths=5,linecolor='b'
            ,cbar=False,xticklabels=False,yticklabels=False)

# data = sns.load_dataset("anagrams")
# x=data.drop(columns=["attnr"],axis=1).head(10)
# sns.heatmap(x)
plt.show()