from flask import Flask
from flask_socketio import SocketIO
import os, sys


app = Flaske(__name__)

io = SocketIO(app)

@io.on('connect')
def connect():
	print('Client connected')
	send({'message': 'Client connected',
		  'connection': true }
		 
if __name__ == '__main__':
	io.run(app)
