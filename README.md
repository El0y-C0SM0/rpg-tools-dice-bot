# RPG Tools - Dice Bot ![Versão](https://img.shields.io/badge/vers%C3%A3o-2.0.0-purple?style=flat-square) ![Status](https://img.shields.io/badge/status-concluido-lightblue?style=flat-square)

## Descrição

O **RPG Tools - Dice Bot** é um bot desenvolvido para facilitar as sessões de RPG no Discord. Ele permite realizar rolagens de dados com diversos modificadores, enviar resultados de forma sigilosa e simplificar a dinâmica do jogo. 

O código-fonte seguro do bot está disponível [aqui](https://github.com/El0y-C0SM0/rpg-tools-dice-bot/tree/main/bot).

Adicione o bot ao seu servidor do Discord clicando [aqui](https://discord.com/oauth2/authorize?client_id=1063954442006831234&permissions=2048&scope=bot%20applications.commands).

Explore também a aplicação completa do [RPG Tools](https://github.com/El0y-C0SM0/RPG-Tools), que oferece ferramentas adicionais, como registro de armas e calculadoras para RPG.

## Comandos

### Descrição dos Comandos
- `/help`: Exibe todos os comandos disponíveis.
- `/roll`: Rola dados e soma o modificador ao total. Exemplo: `2d20+2 d6`.
- `/best`: Rola dados e escolhe o melhor resultado. Exemplo: `2d20+2 d6`.
- `/worst`: Rola dados e escolhe o pior resultado. Exemplo: `2d20+2 d6`.
- `/allmod`: Rola dados e aplica o modificador a todos os resultados. Exemplo: `2d20+2 d6`.
- `/hiddenroll`: Rola dados secretamente e soma o modificador ao total. Exemplo: `2d20+2 d6`.
- `/hiddenbest`: Rola dados secretamente e escolhe o melhor resultado. Exemplo: `2d20+2 d6`.
- `/hiddenworst`: Rola dados secretamente e escolhe o pior resultado. Exemplo: `2d20+2 d6`.
- `/hiddenallmod`: Rola dados secretamente e aplica o modificador a todos os resultados. Exemplo: `2d20+2 d6`.

### Tipos de Sigilo
- `all`: Sigilo total.
- `minimum`: Notifica que dados foram rolados.
- `verbose`: Notifica quais dados foram rolados.

### Operadores
- `+`: Soma o valor ao resultado.
- `-`: Subtrai o valor do resultado.
- `*`: Multiplica o resultado pelo valor.
- `/`: Divide o resultado pelo valor.
- `**`: Eleva o resultado ao valor.

## Rode localmente

Esse bot é aberto para ser adaptado e executado localmente. Siga os passos abaixo para configurar o ambiente:

### Configuração do Ambiente

1. Clone o repositório:
2. Crie um ambiente virtual e ative-o, a versão recomendada do Python é a **3.12**.
3. Instale as dependências
4. Crie um arquivo `.env` em `bot/` e preencha as variáveis.

### Arquivo ENV de referência

Caso deseje configurar o bot localmente, utilize o seguinte modelo para o arquivo `.env`:

```
DEBUG=False
TOKEN_TESTE=""
TOKEN_BOT=""
GUILD_ID_TESTE=0
GUILD_ID=0
```

Observe que os valores devem ser preenchidos conforme suas necessidades, portanto, é necessário ter as próprias aplicações registradas no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications). Se não quiser especificar servidores de teste, pode deixar os IDs como `0`.
