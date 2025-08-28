import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd  

var = sns.load_dataset("tips").head(20)
sns.catplot(x="tip",y="size",data=var,
            hue="sex")
plt.show()