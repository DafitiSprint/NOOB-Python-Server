import tornado.websocket

clients = {}

class WebSocketHandler(tornado.websocket.WebSocketHandler):


    @staticmethod
    def broadcast(message, device_type=None):
        
        if device_type is None:
            for client in clients:
                clients[client]["object"].write_message(message);
        else:
            for client in clients:
                if clients[client]["type"] == device_type:
                    clients[client]["object"].write_message(message);



    def open(self, *args):
        self.id = self.get_argument("id", (len(clients) + 1))
        device_type = self.get_argument("type", "default")

        print "'%s' device has connected with id: %s" % (device_type, self.id)

        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "type": device_type, "object": self}


    def on_message(self, message):
        """
        when we receive some message we want some message handler..
        for this example i will just print message to console
        """
        print "Client %s received a message : %s" % (self.id, message)


    def on_close(self):
        if self.id in clients:
            del clients[self.id]


    def check_origin(self, origin):
        return True