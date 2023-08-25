from flask import Flask , render_template
from flask_socketio import SocketIO , send
from flask import make_response
import os

app = Flask(__name__ )
app.config['SECRET'] = '1234'
socketio = SocketIO(app, cors_allowed_origins = '*')

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    if message != "User connected!":
        send(message , broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

    

if __name__ == "__main__":
    socketio.run(app , host= "0.0.0.0")