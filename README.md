# Jogo da Velha em Python

Este é um jogo da velha simples implementado em Python, jogado no terminal, onde dois jogadores alternam jogadas para marcar `X` e `O` em um tabuleiro 3x3. O objetivo é alinhar três símbolos iguais em uma linha, coluna ou diagonal antes do adversário.

## Pré-requisitos

- Python 3.6 ou superior

## Instalação

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/jogo-da-velha-python.git
    cd jogo-da-velha-python
    ```

2. Certifique-se de que você tem o Python instalado e execute o jogo:

    ```bash
    python3 jogo_da_velha.py
    ```

## Como Jogar

- O jogo é para dois jogadores: **Jogador X** e **Jogador O**.
- Cada jogador escolhe uma posição no tabuleiro, indicando a linha e a coluna desejadas.
- O objetivo é conseguir alinhar três símbolos iguais (X ou O) em uma linha, coluna ou diagonal.

## Exemplo de Uso

Ao iniciar o jogo, você verá uma representação do tabuleiro 3x3 no terminal. Cada jogador fará uma escolha de posição até que um dos jogadores vença ou todas as posições estejam preenchidas.

Exemplo de uma rodada:


## Estrutura do Código

O código principal está dividido nas seguintes funções:

- **exibir_tabuleiro(tabuleiro)**: Exibe o estado atual do tabuleiro no terminal.
- **verificar_vencedor(tabuleiro, jogador)**: Verifica se o jogador atual conseguiu alinhar três símbolos, vencendo o jogo.
- **jogo_da_velha()**: Controla o fluxo do jogo, alternando entre os jogadores e verificando o estado do tabuleiro.

## Funcionalidades

- Interface no terminal
- Tabuleiro atualizado a cada jogada
- Verificação automática de vitória ou empate
- Validação para evitar jogadas em espaços ocupados

## Contribuindo

Se você deseja contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório
2. Crie uma nova branch para sua feature ou correção: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'Adicionei uma nova feature'`
4. Faça o push para a branch: `git push origin minha-feature`
5. Abra um Pull Request
