# CS361-Microservice

Welcome to the ReadMe for the CS361 Staple Card Microservice!

This microservice creates a continuous server listening for TCP connections from client programs on the localhost IP address, 127.0.0.1, and port 54345. The port number is so high in order to avoid doubling ports with another process.

This microservice receives a string of letters from the set “cwubrg”, with spaces between each letter, from the client process. The form being: “letter space letter space… etc”. One example would be “c w u”, another is “u b r”.

In order for the microservice to correctly interpret the sent string, the order of the letters has to be “c w u b r g”. Any of the letters may be left out, none are required, but the ordering “c w u b r g” is required. One example with correct ordering with removed letters would be: “c w b g”, another would be “u r”, a third, “w b g”.

The microservice will send a string back to the client process in the form: “Staples:\n\nColor:\nStaple Card\nStaple Card\nStaple Card\n\nColor:\n…”. When printed, this is the format:
	Staples:

	Color:
	Staple Card
	Staple Card
	Staple Card

	Color:
	...

An example of part of a correctly created call to this program in the Python programming language would look like:

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	address = "127.0.0.1"
	client_socket.connect((address, 54345))
	message = “c w u b r g”
	client_socket.sendall(message.encode())

Receiving data from the program is as easy as having the calling client process receive data from the microservice. An example in the Python programming language is:

	response = client_socket.recv(4096)
	print(f"{response.decode()}\n")
	client_socket.close()

Any programming language which can create a TCP connection through sockets can be used to communicate with this microservice.

The UML sequence diagram for this microservice:
!(https://github.com/jacobsmith95/CS361-Microservice/blob/main/Microservice%20UML.PNG)
