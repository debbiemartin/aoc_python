import functools

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def parse_nested(self, text):
        """
        Generate nested list structure representing parenthetic contents.
        """

        stack = [[]]
        for c in text:
            if c == " ":
                continue
            if c == "(":
                stack[-1].append([])
                stack.append(stack[-1][-1])
            elif c == ")":
                stack.pop()
                if not stack:
                    raise ValueError('error: opening bracket is missing')
            else:
                stack[-1].append(c)

        if len(stack) > 1:
            print(text)
            raise ValueError('error: closing bracket is missing')

        return stack.pop()


    def solve(self, symbols):
        """
        Takes in nested list of operations and solves for value. Solves L->R
        with no precedence considerations.
        """
        # Just go through the list adding either the number for a string or the
        # solution for a nested list
        val = (int(symbols[0]) if isinstance(symbols[0], str) else self.solve(symbols[0]))

        for i in range(2, len(symbols), 2):
            factor = (int(symbols[i]) if isinstance(symbols[i], str) else self.solve(symbols[i]))
            if symbols[i-1] == "*":
                val *= factor
            else:
                val += factor

        return val

    def solve_precedence(self, symbols):
        """
        Takes in nested list of operations and solves for value. Solves with order
        of precedence - addition before multiplication.
        """

        # Split the symbols into "sum lists" i.e. sublists split on the product
        # sign "*", for which the sums are calculated recursively (like in the
        # "solve" function) before the final product of all of these sum lists is
        # calculated.
        #
        # Gross way to split a list of lists on an occurence of string...
        sumlists = []
        start = 0
        while "*" in symbols[start:]:
            index = symbols[start:].index("*")
            sumlists.append(symbols[start:start + index])
            start += index + 1
        sumlists.append(symbols[start:])

        prodlist = (sum(
            0 if s == "+" else
            int(s) if isinstance(s, str) else
            self.solve_precedence(s)
            for s in sumlist)
            for sumlist in sumlists
        )

        return functools.reduce(lambda a, b: a * b, prodlist)


    def calculate(self):
        self.equations = [self.parse_nested(l) for l in self.parser.get_lines()]

    def part_1(self):
        return sum(self.solve(equation) for equation in self.equations)

    def part_2(self):
        return sum(self.solve_precedence(equation) for equation in self.equations)
