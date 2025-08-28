import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd  

var = sns.load_dataset("tips")
# sns.set(style="whitegrid")

# sns.boxplot(x="day",y="total_bill",data=var
#             ,showmeans=True,color="g",linewidth=3,
#             order=["Fri","Sun","Thur","Sat"],
#             palette="plasma",orient="v")


# sns.boxplot(data=var
#             ,showmeans=True,color="g",
#             palette="plasma",orient="h")

# sns.boxplot(y=var["total_bill"])


#styling implementation 
sns.set_style("white")
#sns.set_context("paper",font_scale=0.2)
#plt.figure(figsize=(12,3))
sns.boxplot(x="day",y="total_bill",data=var)

#sns.despine()
plt.show()