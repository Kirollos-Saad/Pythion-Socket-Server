import socketserver
import string

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            self.data = self.request.recv(1024).strip()
            message = self.data.decode('utf-8')
            operation = message[0]
            text = message[1:]

            if not text:
                response = "The message is empty"
                self.request.sendall(response.encode('utf-8'))
                return

            if operation == 'W':
                response = f"The number of words is {len(text.split())}"
            elif operation == 'L':
                response = f"The number of lowercase letters is {len([c for c in text if c in string.ascii_lowercase])}"
            elif operation == 'U':
                response = f"The number of uppercase letters is {len([c for c in text if c in string.ascii_uppercase])}"
            elif operation == 'R':
                response = f"The number of numeric characters is {len([c for c in text if c.isdigit()])}"
            elif operation == 'T':
                response = f"The total number of characters is {len(text)}"
            else:
                response = message

            self.request.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"An error occurred: {e}")
            response = "An error occurred while processing your request."
            self.request.sendall(response.encode('utf-8'))

def main():
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print("Server started at {}:{}".format(HOST, PORT))
    server.serve_forever()

if __name__ == "__main__":
    main()