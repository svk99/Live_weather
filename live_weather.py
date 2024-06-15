import requests
import pandas as pd
import streamlit as st

df = pd.read_csv('.../weather_cities_dataset.csv')
df.drop(df[df['cityName'] == 'cityName'].index, inplace=True)

BASE_URL = 'https://www.weatherunion.com/gw/weather/external/v0'
locality_url = '/get_locality_weather_data'
API_KEY = *****

headers = {'content-type': 'application/json', 'x-zomato-api-key': API_KEY}

locality_data = dict(zip(df['localityName'], df['localityId']))

st.subheader('Live Weather Data')

city = st.selectbox('Select city name', df['cityName'].unique())
locality = st.selectbox('Select locality', df[df['cityName'] == city]['localityName'])
locality_id = locality_data[locality]

if st.button('Submit'):
    url = BASE_URL + locality_url + '?locality_id=' + locality_id

    response = requests.get(url, headers=headers)
    response = response.json()
    st.write('The temperature is ', response['locality_weather_data']['temperature'])
    st.write('The humidity is ', response['locality_weather_data']['humidity'])
    st.write('The total rain is ', response['locality_weather_data']['rain_accumulation'])
    st.write('The current rain is ', response['locality_weather_data']['rain_intensity'])
    st.write('The wind speed is ', response['locality_weather_data']['wind_speed'])