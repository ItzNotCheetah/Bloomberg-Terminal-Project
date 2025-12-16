# Bloomberg-Terminal-Project
This project is a lightweight, automated “Bloomberg Terminal” for monitoring stock movements and related news — built entirely in Python. While full Bloomberg Terminals are expensive and feature-rich, this script demonstrates the core functionality of tracking stock prices and delivering actionable news:

  -Monitors daily stock prices for any company (default: Tesla Inc / TSLA).
  -Calculates daily percentage changes in stock price.
  -Fetches the top 3 relevant news articles if the stock moves more than 5%, providing real-time context for market changes.
  -Sends the news and stock movement alerts directly to your WhatsApp via Twilio.
Essentially, this project combines market data and news aggregation, delivering instant insights just like a Bloomberg Terminal — but in a simple, free, and customizable Python script.

Why it’s like a Bloomberg Terminal:
  -Price alerts: Tracks stock movement and highlights significant changes.
  -News aggregation: Shows relevant news that could impact stock decisions.
  -Real-time notifications: Alerts delivered instantly via WhatsApp.
  -Customizable: Easily modify it for any stock or company.

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

Notes
  -By default, the script monitors Tesla Inc (TSLA). You can change STOCK_NAME and COMPANY_NAME to monitor any stock.
  -Make sure your Twilio account has a WhatsApp sandbox enabled for testing.



