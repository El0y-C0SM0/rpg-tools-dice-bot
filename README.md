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
