import telebot

# Токен API, получается у BotFather
TOKEN = '1118590522:AAFIXZ2RbT5KQAaoRsXaM1dmkxboFm2E2JA'

# Объект бота
BOT = telebot.TeleBot(TOKEN)

# IS_NUMERATOR: bool = input("Is Numerator?")
IS_NUMERATOR = True

DAYS = [r'пн', r'вт', r'ср', r'чт', r'пт']

STICKERS = {
    'go_fuck_urslf':
        'CAACAgIAAxkBAAIgSWA3-6kDhEPXc76-aetU7AWmF-yLAAKPAAOMgEUSfLi37KtGpWgeBA',
    'honey_or_in_the_face':
        'CAACAgIAAxkBAAIhWWA4IEatwgABNJ93dIrxHNzaYScrawACmgADjIBFEiiUTEB1nq2nHgQ',
    'faggot':
        'CAACAgIAAxkBAAIhWGA4H9n6_FOdgJcKkkPJ0AaRdNEvAAKXAAOMgEUSvBmWQqShtO4eBA',
    'i_see_ur_fucked':
        'CAACAgIAAxkBAAIhWmA4IHVfN9p01szCR-jZwJD9CpnOAAJlAAOMgEUSIRnIEE7mWjYeBA',
    'u_were_fucked_in_children':
        'CAACAgIAAxkBAAIgSmA3--ddAjN8ZRtau1wp3EccgtH-AAKbAAOMgEUSXhu5Q5FXG-0eBA'
}

