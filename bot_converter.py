import io
import telebot
from telebot import types
from PIL import Image

bot = telebot.TeleBot('7495515912:AAHw0oKwFnhc8V1GgTtRaadqssqOcrsKeYA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Вiтаю, {message.from_user.first_name}! Надішліть мені JPEG зображення,щоб'
                                      f' конвертувати його в PNG і PDF та оберiть формат')


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if message.document.mime_type == 'image/jpeg':
            # Конвертация в PNG
            img = Image.open(io.BytesIO(downloaded_file))
            png_bio = io.BytesIO()
            img.save(png_bio, format='PNG')
            png_bio.seek(0)
            bot.send_document(message.chat.id, png_bio, visible_file_name=f'converted_image{message.document.name}.png')

            # Конвертация в PDF
            pdf_bio = io.BytesIO()
            img.save(pdf_bio, format='PDF', resolution=100)
            pdf_bio.seek(0)
            bot.send_document(message.chat.id, pdf_bio, visible_file_name=f'converted_image{message.document.name}.pdf')

        else:
            bot.send_message(message.chat.id, 'Будь ласка, надішліть зображення у форматі JPEG.')

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Виникла помилка при обробці файлу.')


bot.polling(none_stop=True)
