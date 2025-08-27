import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd   



var = [1,2,3,4,5,6,7]
var_1 = [2,3,4,1,5,6,7]

# plt.plot(var,var_1)
# plt.show()

# x_1= pd.DataFrame({"var":var, "var_1":var_1})
# sns.lineplot(x="var",y="var_1",data=x_1)
# plt.show()

#Seaborn start 

y_1 = sns.load_dataset("penguins").head(20)
# print(y_1.head())
# print(y_1.info())
# print(y_1.describe())

#to bulid the graph with the help of parameters Like bill_length_mm
#palette = palette is basically a set of colors used for the plot.
#the legend is the box (usually on the right side of the plot) that explains what different colors/markers represent.

sns.lineplot(x="bill_length_mm", y="flipper_length_mm", data=y_1,hue="sex",style="sex",
             palette="Accent",markers=["o",">"],dashes=False,legend="full")
plt.grid()
plt.title("python")
plt.show()
