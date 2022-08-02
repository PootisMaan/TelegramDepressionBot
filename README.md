  <h3 align="center">Test Depression Telegram Bot</h3>
  <p align="center">
    This telegram bot allows you to find out if you have depression.
    <br/>
    The CES-D (Center for Epidemiologic Studies Depression Scale) scale-questionnaire is intended for screening for the detection of depressive disorder in patients. The questionnaire was developed in the USA in 1977 and is by far the most commonly used in the world.
    <br/>
  </p>
</p>

## Getting Started

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/dborodin836/TelegramDepressionBot.git
$ cd TelegramDepressionBot
```

## Setup

If you don't have [Python](https://www.python.org/downloads/) install it.

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m venv env
$ cd env/Scripts
$ activate
$ cd ../../
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Obtain API Token for your bot. [Guide](https://core.telegram.org/bots)

And set in bot.py file.

```
--- bot.py ---

     ...
15 |
16 | bot = telebot.TeleBot(${ YOUR API TOKEN })
17 | 
     ...
```

And finally run the bot:

```sh
(env)$ py bot.by
```


## Screenshots

**NOTE: Bot currently available only in russian.**

[![image.png](https://i.postimg.cc/htPsTxQz/image.png)](https://postimg.cc/QHwcrFbh)

[![image.png](https://i.postimg.cc/cJ1JsxjN/image.png)](https://postimg.cc/68SKcXtH)

[![image.png](https://i.postimg.cc/pVB5MSy8/image.png)](https://postimg.cc/3WdxgnXJ)

