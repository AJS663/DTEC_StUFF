from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store the chat messages
chat_messages = []

@app.route('/')
def index():
    return render_template('create_account.html')

@app.route('/chat', methods=['POST'])
def chat():
    username = request.form['username']
    return render_template('chat.html', username=username, chat_messages=chat_messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    chat_messages.append(message)
    return redirect('/chat')

if __name__ == '__main__':
    app.run()