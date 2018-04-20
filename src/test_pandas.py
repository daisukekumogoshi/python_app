import pandas as pd
import numpy as np

python_list = [1, 3, 5, np.nan, None, -1]
pandas_series = pd.Series(python_list)
print(python_list)

python_table = [['alice', 100], ['bob', 200], ['charlie', 300]]
pandas_dataframe = pd.DataFrame(python_table, columns=['name', 'score'])
print(pandas_dataframe)
pandas_dataframe.to_csv('C:\\testFolder\hori.csv')