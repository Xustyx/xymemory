from ProcessHandler import *
import struct

class DataException(Exception):
    pass

class DataTypes():
    UINT = 'uint'
    INT = 'int'
    BYTE = 'byte'
    STRING = 'string'


class DataManager(object):
    def __init__(self, process_name=None):
        self.process_name = process_name
        self.process = None
        self.is_open = False

        try:
            self.process = ProcessHandler(process_name)
            self.process.open()
            self.is_open = True
        except ProcessException as e:
            print e.message

    def read(self, address, type = 'uint'):
        if not self.is_open:
            raise DataException("Process is not open.")

        if type == DataTypes.BYTE:
            return self.read_byte(address)
        elif type == DataTypes.STRING:
            return self.read_string(address)
        elif type == DataTypes.INT:
            return self.read_int(address)
        elif type == DataTypes.UINT:
            return self.read_uint(address)
        else:
            raise DataException("Invalid data type.")

    def read_byte(self, address):
        return self.process.read_bytes(address,1)

    def read_string(self, address):
        string = ''
        _address = address

        while True:
            byte = self.read_byte(_address)
            if byte == '\x00':
                break

            string += byte
            _address += 0x01

        return string

    def read_uint(self, address):
        return struct.unpack('I',self.process.read_bytes(address,4))[0]

    def read_int(self, address):
        return struct.unpack('i', self.process.read_bytes(address,4))[0]

    def write(self, address, type):
        if not self.is_open:
            raise DataException("Process is not open.")

        if type == DataTypes.BYTE:
            return self.write_byte(address)
        elif type == DataTypes.STRING:
            return self.write_string(address)
        elif type == DataTypes.INT:
            return self.write_int(address)
        elif type == DataTypes.UINT:
            return self.write_uint(address)
        else:
            raise DataException("Invalid data type.")

    def write_byte(self, address):
        pass

    def write_string(self, address):
        pass

    def write_uint(self, address):
        pass

    def write_int(self, address):
        pass
