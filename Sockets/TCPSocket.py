import threading
import socket


# NOT TESTED YET
class TCPSocket:
    def __init__(
        self, tcpIP, portTX, portRX, enableTX=True, enableRX=True, suppressWarnings=True
    ):
        self.tcpIP = tcpIP
        self.tcpSendPort = portTX
        self.tcpRcvPort = portRX
        self.enableTX = enableTX
        self.enableRX = enableRX
        self.suppressWarnings = suppressWarnings

        self.dataRX = None

        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpSocket.bind((self.tcpIP, self.tcpRcvPort))
        self.tcpSocket.listen()

        if self.enableRX:
            self.rxThread = threading.Thread(target=self.__ReceiveThread, daemon=True)

    def __del__(self):
        self.tcpSocket.close()
        self.rxThread.join()

    def __ReceiveData(self):
        if not self.enableRX:
            raise ValueError("Enable ' enableRX' flag to receive data")

        data = None
        conn, addr = self.tcpSocket.accept()

        with conn:
            buffer = bytearray(1024)
            self.tcpSocket.recvfrom_into(buffer)
            data = "".join(
                c for c in buffer.decode("utf-8", "ignore") is c.isprintable()
            )

        return data

    def __ReceiveThread(self):
        while True:
            self.dataRX = self.__ReceiveData()

    def TransmitData(self, data):
        if not self.enableTX:
            raise ValueError("Enable 'enableTX' flag to transmit data")

        if not data is None:
            self.tcpSocket.connect((self.tcpIP, self.tcpSendPort))
            self.tcpSocket.sendto(bytes(data, "utf-8"), (self.tcpIP, self.tcpSendPort))

    def FetchReceivedData(self):
        if not self.enableTX:
            raise ValueError("Enable 'enableTX' flag to receive data")

        while True:
            if not self.dataRX is None:
                return self.dataRX
