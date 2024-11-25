# Mini-Assignment 4
from netmiko import ConnectHandler
import time

# Task 1
router_details = [
    # Router 1
    {
        'host': "192.168.17.129",
        'username': "",
        'password': "",
        "port": 30003
    },
    # Router 2
    {
        'host': "192.168.17.129",
        'username': "",
        'password': "",
        "port": 30004

    },
    # Router 3
    {
        'host': "192.168.17.129",
        'username': "",
        'password': "",
        "port": 30005
    }
]
# 1. In a python loop, create three text files.
for i in range(1,4):
    router = router_details[i - 1]
    filename = f"router_{i}.txt"
    with open(filename, "w") as file:
        # 2. Each router_X.txt file will contain four lines
        file.write(f"Host of router: {router['host']}\n")
        file.write(f"Username: {router['username']}\n")
        file.write(f"Password: {router['password']}\n")
        file.write(f"Port: {router['port']}\n")

# Task 2 : create a file with commands to create and OSPF routing protocol.
# 1. The name of the file should the ospf_routing_protocol.txt
filename = "ospf_routing_protocol.txt"
ospf_lines = [
    "router ospf 1\n",
    "net 0.0.0.0 0.0.0.0 area 0\n",
    "distance 110\n",
    "default-information originate"
]
with open(filename, "w") as file:
    file.writelines(ospf_lines)

# Task 3
# OSPF configurations commands in list
ospf_commands = [
    "router ospf 1",
    "net 0.0.0.0 0.0.0.0 area 0",
    "distance 110",
    "default-information originate"
]

# reading each file for the info
for i in range(1,4):
    router_file = f"router_{i}.txt"
    with open(router_file, "r") as file:
        lines = file.readlines()

    router = {
        "host": lines[0].split(":")[1].strip(),
        "username": lines[1].split(":")[1].strip(),
        "password": lines[2].split(":")[1].strip(),
        "port": int(lines[3].split(":")[1].strip())
    }

# 1. Using a loop and the Netmiko library, connect to EACH router
for router in router_details:
    try:
        connection = ConnectHandler(
            device_type='cisco_ios_telnet',
            host=router['host'],
            username=router['username'],
            password=router['password'],
            secret="cisco1",
            port=router['port']
        )

        # 3. Enter privilege mode
        connection.enable()
        print(f"Connecting to {router['port']}.\n")
        time.sleep(2)

        # 2. While connected to each router, apply the OSPF configuration.
        connection.send_config_set(ospf_commands)
        time.sleep(2)
        print(f"Applying ospf configuration to {router['port']}.\n")

        # Close connection
        connection.disconnect()
        time.sleep(1)
        print(f"Configuration applied to {router['port']}\n")

    except Exception as e:
        print(f"Failed to connect to router {router['port']}", e)
