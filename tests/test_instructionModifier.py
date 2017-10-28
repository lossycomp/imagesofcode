from unittest import TestCase

from semantic_codec.architecture.capstone_instruction import CAPSInstruction
from semantic_codec.architecture.instruction_modifier import InstructionModifier


class TestInstructionModifier(TestCase):

    #def test_modify_cond(self):
    #    self.fail()

    #def test_modify_opcode(self):
    #    self.fail()

    def test_modify_rn(self):
        inst = CAPSInstruction('000209b4', 8)  # strheq;r0, [r2], -r4
        mod = InstructionModifier()
        self.assertEqual('strheq\tr0, [r0], -r4', str(CAPSInstruction(mod.modify_rn(inst.encoding, 0), 8)))
        self.assertEqual('strheq\tr0, [r4], -r4', str(CAPSInstruction(mod.modify_rn(inst.encoding, 4), 8)))
        self.assertEqual('strheq\tr0, [sl], -r4', str(CAPSInstruction(mod.modify_rn(inst.encoding, 10), 8)))

    def test_get_registers_parts(self):
        mod = InstructionModifier()
        # andeq r0, r0, r0
        parts = mod.get_registers_parts(0x00000000, 0)
        self.assertEqual(3, len(parts))
        self.assertTrue('rn' in parts)
        self.assertTrue('rd' in parts)
        self.assertTrue('rm' in parts)

    def test_modify_rd(self):
        '0xe59f1018'
        inst = CAPSInstruction('e59f1018', 8)  # ldr	r1, [pc, #0x18]
        mod = InstructionModifier()
        self.assertEqual('ldr\tr0, [pc, #0x18]', str(CAPSInstruction(mod.modify_rd(inst.encoding, 0), 8)))
        self.assertEqual('ldr\tr4, [pc, #0x18]', str(CAPSInstruction(mod.modify_rd(inst.encoding, 4), 8)))
        self.assertEqual('ldr\tsl, [pc, #0x18]', str(CAPSInstruction(mod.modify_rd(inst.encoding, 10), 8)))

    #def test_modify_rs(self):
    #    self.fail()

    def test_modify_rm(self):
        inst = CAPSInstruction('000209b4', 8)  # strheq;r0, [r2], -r4
        mod = InstructionModifier()
        self.assertEqual('strheq\tr0, [r2], -r0', str(CAPSInstruction(mod.modify_rm(inst.encoding, 0), 8)))
        self.assertEqual('strheq\tr0, [r2], -r6', str(CAPSInstruction(mod.modify_rm(inst.encoding, 6), 8)))
        self.assertEqual('strheq\tr0, [r2], -sl', str(CAPSInstruction(mod.modify_rm(inst.encoding, 10), 8)))

    #def test_modify_immediate(self):
    #    self.fail()

    def test_modify_register(self):
        inst1 = CAPSInstruction('000209b4', 8)  # strheq;r0, [r2], -r4
        inst2 = CAPSInstruction('e59f1018', 8)  # ldr	r1, [pc, #0x18]
        mod = InstructionModifier()
        self.assertEqual('strheq\tr0, [r2], -r0', str(CAPSInstruction(mod.modify_register(inst1.encoding, 4, 0), 8)))
        self.assertEqual('strheq\tr0, [r6], -r4', str(CAPSInstruction(mod.modify_register(inst1.encoding, 2, 6), 8)))

        self.assertEqual('ldr\tr6, [pc, #0x18]', str(CAPSInstruction(mod.modify_register(inst2.encoding, 1, 6), 8)))
        self.assertEqual('ldr\tr1, [r6, #0x18]', str(CAPSInstruction(mod.modify_register(inst2.encoding, 15, 6), 8)))

    #def test_modify_register_list(self):
    #    self.fail()
