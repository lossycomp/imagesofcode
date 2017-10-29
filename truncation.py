import os
from semantic_codec.architecture.disassembler_readers import ElfioTextDisassembleReader
from semantic_codec.distributed.qos_functions import MockQoSFunction

ARM_SIMPLE = os.path.join(os.path.dirname(__file__), 'tests/data/basicmath_small.disam')
program = ElfioTextDisassembleReader(ARM_SIMPLE).read_instructions()

qos = MockQoSFunction()
# qos = DistributedQoSFunction()
for p in program:
    e = p.encoding & 0xFFFFFF00
    qos.run(e, p.address)  # The server will only keep the correct programs
