import tornado.web
from tornado.escape import json_encode, json_decode
from dispatcher import MethodDispatcher
from websocket import WebSocketHandler

response = {}

class AlertHandler(MethodDispatcher):

    @tornado.web.asynchronous
    def siteDown(self, *args, **kwargs):
        response["status"] = 'sent'
        response["sent_to"] = {}

        self._siren('500','6')
        self._userBrowser("Site is down!", "yellow")


        self.write(json_encode(response))
        self.finish()

    @tornado.web.asynchronous
    def newrelic(self, alert="", deployment=""):
        response["status"] = 'sent'
    	response["sent_to"] = {}
    	
    	
    	self._siren()
    	if deployment != "":
    		self._userBrowser('deployment done, pay attention','yellow')

    	if alert != "":
    		alert = json_decode(alert)
    		self._userBrowser(alert['message'],'red')

    	print alert

        self.finish()	


    @tornado.web.asynchronous
    def message(self, text, color="red", *args, **kwargs):
        response["status"] = 'sent'
        response["sent_to"] = {}

        self._userBrowser(text, color)

        self.write(json_encode(response))
        self.finish()



    def _siren(self, time='1000', repeat='1'):
        WebSocketHandler.broadcast(time+'-'+repeat, 'siren')
        response["sent_to"]["siren"] = str(time)


    def _userBrowser(self, text, color="red"):
        finalMessage = {
            'text': text,
            'color': color
        }
        WebSocketHandler.broadcast(json_encode(finalMessage), 'user-browser')
        response["sent_to"]["userBrowser"] = text+" "+color


    def _default(self):
        response["sent_to"]["default"] = True
