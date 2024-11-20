import discord
from discord.ext import commands
import requests
from datetime import datetime


TOKEN = 'TOKEN'
WEATHERSTACK_API_KEY = 'WEATHERSTACK_API_KEY'
WEATHERSTACK_ENDPOINT = "http://api.weatherstack.com/current"  # Use the appropriate endpoint
WEATHERSTACK_HISTORICAL_ENDPOINT = 'http://api.weatherstack.com/historical'
ACCUWEATHER_API_KEY = 'ACCUWEATHER_API_KEY'
ACCUWEATHER_SEARCH_ENDPOINT = "http://dataservice.accuweather.com/locations/v1/cities/search"


intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')  # Remove the default help command


def safe_get(data, *keys):
    for key in keys:
        if key in data:
            data = data[key]
        else:
            return None
    return data
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def weather(ctx, city: str):
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city
    }

    response = requests.get(WEATHERSTACK_ENDPOINT, params=params).json()

    if response.get('error'):
        await ctx.send(response['error']['info'])
        return

    location = response['location']['name']
    temperature = response['current']['temperature']
    description = response['current']['weather_descriptions'][0]
    wind_speed = response['current']['wind_speed']
    humidity = response['current']['humidity']

    weather_info = (
        f"🌍 **Weather in {location}** 🌍\n"
        f"🌡 Temperature: {temperature}°C\n"
        f"🌫 Description: {description}\n"
        f"💨 Wind Speed: {wind_speed} km/h\n"
        f"💧 Humidity: {humidity}%\n"
    )
    await ctx.send(weather_info)






@bot.command()
async def location(ctx, city: str):
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city
    }
    response = requests.get(WEATHERSTACK_ENDPOINT, params=params).json()
    country = response['location']['country']
    region = response['location']['region']
    lat = response['location']['lat']
    lon = response['location']['lon']

    await ctx.send(f"🌍 Location: {city}, {region}, {country}\n" +
                   f"🌐 Latitude: {lat}, Longitude: {lon}")

@bot.command()
async def wind(ctx, city: str):
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city
    }
    response = requests.get(WEATHERSTACK_ENDPOINT, params=params).json()
    wind_speed = response['current']['wind_speed']
    wind_dir = response['current']['wind_dir']

    await ctx.send(f"🌬 Wind in {city}: {wind_speed} km/h, Direction: {wind_dir}")


@bot.command()
async def pressure(ctx, city: str):
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city
    }
    response = requests.get(WEATHERSTACK_ENDPOINT, params=params).json()
    pressure = response['current']['pressure']

    await ctx.send(f"🌡 Atmospheric Pressure in {city}: {pressure} hPa")

@bot.command()
async def visibility(ctx, city: str):
    params = {
        "access_key": WEATHERSTACK_API_KEY,
        "query": city
    }
    response = requests.get(WEATHERSTACK_ENDPOINT, params=params).json()
    visibility = response['current']['visibility']

    await ctx.send(f"🌁 Visibility in {city}: {visibility} km")



@bot.command()
async def help(ctx):
    help_text = """
    🌦 **Weather Bot Help** 🌦
    Here are the commands you can use:
    🔍 `!weather [CITY]`: Detailed current weather.
    📍 `!location [CITY]`: Overview of the queried location.
    🌬 `!wind [CITY]`: Wind speed and direction.
    🌡 `!pressure [CITY]`: Atmospheric pressure.
    🌁 `!visibility [CITY]`: How clear the sky is.
    """
    await ctx.send(help_text)

bot.run(TOKEN)
