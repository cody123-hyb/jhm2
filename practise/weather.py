import requests
import matplotlib.pyplot as plt

# 定義和風天氣 API 的基本信息
api_key = '你的_API_KEY'
base_url = 'https://api.qweather.com/v1/weather/now'

def get_weather_data(city_name):
    params = {
        'location': city_name,
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()

def plot_weather_data(weather_data):
    fig, ax = plt.subplots()
    ax.set_title('Weather parameters Visualization')
    
    # 提取天氣數據
    temperature = weather_data['temperature']
    humidity = weather_data['humidity']
    wind_speed = weather_data['wind_speed']
    weather_condition = weather_data['weather']
    uv_index = weather_data['uv_index']
    
    # 繪製圖表
    ax.plot(temperature, label='Temperature')
    ax.plot(humidity, label='Humidity')
    ax.plot(wind_speed, label='Wind Speed')
    ax.plot(weather_condition, label='Weather Condition')
    ax.plot(uv_index, label='UV Index')
    
    ax.legend()
    plt.show()

if __name__ == "__main__":
    city_name = input("請輸入城市名：")
    weather_data = get_weather_data(city_name)
    plot_weather_data(weather_data)
