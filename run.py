from flask import Flask, render_template
from flask_socketio import SocketIO
import os, sys


app = Flaske(__name__)
io = SocketIO(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@io.on('connect')
def connect():
	print('Client connected')
	send({'message': 'Client connected',
		  'connection': true }
		 
if __name__ == '__main__':
	io.run(app)
