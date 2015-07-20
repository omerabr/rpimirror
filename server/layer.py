from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
import os.path

class EchoLayer(YowInterfaceLayer):
	

	@ProtocolEntityCallback("message")
	def onMessage(self, messageProtocolEntity):

		if messageProtocolEntity.getType() == 'text':
			self.onTextMessage(messageProtocolEntity)
		elif messageProtocolEntity.getType() == 'media':
			self.onMediaMessage	(messageProtocolEntity)

		self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
		self.toLower(messageProtocolEntity.ack())
		self.toLower(messageProtocolEntity.ack(True))


	@ProtocolEntityCallback("receipt")
	def onReceipt(self, entity):
		self.toLower(entity.ack())

	def onTextMessage(self,messageProtocolEntity):
		# just print info
		chatfile = '/var/tmp/yowsup/chat.log'
		sendername = ""
		if messageProtocolEntity.getFrom(False) == "972549950625":
			sendername = "Omer"
		else:
			if messageProtocolEntity.getFrom(False) == "972544725106":
				sendername = "Tzahit"
			else:
				sendername = "Stranger"
		print("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))
		if not os.path.isfile(chatfile):
			newfile=open(chatfile,'w')
			newfile.close()
		writechat=open(chatfile,'a')
		writechat.write(sendername+": "+messageProtocolEntity.getBody()+'\n')
		
	def onMediaMessage(self, messageProtocolEntity):
		# just print info
		if messageProtocolEntity.getMediaType() == "image":
			print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

		elif messageProtocolEntity.getMediaType() == "location":
			print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

		elif messageProtocolEntity.getMediaType() == "vcard":
			print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))

#~ from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
#~ from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
#~ from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
#~ from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
#~ 
#~ 
#~ 
#~ class EchoLayer(YowInterfaceLayer):
#~ 
    #~ @ProtocolEntityCallback("message")
    #~ def onMessage(self, messageProtocolEntity):
        #~ #send receipt otherwise we keep receiving the same message over and over
#~ 
        #~ if True:
            #~ receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
#~ 
            #~ outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                #~ 'Got it!: '+messageProtocolEntity.getBody(),
                #~ to = messageProtocolEntity.getFrom())
            #~ #print messageProtocolEntity.getBody()
            #~ self.toLower(receipt)
            #~ self.toLower(outgoingMessageProtocolEntity)
#~ 
    #~ @ProtocolEntityCallback("receipt")
    #~ def onReceipt(self, entity):
        #~ ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", "delivery", entity.getFrom())
        #~ self.toLower(ack)
