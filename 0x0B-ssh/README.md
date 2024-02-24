# SSH

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
- **How it works?**: First the client generates rsa keys (public and private), they will be created in the ~/.ssh dir called by default id_rsa.pub and id_rsa, then you have to share the public key in the server, copy it in a file called ~/.ssh/authorized_keys in the server (!DON'T SHARE THE PRIVATE KEY, NEVER), the server and the client will use the public key to encrypt and decrypt the messages sent between them.
  <br/>
- BTW RSA is the default key type, there are also DSA, and ECDSA
  <br/>
  <br/>

## Generating SSH Keys

```bash
ssh-keygen
```

- This command line is to generate a rsa keys, you can change the default dir if you want which is (~/.ssh), and you can set passphrase or leave it blank (Note that you will need this passphrase every time you use the private key)

  <br/>

```bash
ssh-keygen -b 4096
```

- SSH keys are 2048 bits by default, but u can change it by using -b arg with the needed bits numbers
  <br/>

```bash
ssh-keygen -p
```

- To change the passphrase of the key, you can use this arg -p
  <br/>

```bash
ssh-keygen -l
```

- To show the fingerprint of the key, you can use the arg -l
- the fingerprint contains the bit-length, the account, the host and the algo used

<br/>

```bash
ssh-copy-id username@remote_host
cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

- there are 3 ways to copy the public key to the server, you can do it locally using one of the previous commands, or manually coping it to the server to path (~/.ssh/authorized_keys)

<br/>

## Basic Connection Instructions

- How to connecting to the remote servers:
  ```bash
  $ ssh remote_host_ip
  $ ssh user_name@remote_host_ip
  $ ssh user_name@remote_host_ip command_to_run_on_the_fly
  $ ssh -p port_num user_name@remote_host_ip
  ```
  - Choose one way to make the connection:
    - First way assumes that your local username is the same server username.
    - Second using the username and the server host ip.
    - Third is creating a connection to run a command line in the server on the fly, without needing to create a session.
    - Fourth it you wanna use a specific port

## Server-Side Configuration Options

- ### To change any configurations related in the server, First open or create this file:

  ```bash
    sudo nano /etc/ssh/ssh_config
  ```

- **Disabling Password Authentication**
  - If your SSH keys works so fine (configured, tested and working properly) and you don't want to use password to connect to the server anymore, you can disable connecting to the server using password using this command in the server:
    - Append >> PasswordAuthentication no
- **Changing the Port that the SSH Daemon Runs On**

  - If you wanna change the port that SSH runs on:
    - Append >> Port $PORT_NUMBER

- **Limiting the Users Who can Connect Through SSH**

  - If you specify the allowed users to connect.
    - Append >> AllowUsers user1 user2:
  - Or you can specify it by group:
    - Append >> AllowGroups sshmembers

- **Disabling Root Login**
  - It's recommended to disable root to login to SSH:
    - Append >> PermitRootLogin no
- **Enabling Root to run command on the fly**

  - Append >> PermitRootLogin forced-commands-only
    <br/>

  ```bash
    sudo nano /root/.ssh/authorized_keys
  ```

  - Then Append to authorized_keys >> command="/path/to/command arg1 arg2" ssh-rsa ...

### After any appending must restart the service

```bash
  sudo service ssh restart
```

<br/>

- ## Client-Side Configuration Options:

  - ### To change any configurations related in the client, First open or create this file:

    ```bash
      nano ~/.ssh/config
    ```

    - **Create alias by appending the configs**

      ```ssh
      Host testhost
          HostName your_domain
          Port 4444
          User demo
      ```

      - You can then simply connect with:
        ```bash
          $ ssh testhost
        ```

    - **To prevent the timeout of the session**

      ```ssh
      Host testhost
          ServerAliveInterval  120
      ```
