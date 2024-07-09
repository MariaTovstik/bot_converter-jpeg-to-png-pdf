import io
import telebot
from PIL import Image
from telebot import types

bot = telebot.TeleBot('YOUR API-KEY')
chats_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Вiтаю, {message.from_user.first_name}! Надішліть мені JPEG або PNG'
                                      f' зображення, щоб конвертувати його в PDF, PNG або JPEG.')


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
        elif message.document.mime_type == 'image/png':
            img = Image.open(io.BytesIO(downloaded_file))
            markup = types.InlineKeyboardMarkup()
            jpeg_button = types.InlineKeyboardButton('JPEG', callback_data='jpeg')
            pdf_button = types.InlineKeyboardButton("PDF", callback_data="pdf")
            markup.add(jpeg_button, pdf_button)
            bot.send_message(message.chat.id, "Оберiть формат конвертацiї:", reply_markup=markup)
            chats_data[message.chat.id] = {'img': img}
        else:
            bot.send_message(message.chat.id, 'Будь ласка, надішліть зображення у форматі JPEG або PNG.')

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Виникла помилка при обробці файлу.')


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    try:
        img = chats_data.get(call.message.chat.id, {}).get('img')
        if call.data == "png":
            # Конвертацiя в PNG
            png_bio = io.BytesIO()
            img.save(png_bio, format='PNG')
            png_bio.seek(0)
            bot.send_document(call.message.chat.id, png_bio, visible_file_name=f'converted_image.png')
        elif call.data == "pdf":
            # Конвертацiя в PDF
            pdf_bio = io.BytesIO()
            img.save(pdf_bio, format='PDF', resolution=100)
            pdf_bio.seek(0)
            bot.send_document(call.message.chat.id, pdf_bio, visible_file_name=f'converted_image.pdf')

        elif call.data == "jpeg":
            # Конвертацiя в JPEG
            jpeg_bio = io.BytesIO()
            img.save(jpeg_bio, format='JPEG')
            jpeg_bio.seek(0)
            bot.send_document(call.message.chat.id, jpeg_bio, visible_file_name='converted_image.jpg')

        bot.send_message(call.message.chat.id, "Виконано!")

    except Exception as e:
        print(e)
        bot.send_message(call.message.chat.id, 'Виникла помилка при обробці файлу.')


bot.polling(non_stop=True)
