import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
import calmap
from data_prep import full_table

# organize data

covid_data = pd.read_csv('novel-corona-virus-2019-dataset/covid_19_data.csv')

# print full_table.isna().sum()
case_vars = ['Confirmed', 'Deaths', 'Recovered', 'Active']

full_table['Active'] = full_table['Confirmed'] - full_table['Deaths'] - full_table['Recovered']
full_table['Province/State'] = full_table['Province/State'].fillna('Undefined')
full_table[case_vars] = full_table[case_vars].fillna(0)

ship_data = full_table[full_table['Province/State'].str.contains('Diamond Princess') |
                       full_table['Province/State'].str.contains('Grand Princess')]
chinese_data = full_table.loc[full_table['Country/Region'] == 'China']
world_data = full_table.loc[full_table['Country/Region'] != 'China']

full_latest = full_table[full_table['Date'] == max(full_table['Date'])].reset_index()
china_latest = full_latest.loc[full_latest['Country/Region'] == 'China']
world_latest = full_latest.loc[full_latest['Country/Region'] != 'China']

full_latest_grouped = full_latest.groupby('Country/Region')[case_vars].sum().reset_index()
china_latest_grouped = china_latest.groupby('Province/State')[case_vars].sum().reset_index()
world_latest_grouped = world_latest.groupby('Country/Region')[case_vars].sum().reset_index()

# visual case comparison -------------------------------------------------------

province_data = full_latest.groupby(['Country/Region', 'Province/State'])['Confirmed', 'Deaths','Recovered','Active'].max()

latest_case_totals = full_latest.groupby('Date')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum()
lct_temp = latest_case_totals.melt(id_vars='Date', value_vars=case_vars[1:])
lct_fig = px.treemap(lct_temp, path=['variable'],
                               values='value',
                               height=400,
                               width=600,
                               color_discrete_sequence=['#003f5c', '#bc5090', '#ffa600'])

# lct_fig.show()

# heatmap of case totals by country --------------------------------------------

countrywise_cases = full_latest_grouped.loc[full_latest_grouped['Confirmed'] > 50].sort_values(by='Confirmed', ascending=False).set_index('Country/Region')
countrywise_cases = pd.DataFrame(countrywise_cases)

plt.figure(figsize=(6,10))
plt.title('Country Case Heatmap')
cmap = sns.cm.rocket_r
sns.heatmap(countrywise_cases, annot=True, linewidth=.5, cmap=cmap, fmt='d')

plt.show()
