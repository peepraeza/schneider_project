from pyModbusTCP.client import ModbusClient
import time
# TCP auto connect on first modbus request
c = ModbusClient()
c.host("192.168.0.112")
c.port(502)
c.open()

_15minutes = 10*60

# c.write_single_coil(0,0) # relay0
# c.write_single_coil(1,0) # relay1
# c.write_single_coil(2,0) # relay2

#off all
print("0")
	
c.write_single_coil(1,1) # relay1
c.write_single_coil(2,1) # relay2
time.sleep(60)

# # 001
# print("1")
# c.write_single_coil(0,0) # relay0
# c.write_single_coil(1,0) # relay1
# c.write_single_coil(2,1) # relay2
# time.sleep(_15minutes)

# # 010
# print("2")
# c.write_single_coil(0,0) # relay0
# c.write_single_coil(1,1) # relay1
# c.write_single_coil(2,0) # relay2
# time.sleep(_15minutes)

# # 011
# print("3")
# c.write_single_coil(0,0) # relay0
# c.write_single_coil(1,1) # relay1
# c.write_single_coil(2,1) # relay2
# time.sleep(_15minutes)

# # 100
# print("4")
# c.write_single_coil(0,1) # relay0
# c.write_single_coil(1,0) # relay1
# c.write_single_coil(2,0) # relay2
# time.sleep(_15minutes)

# # 101
# print("5")
# c.write_single_coil(0,1) # relay0
# c.write_single_coil(1,0) # relay1
# c.write_single_coil(2,1) # relay2
# time.sleep(_15minutes)

# # 110
# print("6")
# c.write_single_coil(0,1) # relay0
# c.write_single_coil(1,1) # relay1
# c.write_single_coil(2,0) # relay2
# time.sleep(_15minutes)

# # 111
# print("7")
# c.write_single_coil(0,1) # relay0
# c.write_single_coil(1,1) # relay1
# c.write_single_coil(2,1) # relay2
# time.sleep(_15minutes)

# print("finish")
# c.write_single_coil(0,0) # relay0
# c.write_single_coil(1,0) # relay1
# c.write_single_coil(2,0) # relay2

        # if success display registers
# if bits:
#     print("bit ad #0 to 9: "+str(bits))