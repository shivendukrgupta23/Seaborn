import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd   

var = sns.load_dataset("tips").head(20)

sns.pairplot(var,kind="kde",
             hue="sex",hue_order=["Female","Male"])
plt.show()
