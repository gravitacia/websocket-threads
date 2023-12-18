import sys
import threading
import time
import websocket


def on_message(ws, message):
    print(f"Received message: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print(f"Closed with status code {close_status_code}: {close_msg}")


def on_open(ws):
    def run(*args):
        for i in range(5):
            message = f"Hello from Thread {threading.current_thread().name} - {i}"
            ws.send(message)
            time.sleep(1)
        ws.close()

    threading.Thread(target=run).start()


def test_websocket_connection(num_threads):
    websocket.enableTrace(True)

    for _ in range(num_threads):
        ws_url = "url"
        ws = websocket.WebSocketApp(ws_url,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws_thread = threading.Thread(target=ws.run_forever)
        ws_thread.start()

    for ws_thread in threading.enumerate():
        if ws_thread != threading.current_thread():
            ws_thread.join()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <num_threads>")
        sys.exit(1)

    num_threads = int(sys.argv[1])
