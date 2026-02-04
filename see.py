import seaborn as sns
import pandas as pd
data = sns.load_dataset('iris')
print(data)


import pandas as pd
import seaborn as sns
data = sns.load_dataset('iris')
# This command tells pandas to show EVERY row
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(data)