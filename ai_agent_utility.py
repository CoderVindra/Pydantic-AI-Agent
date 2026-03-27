import os
import requests
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


# Load env vriables
load_dotenv()


# define output schema
class WeatherForecast(BaseModel):
    location : str
    description : str
    temperature_celsius : float

# Initialize weather AI agent
weather_agent = Agent(
    model="groq:llama-3.1-8b-instant",
    output_type=str,
    system_prompt=(
        "You are a helpful weather assistant. Use the 'get_weather_forecast' "
        "tool to find the current weather conditions of any city. "
        "Provide clear and friendly answer."
    )
)

# register tool for AI agent
@weather_agent.tool
def get_weather_forecast(ctx : RunContext, city : str) -> WeatherForecast:
    """returns the current weather forecast of a city."""
    params = {
        "q": city,
        "appid": os.environ.get("API_KEY", "your api key"),
        "units": "metric"
    }

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather", 
        params=params
    )
    result = response.json()

    return WeatherForecast(
        location=result['name'],
        description=result['weather'][0]['description'].capitalize(),
        temperature_celsius=result['main']['temp']
    )
