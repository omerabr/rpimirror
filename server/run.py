#!/usr/bin/env python

import linecache
from yowsup.stacks import YowStack
from layer import EchoLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.auth                        import YowCryptLayer, YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.protocol_media              import YowMediaProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.layers.logger                      import YowLoggerLayer
from yowsup.layers.axolotl                     import YowAxolotlLayer
from yowsup.layers.protocol_iq                 import YowIqProtocolLayer
from yowsup.layers.protocol_calls              import YowCallsProtocolLayer
from yowsup.common import YowConstants
from yowsup import env

PASS = linecache.getline('/home/pi/yowsup/config', 4).split("=")[1]+"="
PHONE = linecache.getline('/home/pi/yowsup/config', 3).split("=")[1].split("\n")[0]

CREDENTIALS = (PHONE, PASS) # replace with your phone and password

if __name__==  "__main__":
	env.CURRENT_ENV = env.S40YowsupEnv()
	layers = (
			EchoLayer,
			(YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer, YowMediaProtocolLayer, YowIqProtocolLayer, YowCallsProtocolLayer),
			YowLoggerLayer,
			YowCoderLayer,
			YowCryptLayer,
			YowStanzaRegulator,
			YowNetworkLayer
		)

        stack = YowStack(layers)
        stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)
        stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])
        stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
        stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())
        
        stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            stack.loop()
        except AuthError as e:
            print("Authentication Error: %s" % e.message)

	

#~ import linecache
#~ from layer import EchoLayer
#~ from yowsup.layers.auth                        import YowAuthenticationProtocolLayer
#~ from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
#~ from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
#~ from yowsup.layers.protocol_acks               import YowAckProtocolLayer
#~ from yowsup.layers.network                     import YowNetworkLayer
#~ from yowsup.layers.coder                       import YowCoderLayer
#~ from yowsup.stacks import YowStack
#~ from yowsup.common import YowConstants
#~ from yowsup.layers import YowLayerEvent
#~ from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS
#~ from yowsup import env
#~ 
#~ PASS = linecache.getline('/home/pi/yowsup/config', 4).split("=")[1]+"="
#~ PHONE = linecache.getline('/home/pi/yowsup/config', 3).split("=")[1].split("\n")[0]
#~ 
#~ CREDENTIALS = (PHONE, PASS) # replace with your phone and password
#~ 
#~ if __name__==  "__main__":
    #~ layers = (
        #~ EchoLayer,
        #~ (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer)
    #~ ) + YOWSUP_CORE_LAYERS
#~ 
    #~ stack = YowStack(layers)
    #~ stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)         #setting credentials
    #~ stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])    #whatsapp server address
    #~ stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)              
    #~ stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())          #info about us as WhatsApp client
#~ 
    #~ stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
#~ 
    #~ stack.loop() #this is the program mainloop
