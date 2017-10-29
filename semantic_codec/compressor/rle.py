import os
import random

from semantic_codec.architecture.disassembler_readers import ElfioTextDisassembleReader
from semantic_codec.distributed.qos_functions import DistributedQoS

_qos = DistributedQoS("10.0.0.83:5555", 'basic_math')

ARM_SIMPLE = os.path.join(os.path.dirname(__file__), 'tests/data/basicmath_small.disam')
program = ElfioTextDisassembleReader(ARM_SIMPLE).read_instructions()

#converts the text into a list of characters
#RLE
final = "" #string of encoded text
last_char = program[0]
counter = 0 #keeps track of i's location
first_of_a_kind = 0 #keeps track of the location of where the set started
for i in program:
    if i != last_char: #if a different character was found
        final += str(counter - first_of_a_kind) + last_char
        first_of_a_kind = counter
    counter += 1
    last_char = i

final_s = list(final) #Replacements begin
counter = 0 #keeps track of how many times a set of characters has been replaced (to skip the characters that have been replaced already)
final_result = ""
for i in range(0, (len(final_s) - 1)):
    if i%2 == 0: #makes sure that i is an even number (this means that an integer value will be found in the list)
        if counter == 0:
            try:
                number = int(final_s[i])
                if int(final_s[i]) > int(final_s[(i + 2)]): #If the set of characters is bigger than the one that comes next:
                    qos_result = _qos.run(final_s[i], final_s[i].address) #get a random True or False
                    while qos_result:
                        counter += 1 #counts how many sets of characters have been replaced
                        index = (i + (2 * counter))
                        number += int(final_s[index]) #adds the number of characters to the bigger set
                        qos_result = _qos.run(number, final_s[index].address) #makes another random choice to decide if the next set of characters should also be replaced
                final_result += str(number) + final_s[(i + 1)] #adds the final result to the final string
            except:
                final_result += str(number) + final_s[(i + 1)]

        else:
            counter -= 1
print(final_result) #prints the final result