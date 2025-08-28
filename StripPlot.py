import matplotlib.pyplot as plt 
import seaborn as sns  
#import pandas as pd   

var = sns.load_dataset("tips")
sns.stripplot(x="day",y="total_bill",data=var
              ,hue="sex",palette="rocket_r",linewidth=1,
              edgecolor="r",alpha = 0.2)
plt.show()