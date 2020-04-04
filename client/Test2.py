import websocket
import threading
import sys
from PySide2.QtCore import *

sys.path.append(
    'C:\\Users\\Lenovo\\Documents\\SE\\Year2S2\\SEP\\Project\\Bello\\UI_pages')

from BelloUI import *


class WebSocketClient:
    def __init__(self):
        self.ws =  websocket.WebSocket()
        self.ws.connect("ws://localhost:8765")
        self.ws.send("hi")
        t = threading.Thread(target=self.receive, args=[])
        t.start()
        
    
    def sendHello(self):
        self.ws.send("Hello, Server")
        
    def receive(self):
        while True:
            message = self.ws.recv()
            print(message)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    
    ui = BelloUI(None, WebSocketClient())
    
    sys.exit(application.exec_())
