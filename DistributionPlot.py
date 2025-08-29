#Distribution Plots:
# . used for univariate analysis
# .used to find out the distribution
# .range of the observation
# .central Tendency
# .is the data bimodal?
# .are the outliers

# Its under :
#     .histplot
#     .kdeplot
#     .rugplot
#figure level -> displot
#axes level -> histplot, kdeplot,rugplot


# import seaborn as sns 
# import matplotlib.pyplot as plt 

# var = sns.load_dataset("tips")


# # sns.histplot(x="total_bill",data=var)

# sns.displot(data=var,x="tip",hue="sex", kind="hist")

# plt.show()



#kde Plot:

import seaborn as sns 
import matplotlib.pyplot as plt 

var = sns.load_dataset("tips")

# sns.kdeplot(data=var,x="total_bill")
# plt.show()

sns.histplot(data=var,x="total_bill", y="tip")
plt.show()