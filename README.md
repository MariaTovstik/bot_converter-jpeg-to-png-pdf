# bot_converter-jpeg-to-png-pdf
> The bot that converts jpeg-images to png- or pdf 

Bot uses pyTelegramBotApi library to work with Telegram.


```shell
git clone https://github.com/MariaTovstik/bot_converter-jpeg-to-png-pdf.git
cd bot_converter-jpeg-to-png-pdf
python3 -m venv venv
venv\Scripts\activate (on Windows)
sourse venv/bin/activate (on macOS)
pip install -r tequirements.txt
Enter your telegram api key to config.py
python bot.py run
```

### Ideas for improvements


- Add reverse conversation (PDF to JPEG, PNG to JPEG etc.)
- Add buttons  or keyboard to select the conversation format
- Add conversion option for more document/images formats