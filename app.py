from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    telegram_token = '7908641572:AAEfO9aBUbE26xA5BF_XjQQnpSk3-QFjac4'
    chat_id = '-1002447941825'
    message = f"Форма заполнена! Данные: {data}"
    requests.post(f'https://api.telegram.org/bot{telegram_token}/sendMessage', data={'chat_id': chat_id, 'text': message})
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
