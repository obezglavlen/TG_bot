# Telegram bot

To run this bot you need `.env` file in root of project, with this content:

```sh
TELEGRAM_TOKEN="bot_token"
MONGO_URL="mongo_url"
HEROKU_URL="heroku_url"
```

To run <span style="font-size: 1.5rem; color: lightblue">local</span> you need comment this string and uncomment this

```py
if __name__ == "__main__":
    # If you host bot on Heroku, you can use Flask server for webhook
    comment > server.run(host="0.0.0.0", port=PORT)

    # If you host bot on localhost, you can use bot polling
    uncomment > # BOT.remove_webhook()
    uncomment > # BOT.infinity_polling(allowed_updates=["message", "callback_query"])
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
