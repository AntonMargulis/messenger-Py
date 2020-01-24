from flask import Flask, request
import datetime
import time

app = Flask(__name__)

messages = [
    {"username": "Jack", "text": "Hello!", "time": time.time()},
    {"username": "Mary", "text": "Hi, Jack!", "time": time.time()},
]
users = {
    'Jack': '12345',
    'Mary': '09876',
}


@app.route("/")
def hello_view():
    return "<h1>Welcome to Python messenger!</h1>"


@app.route("/status")
def status_view():
    server_status = {
        'live_status': True,
        'time from datetime': datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        'time from time': time.asctime()
    }

    return str('Server status: ') + str(server_status['live_status']) + \
           str('<br>') + \
           str('Current server time from datetime: ') + str(server_status['time from datetime']) + \
           str('<br>') + \
           str('Current server time from time: ') + str(server_status['time from time']) + \
           str('<br>') + \
           str('Current number of users: ') + str(len(users)) + \
           str('<br>') + \
           str('Current number of messages: ') + str(len(messages))


@app.route("/messages")
def messages_view():
    """
    Получение сообщений после отметки after
    input: after - отметка времени
    output: {
        "messages" [
            "username": str, "text": str, "time": float()
        ]
    }
    """
    after = float(request.args['after'])
    new_messages = [message
                    for message in messages
                    if message['time'] > after]
    return {'messages': new_messages}


@app.route("/send", methods=['POST'])
def send_view():
    """
    Отправка сообщений
    input: {
        "username": str,
        "password": str,
        "text": str
    }
    output: {"ok": bool}
    """
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in users or users[username] != password:
        return {"ok": False}

    text = data["text"]
    messages.append({"username": username, "text": text, "time": time.time()})

    return {'ok': True}


@app.route("/auth", methods=['POST'])
def auth_view():
    """
    Авторизовать пользователя или соообщить, что пароль неверный
    input: {
        "username": str,
        "password": str,
    }
    output: {"ok": bool}
    """
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in users:
        users[username] = password
        return {"ok": True}
    elif users[username] == password:
        return {"ok": True}
    else:
        return {"ok": False}


app.run()
