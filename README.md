# subdomainx-bot
The telegram bot that help you find all subdomains for a given domain.
![](https://i.imgur.com/hWvtRxQ.png)

> Notes: This bot doesn't have any logic for finding subdomains, just grab the result of request from [rapiddns.io](https://rapiddns.io)

## Setup
1. Create your own telegram bot through [BotFather](https://t.me/BotFather) and grab the API TOKEN.
2. Create the `.env` file inside directory and store your own bot API TOKEN into variable.
```
TOKEN=your-own-bot-api-token
```
3. Install `dotenv`, `python-telegram-bot`, `httpx` library.
```
python -m pip install dotenv python-telegram-bot httpx
```
4. Run the bot `python app.py`
5. `/start` the bot, then send the domain.
