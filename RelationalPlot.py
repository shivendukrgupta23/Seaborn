# Relational Plot:
# . To see the statistical relation between 2 or more variables.
# .Bivariate analysis

# Plot under this section :
# .Scatter Plot -> axes level function
# .Line Plot


import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px  

# tips = sns.load_dataset("tips")


# sns.scatterplot(data= tips, x="total_bill",y='tip',hue="sex",
#                 style="time",size="size")
# plt.show()

#relplot-> figure level-> works with relplot
#it will not work with scatterplot, line plot


# sns.relplot(x="total_bill",y="tip",data=tips,kind="scatter")
# plt.show()



#Line Plot->axes Level -> its formed graph like rectangle form

gap= px.data.gapminder()
temp=gap[gap['country'] == 'India']
temp_df = gap[gap['country'].isin(["India","Pakistan","China"])]


# sns.relplot(x="year",y="lifeExp",kind="line",data=temp_df,hue='country')
# #sns.lineplot(x="year",y="lifeExp",data=temp)
# plt.show()



#factplot
# var= sns.load_dataset("tips")
# sns.relplot(x="total_bill",y='tip',kind="line",
#             data=var,col="smoker",row='sex')
# plt.show()


#col wrap
gap= px.data.gapminder()
sns.relplot(data=gap,x='lifeExp',y="gdpPercap",
            kind="scatter",col="year",col_wrap=3)
plt.show()