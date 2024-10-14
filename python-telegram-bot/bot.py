from telebot import TeleBot, types

TOKEN = '7529559498:AAFbg6-V0NjTRFkPrdWH1Z31OjQehAoQ-iw'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    answer = (f'<b>Привет, </b> <b><u>{message.from_user.first_name}</u></b>\n\n'
              f'Бот представляет полный ассортимент кроссовок магазина <a href="https://t.me/Rshoptut">Rshop</a>.'
              f' Чтобы оформить заказ, пожалуйста, перейдите в «Каталог», выберите нужную модель кроссовок и укажите данные получателя.'
              f' После этого ожидайте сообщение от менеджера для подтверждения заказа.\n\n'
              f'По заказу и вопросам, пишите в специальный бот по кнопке «Поддержка».')

    bot.send_message(message.chat.id, text=answer, parse_mode='HTML')




if __name__ == '__main__':
    bot.polling(non_stop=True)