# 🌦 WeatherWise Bot

<p align="center">
  <img src="https://github.com/user-attachments/assets/738f9e27-6a53-4a43-a88e-9c7e977bea90" alt="WeatherWise Bot " width="100%">
</p>

**WeatherWise Bot** is a feature-rich Discord bot that provides real-time weather updates, location details, and environmental insights for any city worldwide. Powered by Weatherstack and AccuWeather APIs, WeatherWise Bot ensures accurate and timely weather data.

---

## 📜 Table of Contents

- Features
- Tech Stack
- Command List
- Setup and Usage
- Acknowledgments

---

## ✨ Features

- **Current Weather Information**: Provides real-time weather updates for any city.
- **Location Details**: Fetches location information, including country, region, and coordinates.
- **Wind Data**: Reports wind speed and direction for the queried city.
- **Atmospheric Pressure**: Displays the current pressure in hPa.
- **Visibility Metrics**: Shares visibility information in kilometers.
- **User-Friendly Help**: Offers a detailed guide on available commands.

---

## 🛠️ Tech Stack

- **Python**: The programming language used to build the bot.
- **Discord.py**: Library for interacting with the Discord API.
- **Requests**: For making API calls to fetch weather and location data.
- **APIs Used**:
  - **Weatherstack API**: Provides real-time weather and location data.
  - **AccuWeather API**: Enhances location search capabilities.

---

## 🔧 Command List

| Command                          | Description                                                   |
|----------------------------------|---------------------------------------------------------------|
| `!weather [CITY]`                | Provides current weather details for the specified city.      |
| `!location [CITY]`               | Fetches location info, including country and coordinates.     |
| `!wind [CITY]`                   | Displays wind speed and direction for the city.               |
| `!pressure [CITY]`               | Shows the atmospheric pressure in the specified city.         |
| `!visibility [CITY]`             | Reports visibility metrics for the queried city.              |
| `!help`                          | Displays the list of available commands.                     |

---

## 🚀 Setup and Usage

1. **Install Dependencies**:
   Install the required Python libraries using pip:
   
   ```bash
   pip install discord requests
   
3. **Configure API Keys**: Replace placeholders in the script, such as TOKEN, WEATHERSTACK_API_KEY, and ACCUWEATHER_API_KEY, with your valid API keys.
4. **Run the Bot**: Save the file as weatherwise_bot.py and execute it:
5. 
   ```bash
   python weatherwise_bot.py
   
6. **Invite the Bot to Your Server**:
- Go to the Discord Developer Portal.
- Generate an OAuth2 URL under the "OAuth2" section with the bot scope and necessary permissions.
- Use the generated URL to invite the bot to your Discord server.
5. **Test the Commands**:
- Use **!help** in your server to view the list of available commands and test them.
---
## 🙏 Acknowledgments

- **Discord.py Community**: For providing robust documentation and examples.
- **Weatherstack API**: For accurate real-time weather data.
- **AccuWeather API**: For location search functionality.
- **Open-Source Libraries**: Python libraries like requests and discord.py made development seamless.
---

### Thank you for using WeatherWise Bot! 🌦 
