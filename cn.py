import streamlit as st

tcp_server_code = """
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

class ServerSocketExample {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(3333);
        
        Socket socket = serverSocket.accept();
        
        DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
        
        dataOutputStream.writeUTF("Hello client!");
        dataOutputStream.close();
        socket.close();
        serverSocket.close();
    }
}
"""

tcp_client_code = """
import java.io.DataInputStream;
import java.io.IOException;
import java.net.Socket;

class SocketExample{
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost",3333);
        
        DataInputStream datainputstream = new DataInputStream(socket.getInputStream());
        String msg = datainputstream.readUTF();
        System.out.println("Server says:" +msg);
    }
}
"""

udp_server_code = """
import java.net.*;

class DatagramServer{
    public static void main(String[] args) throws Exception {
        DatagramSocket datagramSocket = new DatagramSocket();
        
        String msg = "Hi Client !";
        InetAddress ip = InetAddress.getByName("localhost");
        
        DatagramPacket datagramPacket = new DatagramPacket(msg.getBytes(),msg.length(),ip,3333);
        
        datagramSocket.send(datagramPacket);
        datagramSocket.close();
    }
}
"""

udp_client_code = """
import java.net.*;

class Datagramclient {
    public static void main(String[] args) throws Exception {
         DatagramSocket datagramSocket = new DatagramSocket(3333);
         
         byte[] buffer = new byte[1024];
         
         DatagramPacket datagramPacket = new DatagramPacket(buffer,1024);
         datagramSocket.receive(datagramPacket);
         
         String msg = new String(datagramPacket.getData());
         System.out.println(msg);
         
         datagramSocket.close();
    }
}
"""

st.title("Socket Programming Examples")

st.header("TCP Server")
st.code(tcp_server_code, language='java')

st.header("TCP Client")
st.code(tcp_client_code, language='java')

st.header("UDP Server")
st.code(udp_server_code, language='java')

st.header("UDP Client")
st.code(udp_client_code, language='java')
