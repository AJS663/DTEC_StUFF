 from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# Handle user message
@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    emit('message', message, broadcast=True)  # Broadcast the message to all clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
