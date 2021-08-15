import pandas as pd
import csv

planet_data = pd.read_csv('merged_data.csv')

print(planet_data.shape)

print(list(planet_data))

del planet_data['Luminosity']

del planet_data['Unnamed: 6']

del planet_data['Star_name.1']

del planet_data['Distance.1']

del planet_data['Mass.1']

del planet_data['Radius.1']

planet_data = planet_data[planet_data['Mass'].notna()]
planet_data = planet_data[planet_data['Radius'].notna()]

print(planet_data.shape)

print(list(planet_data))

planet_data.to_csv('planet_data_cleaned.csv')