import re
from random import randint

dice_pattern = r"(^\d+)?d(\d+)((\+|\-|\/|\*|\*\*)(\d+))?"


def is_dice_pattern(text: str) -> bool:
    """
    Verifica se o texto é um padrão de rolagem de dados.

    :param text: Texto a ser verificado.
    :type text: str
    :return: True se o texto é um padrão de rolagem de dados, False caso contrário.
    :rtype: bool
    """
    return re.match(dice_pattern, text) is not None


def parse_dice_command(text: str) -> tuple[int, int, str, int]:
    """
    Extrai os valores de um padrão de rolagem de dados.

    :param text: Texto a ser analisado.
    :type text: str
    :return: Número de dados, número de faces, operação matemática e modificador.
    :rtype: tuple[int, int, str, int]
    """
    match = re.match(dice_pattern, text)
    dices = int(match.group(1)) if match.group(1) else 1
    faces = int(match.group(2))
    operation = match.group(4) if match.group(4) else "+"
    mod = int(match.group(5)) if match.group(5) else 0

    return dices, faces, operation, mod


def roll_dice(faces: int) -> int:
    """
    Rola um dado com o número especificado de faces.

    :param faces: Número de faces do dado.
    :type faces: int
    :return: Resultado da rolagem do dado.
    :rtype: int
    """
    return randint(1, faces)


def calculate_mod(dice: int, operation: str, mod: int) -> int:
    """
    Aplica uma operação matemática ao resultado de uma rolagem de dado.

    :param dice: Resultado da rolagem do dado.
    :type dice: int
    :param operation: Operação matemática a ser aplicada ('+', '-', '/', '*', '**').
    :type operation: str
    :param mod: Valor do modificador a ser aplicado.
    :type mod: int
    :return: Resultado após aplicar a operação.
    :rtype: int
    """
    if operation == "+":
        return dice + mod
    elif operation == "-":
        return dice - mod
    elif operation == "/":
        return dice // mod
    elif operation == "*":
        return dice * mod
    elif operation == "**":
        return dice**mod
    else:
        return dice


def roll_best_dice(faces: int, dices: int) -> list:
    """
    Rola vários dados e retorna os resultados em ordem decrescente.

    :param faces: Número de faces dos dados.
    :type faces: int
    :param dices: Número de dados a serem rolados.
    :type dices: int
    :return: Lista de resultados das rolagens em ordem decrescente.
    :rtype: list
    """
    return sorted([roll_dice(faces) for _ in range(dices)], reverse=True)


def roll_worst_dice(faces: int, dices: int) -> list:
    """
    Rola vários dados e retorna os resultados em ordem crescente.

    :param faces: Número de faces dos dados.
    :type faces: int
    :param dices: Número de dados a serem rolados.
    :type dices: int
    :return: Lista de resultados das rolagens em ordem crescente.
    :rtype: list
    """
    return sorted([roll_dice(faces) for _ in range(dices)])


def roll_dices(faces: int, dices: int) -> list:
    """
    Rola vários dados e retorna os resultados.

    :param faces: Número de faces dos dados.
    :type faces: int
    :param dices: Número de dados a serem rolados.
    :type dices: int
    :return: Lista de resultados das rolagens.
    :rtype: list
    """
    return [roll_dice(faces) for _ in range(dices)]


def roll_dices_sum_with_mod(
    faces: int, dices: int = 1, operation: str = "+", mod: int = 0
) -> tuple[int, int, list]:
    """
    Rola vários dados, aplica um modificador ao resultado total e retorna o resultado e as rolagens individuais.

    :param dices: Número de dados a serem rolados.
    :type dices: int
    :param faces: Número de faces dos dados.
    :type faces: int
    :param operation: Operação matemática a ser aplicada ('+', '-', '/', '*', '**').
    :type operation: str
    :param mod: Valor do modificador a ser aplicado.
    :type mod: int
    :return: Resultado após aplicar a operação e lista de resultados das rolagens.
    :rtype: tuple[int, list]
    """
    rolls = roll_dices(faces, dices)
    sum_rolls = sum(rolls)
    return calculate_mod(sum_rolls, operation, mod), sum_rolls, rolls


def roll_best_dice_with_mod(
    faces: int, dices: int = 1, operation: str = "+", mod: int = 0
) -> tuple[int, int, list]:
    """
    Rola vários dados, seleciona o melhor resultado, aplica um modificador e retorna o resultado e as rolagens individuais.

    :param dices: Número de dados a serem rolados.
    :type dices: int
    :param faces: Número de faces dos dados.
    :type faces: int
    :param operation: Operação matemática a ser aplicada ('+', '-', '/', '*', '**').
    :type operation: str
    :param mod: Valor do modificador a ser aplicado.
    :type mod: int
    :return: Resultado após aplicar a operação ao melhor dado e lista de resultados das rolagens.
    :rtype: tuple[int, list]
    """
    rolls = roll_best_dice(faces, dices)
    best = rolls[0]
    return calculate_mod(best, operation, mod), best, rolls


def roll_worst_dice_with_mod(
    faces: int, dices: int = 1, operation: str = "+", mod: int = 0
) -> tuple[int, int, list]:
    """
    Rola vários dados, seleciona o pior resultado, aplica um modificador e retorna o resultado e as rolagens individuais.

    :param dices: Número de dados a serem rolados.
    :type dices: int
    :param faces: Número de faces dos dados.
    :type faces: int
    :param operation: Operação matemática a ser aplicada ('+', '-', '/', '*', '**').
    :type operation: str
    :param mod: Valor do modificador a ser aplicado.
    :type mod: int
    :return: Resultado após aplicar a operação ao pior dado e lista de resultados das rolagens.
    :rtype: tuple[int, list]
    """
    rolls = roll_worst_dice(faces, dices)
    worst = rolls[0]
    return calculate_mod(worst, operation, mod), worst, rolls


def roll_dice_with_mod(faces: int, operation: str, mod: int) -> tuple[int, int]:
    """
    Rola um dado, aplica um modificador e retorna o resultado.

    :param faces: Número de faces do dado.
    :type faces: int
    :param operation: Operação matemática a ser aplicada ('+', '-', '/', '*', '**').
    :type operation: str
    :param mod: Valor do modificador a ser aplicado.
    :type mod: int
    :return: Resultado após aplicar a operação e resultado da rolagem do dado.
    :rtype: tuple[int, int]
    """
    dice = roll_dice(faces)
    return calculate_mod(dice, operation, mod), dice


def roll_dices_all_with_mod(
    faces: int, dices: int = 1, operation: str = "+", mod: int = 0
) -> tuple[int, list, list]:
    """
    Rola vários dados, aplica um modificador a cada resultado e retorna o resultado total e as rolagens individuais.

    :param dices: Número de dados a serem rolados.
    :type dices: int
    :param faces: Número de faces dos dados.
    :type faces: int
    :param operation: Operação matemática a ser aplicada ('+', '-', '/', '*', '**').
    :type operation: str
    :param mod: Valor do modificador a ser aplicado.
    :type mod: int
    :return: Resultado após aplicar a operação e lista de resultados das rolagens com modificador e sem modificador.
    :rtype: tuple[int, list, list]
    """

    rolls_results = [roll_dice_with_mod(faces, operation, mod) for _ in range(dices)]

    rolls_with_mod = [result[0] for result in rolls_results]
    rolls = [result[1] for result in rolls_results]

    return sum(rolls_with_mod), rolls_with_mod, rolls
