from pyModbusTCP.client import ModbusClient


class ZSALxxVxx:

    def __init__(self):
        self.modbus = ModbusClient()
        self.modbus_ip = "192.168.2.7"
        self.modbus_port = 8234
        self.modbus_timeout = 10
        self.auto_update_time = 0
        self.baud_rate = 38400
        self.device_id = 1
        self.precision = 3
        self.no_channel = 16
        self.channel_volts = []

    def zsalxxvxx_connect(self):
        try:
            self.modbus = ModbusClient(host=self.modbus_ip,
                                       port=self.modbus_port,
                                       timeout=self.modbus_timeout)
        except SystemError:
            print('Connect Error')
            return

    def zsalxxvxx_get_info(self):
        regs = self.modbus.read_holding_registers(0x31, 1)
        self.auto_update_time = regs if regs else None
        regs = self.modbus.read_holding_registers(0x32, 1)
        self.device_id = regs if regs else None
        regs = self.modbus.read_holding_registers(0x33, 1)
        self.baud_rate = regs if regs else None
        regs = self.modbus.read_holding_registers(0x3A, 1)
        self.precision = regs if regs else None

    def channel_acquisition(self):
        tmp = []
        for i in range(16):
            raw = self.modbus.read_holding_registers(i, 1)
            raw = raw[0] if raw else 0
            precs = int(raw / 10000)
            volt = (raw - precs * 10000) / (10 ** precs)
            tmp.append(volt)
        self.channel_volts = tmp

    def zsalxxvxx_close(self):
        self.modbus.close()
