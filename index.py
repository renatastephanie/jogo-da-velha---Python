# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all([celula == jogador for celula in tabuleiro[i]]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1

            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns! Jogador {jogador_atual} venceu!")
                return

            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Espaço já ocupado! Tente novamente.")

    exibir_tabuleiro(tabuleiro)
    print("Empate! Ninguém venceu.")

# Iniciar o jogo
jogo_da_velha()
