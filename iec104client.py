from iec104lib import *
from struct import *
class iec104_tcp_client():
	Tx=0
	Rx=0
	_targetip=''
	_port=2404
	_socket=''

	def __init__(self,targetip):
		self._targetip=targetip

	def connect(self):
		self._socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		self._socket.settimeout(0.5)
		l_onoff=1          
	    	l_linger = 0	
		self._socket.setsockopt(socket.SOL_SOCKET,socket.SO_LINGER,struct.pack('ii', l_onoff, l_linger))
		self._socket.connect((self._targetip,self._port))

	def quit(self):
		self._socket.close()

	def IOA2LE(self,IOA):
		first=IOA&255
		second=(IOA>>8)&255
		third=(IOA>>16)&255
		res=(first<<16)+(second<<8)+third
		return res
	
	def setRx(self):
		self.Rx=self.Rx+1
		if self.Rx > 65534:
			self.Rx = 1

	def getTx(self):
		self.Tx = self.Tx + 1
		if self.Tx > 65534:
			self.Tx = 1
		return self.Tx

	def buildinfobj45(self,Infobj):
		infobj=asdu_infobj_45()
		infobj.IOA=self.IOA2LE(Infobj[0])
		infobj.SCO=Infobj[1]
		return infobj

	def buildinfobj46(self,Infobj):
		infobj=asdu_infobj_46()
		infobj.IOA=self.IOA2LE(Infobj[0])
		infobj.DCO=Infobj[1]
		#print Infobj[1]
		return infobj

	def buildinfobj47(self,Infobj):
		infobj=asdu_infobj_47()
		infobj.IOA=self.IOA2LE(Infobj[0])
		infobj.RCO=Infobj[1]
		return infobj

	def buildinfobj48(self,Infobj):
		infobj=asdu_infobj_48()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('h',Infobj[1]) 
		infobj.Value=value
		infobj.QOS=Infobj[2]
		return infobj

	def buildinfobj49(self,Infobj):
		infobj=asdu_infobj_49()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('h',Infobj[1]) 
		infobj.Value=value
		infobj.QOS=Infobj[2]
		return infobj

	def buildinfobj50(self,Infobj):
		infobj=asdu_infobj_50()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('f',Infobj[1]) 
		infobj.Value=value
		infobj.QOS=Infobj[2]
		return infobj

	def buildinfobj51(self,Infobj):
		infobj=asdu_infobj_51()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('I',Infobj[1]) 
		LEvalue=value[0]+value[1]
		LEvalue=LEvalue+value[2]
		LEvalue=LEvalue+value[3]
		infobj.Value=LEvalue
		return infobj

	def buildinfobj58(self,Infobj):
		infobj=asdu_infobj_58()
		infobj.IOA=self.IOA2LE(Infobj[0])
		infobj.SCO=Infobj[1]
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildinfobj59(self,Infobj):
		infobj=asdu_infobj_59()
		infobj.IOA=self.IOA2LE(Infobj[0])
		infobj.DCO=Infobj[1]
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildinfobj60(self,Infobj):
		infobj=asdu_infobj_60()
		infobj.IOA=self.IOA2LE(Infobj[0])
		infobj.RCO=Infobj[1]
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildinfobj61(self,Infobj):
		infobj=asdu_infobj_61()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('h',Infobj[1]) 
		infobj.Value=value
		infobj.QOS=Infobj[2]
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildinfobj62(self,Infobj):
		infobj=asdu_infobj_62()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('h',Infobj[1]) 
		infobj.Value=value
		infobj.QOS=Infobj[2]
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildinfobj63(self,Infobj):
		infobj=asdu_infobj_63()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('f',Infobj[1]) 
		infobj.Value=value
		infobj.QOS=Infobj[2]
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildinfobj64(self,Infobj):
		infobj=asdu_infobj_64()
		infobj.IOA=self.IOA2LE(Infobj[0])
		value=struct.pack('I',Infobj[1]) 
		LEvalue=value[0]+value[1]
		LEvalue=LEvalue+value[2]
		LEvalue=LEvalue+value[3]
		infobj.Value=LEvalue
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildinfobj101(self,Infobj):
		infobj=asdu_infobj_101()
		infobj.IOA=self.IOA2LE(Infobj[0])
		infobj.Operation=Infobj[1]
		return infobj

	def buildinfobj103(self,Infobj):
		infobj=asdu_infobj_103()
		infobj.IOA=self.IOA2LE(Infobj[0])
		CPtime=CP56Time()
		infobj.CP56Time=CPtime
		return infobj

	def buildpacket(self,p):
		start=p[0]
		ApduLen=p[1]
		frame_type=p[2]

		if(frame_type=='sf'):
			sframe=s_frame()
			if(start!='START'):
				sframe.START=start
			if(ApduLen!='auto'):
				sframe.ApduLen=ApduLen
			sframe.Rx=self.Rx<<1
			return sframe

		elif(frame_type=='uf'):
			uf_type=p[3]
			uframe=u_frame()

			if(start!='START'):
				uframe.START=start
			if(ApduLen!='auto'):
				uframe.ApduLen=ApduLen
			uframe.Type=uf_type
			return uframe

		elif(frame_type=='short_if'):
			iframe=i_frame()
			if(start!='START'):
				iframe.START=start
			if(ApduLen!='auto'):
				iframe.ApduLen=ApduLen
			iframe.Tx=self.getTx()<<1
			iframe.Rx=self.Rx<<1
			return iframe

		elif(frame_type=='if'):
			#build I frame
			iframe=i_frame()
			if(start!='START'):
				iframe.START=start
			if(ApduLen!='auto'):
				iframe.ApduLen=ApduLen
			iframe.Tx=self.getTx()<<1
			iframe.Rx=self.Rx<<1
			
			#build asdu head
			if_asdu=p[3]
			TypeID=if_asdu[0]
			SQ=if_asdu[1]
			Cause=if_asdu[2]
			OA=if_asdu[3]
			Addr=if_asdu[4]
			asduhead=asdu_head()
			asduhead.TypeID=TypeID
			asduhead.SQ=SQ
			asduhead.Cause=Cause
			asduhead.OA=OA
			asduhead.Addr=Addr

			#build asdu Infobj
			Infobj=if_asdu[5]
			if(TypeID==45):
				asdubody=self.buildinfobj45(Infobj)
			elif(TypeID==46):
				asdubody=self.buildinfobj46(Infobj)
			elif(TypeID==47):
				asdubody=self.buildinfobj47(Infobj)
			elif(TypeID==48):
				asdubody=self.buildinfobj48(Infobj)
			elif(TypeID==49):
				asdubody=self.buildinfobj49(Infobj)
			elif(TypeID==50):
				asdubody=self.buildinfobj50(Infobj)
			elif(TypeID==51):
				asdubody=self.buildinfobj51(Infobj)
			elif(TypeID==58):
				asdubody=self.buildinfobj58(Infobj)
			elif(TypeID==59):
				asdubody=self.buildinfobj59(Infobj)
			elif(TypeID==60):
				asdubody=self.buildinfobj60(Infobj)
			elif(TypeID==61):
				asdubody=self.buildinfobj61(Infobj)
			elif(TypeID==62):
				asdubody=self.buildinfobj62(Infobj)
			elif(TypeID==63):
				asdubody=self.buildinfobj63(Infobj)
			elif(TypeID==64):
				asdubody=self.buildinfobj64(Infobj)
			elif(TypeID==101):
				asdubody=self.buildinfobj101(Infobj)
			elif(TypeID==103):
				asdubody=self.buildinfobj103(Infobj)

			else:
				print 'ASDU_TypeID is not supported' 

			#print hexdump(iframe/asduhead/asdubody)
			return iframe/asduhead/asdubody

		else:
			print 'wrong apci type'

	def sendOne(self,p):
		self.connect()
		iec104=self.buildpacket(p)
		self._socket.send(str(iec104))
		time.sleep(0.015)
		try:
			output=self._socket.recv(1024)
		except Exception,e:
			if (str(e).find('[Errno 104]')!=-1):
				#self._socket.close()
				return 'RST'
			else:
				#self._socket.close()
				return 'Drop'
		self._socket.close()
		self.setRx()
		return 'Accept'
