import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('novel-corona-virus-2019-dataset/covid_19_data.csv')
df = data.copy()

null_replacements = {
    'Province/State': 'Undefined',
}
df.fillna(null_replacements, inplace=True)

print df['Province/State'].value_counts()
