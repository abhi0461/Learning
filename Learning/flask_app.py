##-- Working code with flask serving on WSGI server (waitress)

from flask import Flask
import subprocess
from waitress import serve

app = Flask(__name__)

@app.route('/open_windows_app')
def open_windows_app():
    print("open_windows_app function called...")
    subprocess.run('control')
    return "open_windows_app"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
