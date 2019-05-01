from pyModbusTCP.client import ModbusClient

# TCP auto connect on first modbus request
c = ModbusClient()
c.host("192.168.0.102")
c.port(502)
c.open()


c.write_single_coil(0,0) # relay0
c.write_single_coil(1,0) # relay1
c.write_single_coil(2,1) # relay2

bits = c.read_coils(0, 3)
        # if success display registers
if bits:
    print("bit ad #0 to 9: "+str(bits))