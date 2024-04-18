# Python SocketServer: Word and Character Counter

## Overview
This project is a Python-based server that uses the `socketserver` module. It accepts strings from a client, counts the number of words and characters in the string, and performs specific operations based on the first character of the string.

## Features
- Receives client connections and processes strings sent by the client.
- Counts the number of words and characters in the received string.
- Executes operations based on the first character of the string:
  - 'W': Returns the count of words in the string.
  - 'L': Returns the count of lowercase letters in the string.
  - 'U': Returns the count of uppercase letters in the string.
  - 'R': Returns the count of numeric characters in the string.
  - 'T': Returns the total count of characters in the string.
- Handles exceptions and special cases.

## Usage
1. **Starting the Server**: Execute the Python script that contains the server code.
2. **Connecting to the Server**: Use the client script to connect to the server.
3. **Sending Requests**: Send a string to the server. The string should start with one of the specified operations ('W', 'L', 'U', 'R', 'T'), followed by a space and the string to be analyzed.
4. **Receiving Responses**: The server will respond with the requested count or the original message if the operation is invalid.

## Running the Scripts
To run the Server script, use the following command in your terminal:

```bash
py server.py
```
and execute the following command in another terminal or command prompt:
```bash
py server.py
```
then enter your strings( test cases).

## Some Test Cases
- **Test 1**: Input: "Wpython Socket Server". Expected Output: "The number of words is 3"
- **Test 2**: Input: "LpythonSocketServer". Expected Output: "The number of lowercase letters is 16"
- **Test 3**: Input: "UPYTHONSOCKETSERVER". Expected Output: "The number of uppercase letters is 18"
- **Test 4**: Input: "R1234567890". Expected Output: "The number of numeric characters is 10"
- **Test 5**: Input: "TpythonSocketServer123". Expected Output: "The total number of characters is 22"
- **Test 6**: Input: "pythonSocketServer123". Expected Output: "pythonSocketServer123"
