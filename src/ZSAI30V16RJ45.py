from pyModbusTCP.client import ModbusClient

update_settings = False

c = ModbusClient(host="192.168.2.7", port=8234, timeout=10)

# regs = c.read_holding_registers(0x31, 1)
# print(regs if regs else "rd ERROR")
# regs = c.read_holding_registers(0x32, 1)
# print(regs if regs else "rd ERROR")
# regs = c.read_holding_registers(0x33, 1)
# print(regs if regs else "rd ERROR")
# regs = c.read_holding_registers(0x3A, 1)
# print(regs if regs else "rd ERROR")

if update_settings:
    # update every 0.01s
    c.write_single_register(0x31, 0)
    # use baud rate 115200
    c.write_single_register(0x33, 7)
    # make floating point precision to 3 digits
    c.write_single_register(0x3A, 0)
    c.close()
    exit(0)

regs = c.read_holding_registers(0x31, 1)
print(regs if regs else "rd ERROR")
regs = c.read_holding_registers(0x32, 1)
print(regs if regs else "rd ERROR")
regs = c.read_holding_registers(0x33, 1)
print(regs if regs else "rd ERROR")
regs = c.read_holding_registers(0x3A, 1)
print(regs if regs else "rd ERROR")

while True:
    acq_ar = []
    for i in range(16):
        raw = c.read_holding_registers(i, 1)
        raw = raw[0] if raw else 0
        precs = int(raw / 10000)
        volt = (raw - precs * 10000) / (10 ** precs)
        acq_ar.append(volt)
    print(acq_ar)

c.close()
