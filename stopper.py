import os
import platform
import socket
import time

from flask import Flask, render_template, request

app = Flask(__name__)


def shutdown():
    """Detect OS and run appropriate shutdown command"""
    if platform.system() == "Windows":
        os.system('shutdown -s -c "Go to sleep, big things tomorrow! (shutting down in 20 seconds)" -t 20')
    else:
        os.system("shutdown now -h")


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        shutdown()
        return render_template('goodnight.html')
    else:
        return render_template('shutdown.html')


if __name__ == '__main__':
    time.sleep(30)
    app.run(host=socket.gethostbyname(socket.gethostname()), port=9843)
