import io
import telebot
from PIL import Image
from telebot import types

bot = telebot.TeleBot('YOUR API')
chats_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Вiтаю, {message.from_user.first_name}! Надішліть мені JPEG зображення, щоб'
                                      f' конвертувати його в PNG і PDF.')


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if message.document.mime_type == 'image/jpeg':
            img = Image.open(io.BytesIO(downloaded_file))

            markup = types.InlineKeyboardMarkup()
            png_button = types.InlineKeyboardButton("PNG", callback_data="png")
            pdf_button = types.InlineKeyboardButton("PDF", callback_data="pdf")
            markup.add(png_button, pdf_button)

            bot.send_message(message.chat.id, "Оберiть формат конвертацiї:", reply_markup=markup)
            chats_data[message.chat.id] = {'img': img}
        else:
            bot.send_message(message.chat.id, 'Будь ласка, надішліть зображення у форматі JPEG.')

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Виникла помилка при обробці файлу.')


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    try:
        img = chats_data.get(call.message.chat.id, {}).get('img')
        if call.data == "png":
            # Конвертация в PNG
            png_bio = io.BytesIO()
            img.save(png_bio, format='PNG')
            png_bio.seek(0)
            bot.send_document(call.message.chat.id, png_bio, visible_file_name=f'converted_image.png')
        elif call.data == "pdf":
            # Конвертация в PDF
            pdf_bio = io.BytesIO()
            img.save(pdf_bio, format='PDF', resolution=100)
            pdf_bio.seek(0)
            bot.send_document(call.message.chat.id, pdf_bio, visible_file_name=f'converted_image.pdf')

        bot.answer_callback_query(call.id, "Виконано!")
    except Exception as e:
        print(e)
        bot.send_message(call.message.chat.id, 'Виникла помилка при обробці файлу.')


bot.polling(none_stop=True)
