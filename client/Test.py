import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)
    ws.send("hi from client!")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")
    


def on_open(ws):
    def run(*args):
        ws.send("Hello")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8765",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()