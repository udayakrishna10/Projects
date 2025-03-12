import json
from datetime import datetime
import requests
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("weather")

def get_weather_data(city):
    api_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "q": city,
        "key": "<KEY>"
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        if 'current' in data:
            return data
        else:
            print(f"Missing 'current' data for {city}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return None

def lambda_handler(event, context):
    cities = ["Chicago", "Ames", "Nashville", "Sydney", "Mumbai", "Boston", "London", "Venice", "Paris", "Davenport"]
    
    for city in cities:
        data = get_weather_data(city)
        
        if data is not None:
            temp = data['current']['temp_c']
            wind_speed = data['current']['wind_mph']
            wind_dir = data['current']['wind_dir']
            pressure_mb = data['current']['pressure_mb']
            humidity = data['current']['humidity']
    
            print(city, temp, wind_speed, wind_dir, pressure_mb, humidity)
            current_timestamp = datetime.utcnow().isoformat()

            item = {
                'city': city,
                'time': str(current_timestamp),
                'temp': temp,
                'wind_speed': wind_speed,
                'wind_dir': wind_dir,
                'pressure_mb': pressure_mb,
                'humidity': humidity
            }
            item = json.loads(json.dumps(item), parse_float=Decimal)
            
            try:
                table.put_item(
                    Item=item
                )
            except Exception as e:
                print(f"Error inserting data into DynamoDB for {city}: {e}")
