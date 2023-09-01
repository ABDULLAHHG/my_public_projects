import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={'/':'./../src/'}
                       )
@sio.event
async def connect(sid , environ):
    print(sid , "connectd") 

@sio.event
async def disconnect(sid):
    print(sid , 'Disconnected')

@sio.event
async def sum(sid , data):
    result = data['numbers'][0] + data['numbers'][1]
    await sio.emit('sum_result' , {'result' : result} , to = sid)