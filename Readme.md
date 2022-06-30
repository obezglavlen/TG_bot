# Telegram bot

To run this bot you need `.env` file in root of project, with this content:

```sh
TELEGRAM_TOKEN="bot_token"
MONGO_URL="mongo_url"
HEROKU_URL="heroku_url"
ENV="production" | "development"
```

## Install all libraries with

```
pip install -r requirements.txt
```

## Run with

```
python main.py
```

# Bot commands

| Command | Description                                           | Chat types     |
| ------- | ----------------------------------------------------- | -------------- |
| start   | Start work with bot, welcome message, registration    | Group, Private |
| help    | Show command list                                     | Group, Private |
| random  | Random coin flip, or with 1/2 arguments random number | Group, Private |
| search  | Search anime moment by image/gif                      | Group, Private |
| dick    | Simple random game                                    | Group, Private |
| anime   | Work with anime watch list                            | Private        |
