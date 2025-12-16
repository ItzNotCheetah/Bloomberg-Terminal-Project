import requests
import os
from twilio.rest import Client

# In this example I use Tesla but you can change it to any Equity
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# --------------------------
# CONFIGURATION
# --------------------------
# Set your own API keys and Twilio credentials in environment variables.
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_KEY_HERE"
NEWS_API_KEY = "YOUR_NEWSAPI_KEY_HERE"
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID_HERE"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN_HERE"
TWILIO_WHATSAPP_FROM = "whatsapp:+1234567890"  # replace with your twilio number
TWILIO_WHATSAPP_TO = "whatsapp:+1234567890"    # replace with your own number

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "apikey" : STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
}

news_parameters = {
    "apiKey" : NEWS_API_KEY,
    "qInTitle" : COMPANY_NAME,
}

# --------------------------
# STEP 1: Get stock prices
# --------------------------
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()

time_series = stock_data["Time Series (Daily)"]
dates = list(time_series.keys())

yesterday_closing_price = float(time_series[dates[0]]["4. close"])
day_before_closing_price = float(time_series[dates[1]]["4. close"])


difference = yesterday_closing_price - day_before_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage = round((difference / day_before_closing_price) * 100)

if abs(percentage) > 5:

    # --------------------------
    # STEP 2: Get first 3news if change > 5%
    # --------------------------
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()["articles"]

    three_articles = news_data[:3]

    # --------------------------
    # STEP 3: Send messages via Twilio
    # --------------------------
    formatted_articles_list = [
        f"{STOCK_NAME}: {up_down}{percentage}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
        for article in three_articles
    ]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles_list:
        message = client.messages.create(
            body= article,
            from_= TWILIO_WHATSAPP_FROM,
            to= TWILIO_WHATSAPP_TO
        )



