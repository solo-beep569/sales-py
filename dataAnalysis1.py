import pandas as pd
# import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# https: // www.kaggle.com/datasets/ruchi798/data-science-job-salaries/data?select = ds_salaries.csv

# https: // www.kaggle.com/datasets/rishikeshkanabar/premier-league-player-statistics-updated-daily

handle = 'ruchi798/data-science-job-salaries'
api.dataset_download_files(handle, path='./data', unzip=True)

data = pd.read_csv('./data/data.csv')
pd.options.display.max_rows = 9999

data.corr()
print(data)


# Built in maths  functions
df = pd.read_csv("./data/dataset - 2020-09-24.csv")


df.head()
