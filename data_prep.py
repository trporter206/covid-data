import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

confirmed_data = pd.read_csv('novel-corona-virus-2019-dataset/time_series_covid_19_confirmed.csv')
deaths_data = pd.read_csv('novel-corona-virus-2019-dataset/time_series_covid_19_deaths.csv')
recovered_data = pd.read_csv('novel-corona-virus-2019-dataset/time_series_covid_19_recovered.csv')

dates = confirmed_data.columns[4:]

confirmed_data_clean = confirmed_data.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                           value_vars=dates,
                                           var_name='Date',
                                           value_name='Confirmed')
deaths_data_clean = deaths_data.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                           value_vars=dates,
                                           var_name='Date',
                                           value_name='Deaths')
recovered_data_clean = recovered_data.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                           value_vars=dates,
                                           var_name='Date',
                                           value_name='Recovered')
full_table = pd.concat([confirmed_data_clean, deaths_data_clean['Deaths'], recovered_data_clean['Recovered']],
                             axis=1,
                             sort=False)

full_table = full_table[full_table['Province/State'].str.contains(',')!= True]

full_table.to_csv('covid_19_data_cleaned', index=False)
