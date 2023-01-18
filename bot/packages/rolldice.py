from random import randint

class RollDice:
    def __init__(self, solicitacao: str) -> None:
        self.solicitacao = solicitacao
        self.dados = solicitacao.split(' ')
        self.quant_dados = len(self.dados)
        self.total = 0
        self.resultados = []

    
    ### Gera o numero aleatório no intervalo do dado ###
    def _rola(self, dado: str) -> int:
        match dado:
            case 'd2':
                return randint(1, 2)
            case 'd3':
                return randint(1, 3)
            case 'd4':
                return randint(1, 4)
            case 'd6':
                return randint(1, 6)
            case 'd8':
                return randint(1, 8)
            case 'd10':
                return randint(1, 10)
            case 'd12':
                return randint(1, 12)
            case 'd20':
                return randint(1, 20)
            case 'd100':
                return randint(1, 100)
            case 'd1000':
                return randint(1, 1000)
            case _:
                return -1

    ### Realiza a rolagem individual de cada dado e retorna os resultados desse dado ###
    def rolar_dado(self, dado: str) -> str:
        def monta_string(dado: str, resultados: list, soma: int, mod: int=0) -> str:
            if -1 in resultados:
                return '[ERRO: Solicitação invalida]'

            resultado = f'[{soma}] <- '
            soma_resultados = ''

            if len(resultados) > 1:
                for i in range(len(resultados)-1):
                    soma_resultados = f'{soma_resultados}{resultados[i]} + '
                    
            soma_resultados = soma_resultados + str(resultados[len(resultados)-1])

            if mod > 0:
                soma_resultados = f'{soma_resultados} + {mod}'
            elif mod < 0:
                soma_resultados = f'{soma_resultados} - {mod * -1}'

            dado = f' ({dado})\n'

            return resultado + soma_resultados + dado

        mod = 0
        dado_cpy = dado

        if '+' in dado:
            sinal_mod = dado.find('+')
            mod = int(dado[sinal_mod + 1:])
            dado = dado[:sinal_mod]
        elif '-' in dado:
            sinal_mod = dado.find('-')
            mod = int(dado[sinal_mod + 1:]) * -1
            dado = dado[:sinal_mod]

        soma = mod

        if 'd' not in dado:
            return '[ERRO]\n'
        elif dado[0] != 'd':
            inicio_dado = dado.find('d')
            quant = int(dado[:inicio_dado])
            resultados = []

            for i in range(quant):
                rolado = self._rola(dado[inicio_dado:])
                soma = soma + rolado
                resultados.append(rolado)

            self.total = self.total + soma
            return monta_string(dado_cpy, resultados, soma, mod)

        elif dado[0] == 'd':
            resultados = []

            rolado = self._rola(dado)

            soma = soma + rolado
            resultados.append(rolado)

            self.total = self.total + soma
            return monta_string(dado_cpy, resultados, soma, mod)

        return '[ERRO: NAO ROLADO]\n'

    ### Faz a rolagem solicitada e retorna a string formatada com todos os resultados ###
    def faz_rolagens(self) -> str:
        resultado = ''

        for i in range(len(self.dados)):
            resultado = f'{resultado}{self.rolar_dado(self.dados[i])}'

        if len(self.dados) > 1:
            resultado = f'{resultado}[{self.total}] <- total'

        return resultado