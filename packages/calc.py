### Classe de calculo ###
class Calc:
    def __init__(self, number1, operacao, number2):
        if ',' in number1:
            number1 = float(number1)
        else:
            number1 = int(number1)
            
        if ',' in number2:
            number2 = float(number2)
        else:
            number2 = int(number2)

        self.number1 = number1
        self.operacao = operacao
        self.number2 = number2
        self.resultado = 0

    ### Soma os dois numeros que foram digitados ###
    def _soma(self):
        self.resultado = self.number1 + self.number2
        return self.resultado

    ### Subtrai do number1 numero o valor do number2 ###
    def _subtrai(self):
        self.resultado = self.number1 - self.number2
        return self.resultado
    
    ### Multiplica os dois numeros que foram digitados ###
    def _multiplica(self):
        self.resultado = self.number1 * self.number2
        return self.resultado

    ### Divide o number1 pelo number2 ###
    def _divide(self):
        self.resultado = self.number1 / self.number2
        return self.resultado

    ### Calcula o valor percentual do number1 no number2 ###
    def _porcentual(self):
        self.resultado = self.number2 * (self.number1 / 100)
        return self.resultado

    ### Exponecia o number1 pelo number2 ###
    def _exponencia(self):
        self.resultado = self.number1 ** self.number2

    ### Realiza o calculo solicitado ###
    def calcula(self) -> str:
        match self.operacao:
            case '+':
                return str(self._soma())
            case '-':
                return str(self._subtrai())
            case '*' | '×' | 'x':
                return str(self._multiplica())
            case '/' | '÷':
                if self.number1 == 0 or self.number2 == 0:
                    return 'ERRO divisao por 0'
                return str(self._divide())
            case '**' | '^':
                return str(self._exponencia())
            case '%':
                return str(self._porcentual())
            case _:
                return 'ERRO: operador não reconhecido'