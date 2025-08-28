import matplotlib.pyplot as plt 
import seaborn as sns 

var = sns.load_dataset("tips")
fg=sns.FacetGrid(var,col="sex",hue="day",palette="summer")
fg.map(plt.bar,"total_bill","tip").add_legend()
plt.show()