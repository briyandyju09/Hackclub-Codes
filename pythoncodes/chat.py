import socket
import threading
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                console.print(f"[bold green]Client:[/bold green] {message}")
            else:
                break
        except Exception as e:
            console.print(Panel(f"Connection lost: {e}", style="red"))
            break

def send_messages(client_socket):
    while True:
        message = Prompt.ask("You")
        if message.lower() == "exit":
            client_socket.close()
            break
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            console.print(Panel(f"Error sending message: {e}", style="red"))
            break

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    console.print(Panel(f"Server started on {host}:{port}", style="cyan"))
    client_socket, addr = server.accept()
    console.print(Panel(f"Connection from {addr}", style="green"))

    receive_thread = threading.Thread(target=handle_client, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()
    server.close()

def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        console.print(Panel(f"Connected to server {host}:{port}", style="green"))

        receive_thread = threading.Thread(target=handle_client, args=(client,))
        send_thread = threading.Thread(target=send_messages, args=(client,))
        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()
    except Exception as e:
        console.print(Panel(f"Failed to connect: {e}", style="red"))
    finally:
        client.close()

def main():
    console.print(Panel("Real-Time Chat Application", style="bold blue"))
    mode = Prompt.ask("Choose mode: [1] Server, [2] Client", choices=["1", "2"], default="1")
    host = Prompt.ask("Enter host", default="127.0.0.1")
    port = int(Prompt.ask("Enter port", default="12345"))

    if mode == "1":
        start_server(host, port)
    else:
        start_client(host, port)

if __name__ == "__main__":
    main()
