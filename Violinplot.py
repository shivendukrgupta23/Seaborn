import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd   

var = sns.load_dataset("tips")
# sns.violinplot(x="day",y="total_bill",data=var,
#                linewidth=2,palette="Dark2")

sns.violinplot(x="time",y="total_bill",data=var,hue="sex",
               order= ["Dinner","Lunch"],inner="stick")

# sns.violinplot(x="day",y="total_bill",data=var,
#                 hue="sex", split=True,scale="count")
plt.show()