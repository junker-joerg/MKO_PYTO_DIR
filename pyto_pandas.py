import pandas as pd
import statsmodels as sm

import requests

# 1) Warnings in jupyter abschalten
import warnings
warnings.filterwarnings("ignore")
# 2) requests noch mit 3 Beispielen besser verstehen
# 3) Dataframes scrollbar a z
import io
import requests
url="https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
s=requests.get(url).content
df =pd.read_csv(io.StringIO(s.decode('utf-8')))    
# df.info()



# AttributeError: module 'numpy' has no attribute '__config__'


import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
reg.score(X, y)
