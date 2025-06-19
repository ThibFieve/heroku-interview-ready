import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the index.html file from the current directory
    return send_file('index.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    # Heroku assigns a dynamic port, so we use os.environ.get("PORT")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    