from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Ваш код для обработки данных
    # Например, отправим сообщение в Telegram
    telegram_token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    message = f"Форма заполнена! Данные: {data}"
    requests.post(f'https://api.telegram.org/bot{telegram_token}/sendMessage', data={'chat_id': chat_id, 'text': message})
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
