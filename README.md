# bot_converter-jpeg-to-png-pdf
> A Telegram bot that converts jpeg/png images to pdf,png or jpeg formats

Bot uses pyTelegramBotApi library to work with Telegram and Pillow library to work with images.


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
[Presentation](https://www.canva.com/design/DAGKX6WUxfU/HlUcEgBqhpxDNUcIlSjuLw/view?utm_content=DAGKX6WUxfU&utm_campaign=designshare&utm_medium=link&utm_source=editor)
### Ideas for improvements


- Implement a progress bar for tracking conversion progress
- Implement error handling for more robust operation
- Add buttons  or keyboard to select the conversation format
- Add support for additional image formats(e.g. BMP, GIF)
- Allow users to specify custom file names for converted files