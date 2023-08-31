import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={'/':'./src/'})
@sio.event
def connect(sid , environ):
    print(sid , "connectd") 

@sio.event
def disconnect(sid):
    print(sid , 'Disconnected')
