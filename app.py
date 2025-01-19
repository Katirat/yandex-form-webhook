from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
 

    # Отправляем сообщение в Telegram
    response = requests.post(f'https://api.telegram.org/bot{telegram_token}/sendMessage', json={'chat_id': chat_id, 'text': message})
    
    if response.status_code != 200:
        return f"Ошибка отправки сообщения. Код: {response.status_code}", 500

    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

