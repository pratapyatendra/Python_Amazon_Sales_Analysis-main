import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have some data stored in a variable 'data'
# For example:
# data = pd.read_csv('your_data.csv')

# Now you can create plots using Matplotlib or Seaborn
# For example:

df=pd.read_csv(r'E:\Machine Learning\Python_Amazon_Sales_Analysis-main\Python_Amazon_Sales_Analysis-main\Amazon Sale Report.csv',encoding= 'unicode_escape')
df.shape
sns.scatterplot(x='column1', y='column2')
plt.show()
