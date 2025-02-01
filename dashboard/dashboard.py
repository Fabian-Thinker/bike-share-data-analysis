import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

main_data = pd.read_csv('dashboard/main_data.csv')

st.title('Bike Sharing Dashboard')

st.sidebar.title("Informasi")
st.sidebar.write("Ini adalah dashboard untuk menganalisis data peminjaman sepeda berdasarkan tanggal, musim, kondisi cuaca, dan jenis peminjam.")
st.sidebar.write("Pilih tahun dan bulan untuk menentukan tren peminjaman sepeda pada bulan dan tahun tertentu.")

st.subheader('Filter Data')
tahun = st.selectbox('Pilih Tahun', [2011, 2012])
bulan = st.selectbox('Pilih Bulan', main_data['mnth'].unique())


st.write(
'''
#### Tren peminjaman sepeda pada bulan tertentu
'''
)
plt.figure(figsize=(15, 6))
sns.lineplot(x='dteday', y='cnt', data=main_data[(main_data['yr'] == tahun) & (main_data['mnth'] == bulan)], color='brown')
plt.title(f'Dately Bike Rental in {bulan} {tahun}')
plt.xlabel('Date')
plt.ylabel('Rental Amount')
plt.xticks(rotation=45)
plt.grid(True)

st.pyplot(plt)

st.write(
'''
#### Pada kondisi cuaca dan musim apa sepeda terpinjam paling banyak dan paling sedikit?
'''
)

weathery_amounts = main_data[(main_data['yr'] == tahun) & (main_data['mnth'] == bulan)].groupby('weathersit').cnt.sum().sort_values(ascending=False)
sizes = weathery_amounts.values
labels = weathery_amounts.index
weather_color = {'Clear': 'deepskyblue', 'Cloudy': 'silver', 'Light Snow/Rain': 'snow', 'Heavy Rain': 'gray'}
colors = [weather_color.get(label, 'black') for label in labels]

fig_weather, ax = plt.subplots(figsize=(7, 5))
ax.bar(labels, sizes, color=colors, edgecolor='black')

ax.set_title(f'Bike Rented Weatherly in {bulan} {tahun}')
ax.set_xlabel('Weather')
ax.set_ylabel('Rental amount')

for i, value in enumerate(sizes):
    ax.text(i, value + 500, str(value), ha='center', va='bottom')

st.pyplot(fig_weather)

#seasonal is only yearly, not effected by month input

seasonal_amounts = main_data[main_data['yr'] == tahun].groupby('season').cnt.sum().sort_values(ascending=False)
sizes = seasonal_amounts.values
labels = seasonal_amounts.index
season_color = {'Winter': 'paleturquoise','Spring': 'greenyellow','Summer': 'khaki','Autumn': 'indianred'}
colors = [season_color[label] for label in labels]

fig_season, ax = plt.subplots(figsize=(7, 5))
ax.bar(labels, sizes, color=colors, edgecolor='black')

ax.set_title(f'Bike Rented Seasonally in {tahun}')
ax.set_xlabel('Season')
ax.set_ylabel('Rental Amount')
for i, value in enumerate(sizes):
    ax.text(i, value + 500, str(value), ha='center', va='bottom')

st.pyplot(fig_season)

st.write(
'''
#### Berapa total peminjaman casual dan registered pada bulan tertentu?
'''
)

registered, casual = main_data[(main_data['yr'] == tahun) & (main_data['mnth'] == bulan)][['registered', 'casual']].sum()

st.subheader(f'Total Peminjaman di {bulan} {tahun}')
st.write(f"Registered: {registered}")
st.write(f"Casual: {casual}")

st.caption('Fabian©copyright')
