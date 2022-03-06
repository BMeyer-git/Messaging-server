# Overview

This program was written to familiarize myself with how communications can be established between computers in software. Right now it can only handle a server and a single client,
and supports a few commands. To start the server, the server.py file must be run, and then at that point a client can connect by running the client.py file in a separate window
or on another computer. At this point, the client will be welcomed and they can either send messages, or use a few commands (/quit, /time, or /name).

[Software Demo Video](https://youtu.be/nAwYSkl3iAU)

# Network Communication

This program uses a client/server architecture and uses TCP on port 50007. The data is sent back and forth as bytes-like objects and manipulated as strings

# Development Environment

* Visual Studio Code
* Pylance v2022.2.3
* IntelliSense (Pylance) v2022.0.1814523869

* socket module
* datetime module

# Useful Websites

* [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
* [Python Tutorialspoint](https://www.tutorialspoint.com/python/)

# Future Work

* Enable support for multiple clients
* Improve input handling to be more robust for unexpected data
* Add additional features such as sound or graphical interface