from enum import Enum
import math

class Pulse(Enum):
    high = 0
    low = 1

class Component(object):
    def __init__(self, outputs):
        self.outputs = outputs

    def process_pulse(self, input, pulse):
        raise NotImplementedError

    def add_input(self, input):
        pass

    def same_as_start(self):
        raise NotImplementedError

class FlipFlop(Component):
    def __init__(self, outputs):
        # Flip flop - initially off, turns on/off wit low pulse. Sends high pulse
        # when it turns on and low pulse when it turns off
        super().__init__(outputs)
        self.on = False

    def process_pulse(self, input, pulse):
        if pulse == Pulse.low:
            self.on = not self.on
            return Pulse.high if self.on else Pulse.low

    def same_as_start(self):
        return not self.on

class Conjunction(Component):
    def __init__(self, outputs):
        # Conjuntion - remember last pulse for all inputs, initially low pulse.
        # If all inputs high then sends low pulse otherwise sends high.
        super().__init__(outputs)
        self.inputs = {}

    def process_pulse(self, input, pulse):
        self.inputs[input] = pulse
        if all(p == Pulse.high for p in self.inputs.values()):
            return Pulse.low
        else:
            return Pulse.high

    def add_input(self, input):
        self.inputs[input] = Pulse.low

    def same_as_start(self):
        return all(p == Pulse.low for p in self.inputs.values())

class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.low_sum = 0
        self.high_sum = 0

    def calculate(self):
        lines = self.parser.get_lines()
        self.components = {}

        for line in lines:
            component = line.split(" -> ")[0]
            outputs = line.split(" -> ")[1].split(", ")

            if component.startswith("broadcaster"):
                self.broadcaster = outputs
            elif component.startswith("%"):
                self.components[component[1:]] = FlipFlop(outputs)
            elif component.startswith("&"):
                self.components[component[1:]] = Conjunction(outputs)

        for c, o in ((c, o) for c, comp in self.components.items() for o in comp.outputs):
            if o in self.components:
                self.components[o].add_input(c)

    def button_press(self, find_high):
        # Button - single low pulse is sent directly to the broadcaster module.
        # Broadcast - sends received pulse to all destinations.
        self.low_sum += 1
        found_high = set()
        queue = [(o, "broadcaster", Pulse.low) for o in self.broadcaster]
        while queue:
            to_component, from_component, i_pulse = queue.pop(0)

            if i_pulse == Pulse.high:
                self.high_sum += 1
            elif i_pulse == Pulse.low:
                self.low_sum += 1

            if to_component not in self.components:
                continue

            component = self.components[to_component]

            if "rx" in component.outputs:
                for i, p in component.inputs.items():
                    if i in find_high and p == Pulse.high:
                        found_high.add(i)

            o_pulse = component.process_pulse(from_component, i_pulse)

            if o_pulse:
                queue += [(o, to_component, o_pulse) for o in component.outputs]

        return found_high

    def part_1(self):
        # Doing p1 and p2 in a single loop so I don't have to reset
        for c in self.components.values():
            if "rx" in c.outputs:
                find_high = list(c.inputs.keys())

        highs = []
        for i in range(1, 1000000):
            found_high = self.button_press(find_high)
            if i == 1000:
                print(self.high_sum * self.low_sum)

            for f in found_high:
                find_high.remove(f)
                highs.append(i)

            if len(find_high) == 0:
                lcm = math.lcm(*highs)
                print(f"p2: {lcm}")
                return

    def part_2(self):
        pass
