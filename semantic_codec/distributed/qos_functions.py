import struct

import zmq


class MockQoSFunction(object):

    def __init__(self):
        self.probability = 0.1

        self._counter = 0

    def run(self, new_instruction, address):
        if self._counter == 2:
            self._counter = 0
            return True
        else:
            self._counter += 1
            return False

class DistributedQoS(object):

    def __init__(self, ip, program_name):
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REQ)
        self._socket.connect(ip)

    def run(self, new_instruction, address):
        self._socket.send_json(struct.pack('@L@L', new_instruction, address))



