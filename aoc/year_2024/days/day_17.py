import re


def test_instructions():
    d = Day(ParserStub(LINES))


class Machine(object):
    def __init__(self, program, registers):
        self.A = registers["A"]
        self.B = registers["B"]
        self.C = registers["C"]
        self.program = program
        self.out = []

    def combo(self, operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        assert False

    def run_program(self):
        ip = 0

        while ip < len(self.program)-1:
            opcode = self.program[ip]
            operand = self.program[ip+1]

            if opcode == 0:
                self.A = self.A >> self.combo(operand)
            elif opcode == 1:
                self.B = operand ^ self.B
            elif opcode == 2:
                self.B = self.combo(operand) % 8
            elif opcode == 3:
                if self.A != 0:
                    ip = operand
                    continue
            elif opcode == 4:
                self.B = self.B ^ self.C
            elif opcode == 5:
                self.out.append(self.combo(operand) % 8)
            elif opcode == 6:
                self.B = self.A >> self.combo(operand)
            elif opcode == 7:
                self.C = self.A >> self.combo(operand)

            ip += 2


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        regstr = self.parser.get_sections()[0]
        pattern = re.compile(r"Register (?P<reg>[A-C]): (?P<val>[0-9]+)")
        matches = pattern.findall(regstr)
        self.registers = {}
        for m in matches:
            self.registers[m[0]] = int(m[1])

        self.program = [
            int(x)
            for x in self.parser.get_sections()[1].split(": ")[1].split(",")
        ]

    def part_1(self):
        machine = Machine(self.program, self.registers)
        machine.run_program()
        return ",".join(str(s) for s in machine.out)

    def find_soln(self, A, pos):
        A = A << 3
        for test in range(8):
            self.registers["A"] = A + test
            machine = Machine(self.program, self.registers)
            machine.run_program()
            if machine.out[0] == self.program[pos]:
                if pos == 0:
                    return A + test
                soln = self.find_soln(A + test, pos-1)
                if soln:
                    return soln

    def part_2(self):
        return self.find_soln(0, len(self.program)-1)
