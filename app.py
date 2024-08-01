from flask import Flask
import threading
import main

app = Flask(__name__)

@app.route('/')
def home():
    return "Discord bot is running!"

def run_bot():
    main.main()

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    app.run(host='0.0.0.0', port=8080)