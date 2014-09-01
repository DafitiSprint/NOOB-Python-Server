import tornado.web
from tornado.escape import json_encode
from dispatcher import MethodDispatcher
from websocket import WebSocketHandler

response = {}

class AlertHandler(MethodDispatcher):

    @tornado.web.asynchronous
    def siteDown(self, time=1000):

        response["status"] = 'sent'
        response["sent_to"] = {}

        self._siren(time)
        self._userBrowser("Site is down!", "yellow")


        self.write(json_encode(response))
        self.finish()


    @tornado.web.asynchronous
    def message(self, text, color="red"):
        response["status"] = 'sent'
        response["sent_to"] = {}

        self._userBrowser(text, color)

        self.write(json_encode(response))
        self.finish()



    def _siren(self, time):
        WebSocketHandler.broadcast(self.get_argument("time", time), 'siren')
        response["sent_to"]["siren"] = time


    def _userBrowser(self, text, color="red"):
        finalMessage = {
            'text': text,
            'color': color
        }
        WebSocketHandler.broadcast(json_encode(finalMessage), 'user-browser')
        response["sent_to"]["userBrowser"] = text+" "+color


    def _default(self):
        response["sent_to"]["default"] = True