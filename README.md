# Bloomberg-Terminal-Project
This project is a lightweight, automated “Bloomberg Terminal” for monitoring stock movements and related news — built entirely in Python. While full Bloomberg Terminals are expensive and feature-rich, this script demonstrates the core functionality of tracking stock prices and delivering actionable news

This project is perfect for anyone interested in stocks, financial news, and automating notifications using Python and Twilio.
Features
Fetches daily stock prices from Alpha Vantage API.
Calculates the percentage change between the last two trading days.
If the change exceeds 5%, fetches the top 3 news articles for the company from NewsAPI.
Sends the news headlines and brief descriptions to your WhatsApp number using Twilio.
Easily configurable to monitor any stock or company.

How to Use

1.Install twilio using pip

2.Get your API keys:
  Alpha Vantage (stock data):
  https://www.alphavantage.co/support/#api-key
  NewsAPI (news data):
  https://newsapi.org/register
  Twilio (WhatsApp messaging):
  https://www.twilio.com/try-twilio

3.Update the script (main.py) with your own API keys and Twilio credentials

4.Run the Script


