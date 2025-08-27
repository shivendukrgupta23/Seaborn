import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd   

var = sns.load_dataset("penguins")
#print(var)
sns.set(style="darkgrid")
order_1 = ["Dream","Torgersen","Biscoe"]
sns.barplot(x="island", y="bill_length_mm",data=var
           ,hue="sex",order =order_1,hue_order = ["Female","Male"],
           ci=80,n_boot=2,saturation=100,errcolor="b"
           ,alpha=0.5)
           
#to represent graph in horizontal form that's we take numeric vallue is allowed  only           
# order_1 = ["Dream","Torgersen","Biscoe"]
# sns.barplot(x="bill_depth_mm", y="bill_length_mm",data=var,
#             orient="h")
plt.show()