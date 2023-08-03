import random
from threading import Thread

from flask import Flask

app = Flask("")


@app.route("/")
def home() -> str:
    return "Im in!"


def run() -> None:
    app.run(host="0.0.0.0", port=random.randint(2000, 9000))


def keep_alive() -> None:
    """
    Creates and starts new thread that runs the function run.
    """
    t = Thread(target=run)
    t.start()
