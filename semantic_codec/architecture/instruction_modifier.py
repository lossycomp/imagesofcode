import struct
import sys
from semantic_codec.architecture.bits import Bits
from semantic_codec.architecture.capstone_instruction import CAPSInstruction
from libs.darm import darm



class InstructionModifier(object):
    """
    Modifies parts of an instruction such as its conditional, operand, etc.
    """
    def modify_cond(self, inst, new_cond):
        """
        Modifies an instructions conditional
        :param inst: Instruction to modify
        :param new_cond: New conditional
        :return: The modified instruction
        """
        return Bits.copy_bits(new_cond, inst, 0, 3, 28)

    def modify_opcode(self, inst, new_cond):
        """
        Modifies an instructions conditional
        :param inst: Instruction to modify
        :param new_cond: New conditional
        :return: The modified instruction
        """
        return Bits.copy_bits(new_cond, inst, 0, 3, 21)

    def modify_rn(self, encoding, rn):
        """
        Modifies the Rn register in an instruction
        :param encoding: Instruction to modify
        :param Rn: The new register
        :return: The modified instruction
        """
        return Bits.copy_bits(rn, encoding, 0, 3, 16)

    def modify_rd(self, inst, rd):
        """
        Modifies the Rd register in an instruction
        :param inst: Instruction to modify
        :param Rd: The new register
        :return: The modified instruction
        """
        return Bits.copy_bits(rd, inst, 0, 3, 12)

    def modify_rs(self, inst, rs):
        """
        Modifies the Rd register in an instruction
        :param inst: Instruction to modify
        :param Rd: The new register
        :return: The modified instruction
        """
        return Bits.copy_bits(rs, inst, 0, 3, 8)

    def modify_rm(self, inst, rs):
        """
        Modifies the Rd register in an instruction
        :param inst: Instruction to modify
        :param Rd: The new register
        :return: The modified instruction
        """
        return Bits.copy_bits(rs, inst, 0, 3, 0)

    def modify_immediate(self, inst, immediate):
        """
        Modify the immediate in an instruction
        :param inst: Instruction to modify
        :param inmediate: The new Immediate
        :return:
        """
        if inst & 0xE000000 == 0x4000000:
            return Bits.copy_bits(immediate, inst, 0, 11, 0)
        else:
            return Bits.copy_bits(immediate, inst, 0, 7, 0)

    def get_opcode_parts(self, encoding, conditional):
        return ['c']

    def get_conditional_parts(self, encoding, conditional):
        return ['c']

    def get_registers_parts(self, encoding, register):
        """
        Get in which parts of an instruction is possible to find a given register
        :param encoding: Intruction encoding
        :param register: Register to find
        :return: the parts where the register lives [Rn, Rd, etc...]
        """
        # DARM instructions came handy as they provide Rn, RD, RM and RS registers
        d = darm.disasm_armv7(encoding)
        result = []
        if d.Rn and register == d.Rn.idx:
            result.append('rn')
        if d.Rd and register == d.Rd.idx:
            result.append('rd')
        if d.Ra and register == d.Ra.idx:
            result.append('rn')  # Not a bug Rt and Rd lives in same bits
        if d.Rt and register == d.Rt.idx:
            result.append('rd')  # Not a bug Rt and Rd lives in same bits
        if d.Rs and register == d.Rs.idx:
            result.append('rs')
        if d.Rm and register == d.Rm.idx:
            result.append('rm')
        if d.reglist.reglist > 0 and register in d.reglist.reglist:
            result.append('reg_list')
        return result

    def modify_register(self, encoding, register_number, new_reg, register_part=None):

        d = darm.disasm_armv7(encoding)

        if d.Rn and register_number == d.Rn.idx and register_part in [None, 'rn']:
            encoding = self.modify_rn(encoding, new_reg)

        elif d.Rd and register_number == d.Rd.idx and register_part in [None, 'rd']:
            encoding = self.modify_rd(encoding, new_reg)

        elif d.Ra and register_number == d.Ra.idx and register_part in [None, 'rn']:
            encoding = self.modify_rn(encoding, new_reg)  # Not a bug Rt and Rd lives in same bits

        elif d.Rt and register_number == d.Rt.idx and register_part in [None, 'rd']:
            encoding = self.modify_rd(encoding, new_reg)  # Not a bug Rt and Rd lives in same bits

        elif d.Rs and register_number == d.Rs.idx and register_part in [None, 'rs']:
            encoding = self.modify_rs(encoding, new_reg)

        elif d.Rm and register_number == d.Rm.idx and register_part in [None, 'rm']:
            encoding = self.modify_rm(encoding, new_reg)

        elif d.reglist.reglist > 0 and register_number in d.reglist.reglist  and register_part in [None, 'reg_list']:
            encoding = self.modify_register_list(encoding, register_number, new_reg)

        #encoding = self.swap23(encoding)
        return encoding

    def modify_register_list(self, encoding, register, new_reg):
        #if instruction.is_push_pop():
        encoding &= 2 ** register
        encoding |= 2 ** new_reg
        return encoding
        #else:
        #    raise RuntimeError('Not a register list instruction')