import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={'/':'./../src/'}
                       )
@sio.event
def connect(sid , environ):
    print(sid , "connectd") 

@sio.event
def disconnect(sid):
    print(sid , 'Disconnected')

@sio.event
def sum(sid , data):
    result = data['numbers'][0] + data['numbers'][1]
    sio.emit('sum_result' , {'result':result} , to = sid)
