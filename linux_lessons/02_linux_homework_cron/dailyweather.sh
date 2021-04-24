#! /bin/sh

# if [ ! $OPEN_WEATHER_API_KEY ]; then
#    echo "You don't have a OpenWeather API Key in environment variable. (OPEN_WEATHER_API_KEY)" >&2
#    echo "You have to set them: "
#    echo "      export OPEN_WEATHER_API_KEY='0000000YOU000KEY0000000'"
#    exit 1
# fi

OPEN_WEATHER_API_KEY='00b8baeea0662bf25260c83739e81f3a'
DEFAULT_FILENAME='weather.json'
CITY_NAME='Kharkiv'
COUNTRY_CODE='UA'

API_URL="api.openweathermap.org/data/2.5/weather?q=$CITY_NAME,$COUNTRY_CODE&appid=$OPEN_WEATHER_API_KEY"

FILE=$1
if [ ! $FILE ]; then
   FILE="$(date '+%Y-%m-%d')-$CITY_NAME-${DEFAULT_FILENAME}"
fi

curl --output $HOME/$FILE $API_URL
