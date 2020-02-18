from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import topSecret
import ephem
import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = "Вызван /start"
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: {}, Chat id: {}, Message: {}".format(update.message.chat.username, update.message.chat.id, update.message.text))
    update.message.reply_text(user_text)


def get_constellation(bot, update):
    planets = {"Mars": ephem.Mars(),
               'Venus': ephem.Venus(),
               'Mercury': ephem.Mercury(),
               'Jupiter': ephem.Jupiter(),
               'Saturn': ephem.Saturn(),
               'Uranus': ephem.Uranus(),
               'Neptune': ephem.Neptune(),
               'Moon': ephem.Moon(),
               'Sun': ephem.Sun(),
               'Pluto': ephem.Pluto()}

    planet_name = update.message.text.split()[1]
    logging.info("Planet: {}".format(update.message.text.split()[1]))
    if planet_name in planets:
        m = planets[planet_name]
        m.compute(datetime.datetime.now())
        reply = "В данный момент {} находится в созвездии {}.".format(planet_name, ephem.constellation(m)[1])
        update.message.reply_text(reply)
    else:
        update.message.reply_text("Введите название планеты солнечной системы!")


def main():
    mybot = Updater(topSecret.API_KEY, request_kwargs=topSecret.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', get_constellation))

    mybot.start_polling()
    mybot.idle()


main()