from abc import ABC, abstractmethod

from core.roll_dices import *


class BaseRoll(ABC):
    def __init__(self, command: str):
        dices, faces, operation, mod = parse_dice_command(command)

        self._command = command
        self._faces = faces
        self._dices = dices
        self._operation = operation
        self._mod = mod

        self._results = self.roll()

        self._dices_rolls = self._results[2]
        self._result = self._results[1]
        self._total = self._results[0]

    @abstractmethod
    def roll(self):
        pass

    @property
    def command(self):
        return self._command

    @property
    def faces(self):
        return self._faces

    @property
    def dices(self):
        return self._dices

    @property
    def operation(self):
        return self._operation

    @property
    def mod(self):
        return self._mod

    @property
    def result(self):
        return self._result

    @property
    def total(self):
        return self._total

    @property
    def dices_rolls(self):
        return self._dices_rolls


class Roll(BaseRoll):
    def roll(self):
        return roll_dices_sum_with_mod(self.faces, self.dices, self.operation, self.mod)

    def __str__(self):
        out = f"{self.total} ⟵ [{' + '.join([str(rol) for rol in self.dices_rolls])}]"

        if self.operation and self.mod:
            out += f" {self.operation} {self.mod}"

        out += f" ({self.command})"

        return out

    def __repr__(self):
        return f"<Roll: {self.command} = {self.total}>"


class BestRoll(BaseRoll):
    def roll(self):
        return roll_best_dice_with_mod(self.faces, self.dices, self.operation, self.mod)

    def __str__(self):
        out = f"{self.total} ⟵ [{', '.join([str(rol) for rol in self.dices_rolls])}]"

        if self.operation and self.mod:
            out += f" {self.operation} {self.mod}"

        out += f" ({self.command})"

        return out

    def __repr__(self):
        return f"<BestRoll: {self.command} = {self.total}>"


class WorstRoll(BaseRoll):
    def roll(self):
        return roll_worst_dice_with_mod(
            self.faces, self.dices, self.operation, self.mod
        )

    def __str__(self):
        out = f"{self.total} ⟵ [{', '.join([str(rol) for rol in self.dices_rolls])}]"

        if self.operation and self.mod:
            out += f" {self.operation} {self.mod}"

        out += f" ({self.command})"

        return out

    def __repr__(self):
        return f"<WorstRoll: {self.command} = {self.total}>"


class RollModAll(BaseRoll):
    def roll(self):
        return roll_dices_all_with_mod(self.faces, self.dices, self.operation, self.mod)

    def __str__(self):
        results = []

        for rol, rol_mod in zip(self._dices_rolls, self._results[1]):
            results.append(f"({rol_mod}={rol}{self.operation}{self.mod})")

        out = f"{self.total} ⟵ [{' + '.join(results)}]"

        out += f" ({self.command})"

        return out

    def __repr__(self):
        return f"<RollModAll: {self.command} = {self.total}>"


class RollTypes:
    ROLL = "roll"
    BEST = "best"
    WORST = "worst"
    ALL = "all"


class RollFactory:
    @staticmethod
    def create(command: str, roll_type: str = "roll") -> BaseRoll:
        if roll_type == RollTypes.ROLL:
            return Roll(command)
        elif roll_type == RollTypes.BEST:
            return BestRoll(command)
        elif roll_type == RollTypes.WORST:
            return WorstRoll(command)
        elif roll_type == RollTypes.ALL:
            return RollModAll(command)
        else:
            return Roll(command)


class Rolls:
    def __init__(self, command_line: str, roll_type=RollTypes.ROLL):
        self._command_line = command_line
        self._roll_type = roll_type

        commands = command_line.split(" ")

        self._rolls = [RollFactory.create(command, roll_type) for command in commands]

    def __str__(self):
        return "\n".join(str(roll) for roll in self.rolls)

    def __repr__(self):
        return f"<Rolls {self.roll_type}: {self.command_line}>"

    @property
    def command_line(self):
        return self._command_line

    @property
    def roll_type(self):
        return self._roll_type

    @property
    def rolls(self):
        return self._rolls
