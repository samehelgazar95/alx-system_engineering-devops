### SSH

## Overview

- **What is SSH:** SSH stands for Secure Shell, and it's a common and secure way to connect and log in to remote linux server.
  <br/>
- **Shell Session:** When ever you connect to SSH, a shell session is created, and u can interact with the server using the terminal.
  <br/>
- **Shell Tunnel:** And through the session lifetime, any command you type will be sent to the server through a shell encrypted tunnel and executed there (in the server).
  <br/>
- **SSH Connection**: the SSH connection is implemented using a client-server model,
  - which means that the server must have a piece of software called **server-daemon** which is responsible for listening for the connection through a specific port, authenticates the connection request and create the appropriate environment if the client's credentials are correct.
  - and the client's machine must have an **SSH client**, that knows how to communicate using SSH protocol and it's responsible for sending client's data to request for a connection.
    <br/>
-
