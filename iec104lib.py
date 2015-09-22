from scapy.all import *
# IEC104 asdu
class asdu_head(Packet):
	name = "asdu_head"
	fields_desc = [ XByteField("TypeID", 0x45),
			XByteField("SQ", 0x01),
			XByteField("Cause", 0x06),
			XByteField("OA", 0x04),
			LEShortField("Addr", 0x0003)]

class CP56Time(Packet):
	name = "CP56Time"
	#1991-02-19_10:30:1.237
	fields_desc = [ 
			XShortField("Ms", 0xd504),
			XByteField("Min", 0x1e),
			XByteField("Hour", 0xa),
			XByteField("Day", 0x13),
			XByteField("Month", 0x02),
			XByteField("Year", 0x5b),
			]

class asdu_infobj_45(Packet):
	name = "C_SC_NA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			XByteField("SCO", 0x80)]

class asdu_infobj_46(Packet):
	name = "C_DC_NA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			XByteField("DCO", 0x80)]

class asdu_infobj_47(Packet):
	name = "C_RC_NA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			XByteField("RCO", 0x80)]

class asdu_infobj_48(Packet):
	name = "C_SE_NA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="H", remain=0),
			XByteField("QOS", 0x80)]

class asdu_infobj_49(Packet):
	name = "C_SE_NB_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="H", remain=0),
			XByteField("QOS", 0x80)]

class asdu_infobj_50(Packet):
	name = "C_SE_NC_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="f", remain=0),
			XByteField("QOS", 0x80)]

class asdu_infobj_51(Packet):
	name = "C_BO_NA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="I", remain=0)]

class asdu_infobj_58(Packet):
	name = "C_SC_TA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			XByteField("SCO", 0x80),
			PacketField("CP56Time", CP56Time, Packet)]

class asdu_infobj_59(Packet):
	name = "C_DC_TA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			XByteField("DCO", 0x80),
			PacketField("CP56Time", CP56Time, Packet)]

class asdu_infobj_60(Packet):
	name = "C_RC_TA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			XByteField("RCO", 0x80),
			PacketField("CP56Time", CP56Time, Packet)]

class asdu_infobj_61(Packet):
	name = "C_SE_TA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="H", remain=0),
			XByteField("QOS", 0x80),
			PacketField("CP56Time", CP56Time, Packet)]

class asdu_infobj_62(Packet):
	name = "C_SE_TB_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="H", remain=0),
			XByteField("QOS", 0x80),
			PacketField("CP56Time", CP56Time, Packet)]

class asdu_infobj_63(Packet):
	name = "C_SE_TC_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="f", remain=0),
			XByteField("QOS", 0x80),
			PacketField("CP56Time", CP56Time, Packet)]

class asdu_infobj_64(Packet):
	name = "C_BO_TA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x23),
			StrField("Value", '', fmt="I", remain=0),
			PacketField("CP56Time", CP56Time, Packet)]

class asdu_infobj_101(Packet):
	name = "C_CI_NA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x0),
			XByteField("Operation", 0x05)]

class asdu_infobj_103(Packet):
	name = "C_CS_NA_1"
	fields_desc = [ 
			X3BytesField  ("IOA", 0x0),
			PacketField("CP56Time", CP56Time, Packet)]

# IEC104 apci
class i_frame(Packet):
	name = "i_frame"
	fields_desc = [ XByteField("START", 0x68),
			XByteField("ApduLen", None),
			LEShortField("Tx", 0x0000),
			LEShortField("Rx", 0x0000),
			]

	def post_build(self, p, pay):
		if self.ApduLen is None:
			l = len(pay)+4
			p = p[:1] + struct.pack("!B", l) + p[2:]
		return p+pay


class s_frame(Packet):
	name = "s_frame"
	fields_desc = [ XByteField("START", 0x68),
			XByteField("ApduLen", 0x04),
			LEShortField("Type", 0x01),
			LEShortField("Rx", 0x0000)]


class u_frame(Packet):
	name = "u_frame"
	fields_desc = [ XByteField("START", 0x68),
			XByteField("ApduLen", 0x04),
			LEShortField("Type", 0x07),
			LEShortField("Default", 0x0000)]
