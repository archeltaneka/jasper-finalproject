from socketIO_client import SocketIO, LoggingNamespace, BaseNamespace

class ConnectionSpace(BaseNamespace):
    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

class LightOnSpace(BaseNamespace):
    def handle(self, *args):
        print('Light On', args)
        # LIGHT ON

class LightOffSpace(BaseNamespace):
    def handle(self, *args):
        print('Light Off', args)
        # LIGHT OFF

socketIO = SocketIO('', 8000, ConnectionSpace)

# Define namespaces
lighton_namespace = socketIO.define(LightOnSpace, '/lighton')
lightoff_namespace = socketIO.define(LightOffSpace, '/lightoff')

# Emit events
lighton_namespace.emit('Light on!')
lightoff_namespace.emit('Light off!')
socketIO.wait()

# Listen for events
socketIO.on('Light on!', LightOnSpace)
socketIO.wait()
        
