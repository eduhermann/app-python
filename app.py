#!/usr/bin/env python3

from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def container_id():
    container_id = socket.gethostname()
    return "Aplicação rodando no container ID: " + container_id