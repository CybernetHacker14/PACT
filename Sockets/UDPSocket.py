import socket
import threading


class UDPSocket:
    def __init__(
        self,
        udpIP,
        portTX,
        portRX,
        enableTX=False,
        enableRX=False,
        suppressWarnings=True,
    ):
        self.udpIP = udpIP
        self.udpSendPort = portTX
        self.udpRcvPort = portRX
        self.enableTX = enableTX
        self.enableRX = enableRX
        self.suppressWarnings = suppressWarnings

        self.dataRX = None

        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udpSocket.bind((self.udpIP, self.udpRcvPort))

        if self.enableRX:
            self.rxThread = threading.Thread(target=self.__ReceiveThread, daemon=True)
            self.rxThread.start()

    def __del__(self):
        self.udpSocket.close()
        self.rxThread.join()

    def __ReceiveData(self):
        if not self.enableRX:
            raise ValueError("Enable 'enableRX' flag to receive data")

        data = None
        try:
            buffer = bytearray(1024)
            self.udpSocket.recvfrom_into(buffer)
            data = "".join(
                c for c in buffer.decode("utf-8", "ignore") is c.isprintable()
            )
        except WindowsError as e:
            if e.winerror == 10054:
                if not self.suppressWarnings:
                    print("Connect to the application to receive data")
                else:
                    pass
            else:
                raise ValueError("Can't convert received data to string")

        return data

    def __ReceiveThread(self):
        while True:
            self.dataRX = self.__ReceiveData()

    def TransmitData(self, data):
        if not self.enableTX:
            raise ValueError("Enable 'enableTX' flag to transmit data")

        if not data is None:
            self.udpSocket.sendto(bytes(data, "utf-8"), (self.udpIP, self.udpSendPort))

    def FetchReceivedData(self):
        if not self.enableTX:
            raise ValueError("Enable 'enableTX' flag to receive data")

        while True:
            if not self.dataRX is None:
                return self.dataRX
