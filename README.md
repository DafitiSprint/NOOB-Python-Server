NOOB - Python Server
====

By default the server is started at port 80
You can change the port on the server start as follow

```sh
python NOOB.py --port=8765
```

This is a Web and WebSocket server.
To connect a WebSocket client to this server, you must connect to / and optionally inform the parameters 'type' and 'id' so the server will know
wich kind o message this client accepts:

```sh
192.168.0.1:8765/?id=123&type=siren
```

So far there are only two types:
- siren
- user-browser

The webserver has two actions in place:
#### /alert/siteDown
    This is used to tell every connected client that the site is down
    it accepts "time" param, so the clients know how long should be the duration of the notification

#### /alert/message
    This is used to send a message to the clients who can show it
    it accepts "text" and "color" params.
    "text" is displayed
    "color" can be "red", "yellow" or "green", and the client should know what to do with it
