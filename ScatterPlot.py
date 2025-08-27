import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd  


var = sns.load_dataset("penguins").head(20)
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",
                data=var,hue="sex",style="sex",size="sex",sizes=(100,40)
                ,palette="gist_ncar",alpha=1)
plt.show()