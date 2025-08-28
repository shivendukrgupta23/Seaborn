import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd  

var= sns.load_dataset("tips")
sns.factorplot(x="size",y="tip",data=var,hue="sex",
               kind="bar")
plt.show()