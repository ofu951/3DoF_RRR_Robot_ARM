# Torku kapatıp pozisyon okuma kodu
import rclpy
from rclpy.node import Node
from dynamixel_sdk import *

class GetOffsets(Node):
    def __init__(self):
        super().__init__('get_offsets')
        self.port_handler = PortHandler('/dev/ttyACM0')
        self.packet_handler = PacketHandler(2.0)
        self.port_handler.openPort()
        self.port_handler.setBaudRate(57600)
        
        for dxl_id in [1, 2, 3]:
            # Torku KAPAT (Serbest hareket için)
            self.packet_handler.write1ByteTxRx(self.port_handler, dxl_id, 64, 0)
            pos, _, _ = self.packet_handler.read4ByteTxRx(self.port_handler, dxl_id, 132)
            print(f"ID {dxl_id} Dik Durum Değeri: {pos}")

def main():
    rclpy.init()
    GetOffsets()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
