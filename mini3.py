# Mini-Assignment 3
import paramiko
from datetime import datetime
import time
import os

class SSHClient:
    # Constructor (task 1)
    # Private attributes (task 2)
    def __init__(self, hostname, username, password, port):
        self.__hostname="192.168.17.29"
        self.__username="root"
        self.__password="pnet"
        self.__port=22
        self.__client = None
        self.__shell = None

    def _connect(self):
        try:
            # 1. Connect to an SSH Client using a Paramiko client (3 marks)
            self.__client = paramiko.SSHClient
            self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__client.connect(
                hostname=self.__hostname,
                username=self.__username,
                password=self.__password,
                port=self.__port)
            print("SSH connected.")
        except Exception as e:
            print(f"Failed to connect: {e}")
            self.__client = None


    # 2. Evoking a shell from an SSH Client connection
    def evoke_shell(self):
        if self.__client and self.__client.get_transport() and self.__client.get_transport().is_active():
            self.__shell = self.__client.invoke_shell()
            print("Shell invoked.")
        else:
            print("SSH client not connected!")

    # Public class methods (tasks 3 & 4)
    # 3. Send a command using the Shell (2 marks)
    def shell_command(self, command):
        if self.__client:
            self.__shell.send(command + '\n')
            time.sleep(2)
            output1 = (self.__shell.recv(10000))
            output = output1.decode('utf-8')
            return output
        else:
            print("Shell not invoked.")

    # 4. Send a command-line command using exec_command method (2 marks)
    def exec_command(self, command):
        if self.__client:
            stdin, stdout, stderr = self.__client.exec_command(command)
            time.sleep(2)
            output = stdout.read().decode()
            print(f"Command sent: {command}")

            #save output
            self._save_output(command, output)
        else:
            print("SSH client not connected.")

    # 5. Save either the shell or exec_command output (5 marks)
    def _save_output(self, command, output):
        today = datetime.now()
        day = today.day
        month = today.month
        year = today.year
        hour = today.hour
        minute = today.minute
        saved_file = f"{command}_{day}_{month}_{year}-{hour}_{minute}.txt"
        path = os.path.join(os.path.dirname(__file__), f"{saved_file}")
        with open(path, "w") as file:
            file.write(output)
            print(f"Output saved to {saved_file}.")


    # 6. Closing the connection (1 mark)
    # Destructor (task 6)
    def __del__(self):
        if self.__client:
            self.__client.close()
            print("Closing connection!")

#calling
Test1 = SSHClient("192.168.17.29", "root", "pnet", 22)
Test1.evoke_shell()

