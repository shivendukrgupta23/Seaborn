import matplotlib.pyplot as plt  
import seaborn as sns 
import pandas as pd   

var = sns.load_dataset("tips")

sns.countplot(x="sex",data=var,hue="smoker",
              color="g",saturation=1)
plt.show()