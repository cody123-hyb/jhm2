import requests
import matplotlib.pyplot as plt

# 定义 OpenWeatherMap API 的基本信息
api_key = '65e48f988ae30c4af07ee29855ec28f7'
base_url = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city_name):
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # 使用公制单位（摄氏度）
    }
    response = requests.get(base_url, params=params)
    return response.json()

def plot_weather_data(weather_data):
    fig, ax = plt.subplots()
    ax.set_title('Weather parameters Visualization')
    
    # 提取天气数据
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    weather_condition = weather_data['weather'][0]['description']
    uv_index = "N/A"  # OpenWeatherMap 免费 API 不提供紫外线指数
    
    # 打印天气数据
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather Condition: {weather_condition}")
    print(f"UV Index: {uv_index}")
    
    # 绘制图表（这里只显示温度、湿度和风速）
    ax.plot([temperature], label='Temperature (°C)')
    ax.plot([humidity], label='Humidity (%)')
    ax.plot([wind_speed], label='Wind Speed (m/s)')
    
    ax.legend()
    plt.show()

def main():
    city_name = input("Enter your city name:")
    weather_data = get_weather_data(city_name)
    if weather_data:
        display_weather_chart(weather_data,city_name)

if __name__ == "__main__":
    main()

