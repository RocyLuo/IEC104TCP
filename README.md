# IEC104TCP
IEC104 client and server simulator

So far, the IEC104 simulator can only support certain client to server side protocol based on IEC 60870-5-104. The supported frames are u frame, s frame and i frame in which asud types are 45,46,47,48,49,50,51,58,59,60,61,62,63,64,101 and 103. 

The way to build IEC104 packets is shown in the iec104_tcp_packets.py file. The packet structure is build based on SCAPY. So, make sure your machine has SCAPY installed. Also, there is an example to show how to use the iec104client to send some IEC104 packets. 

In term of the Server side, it is coded in the EchoIEC104Server.py. As its name suggests, this is not a real IEC104 server implemented according to IEC 60870-5-104. This is just an echo server which sends what it receives back to clients. 

The simulator can be used to simulate some IEC104 traffic, which is quiet useful to test network equipment such as Industrial Firewall.
