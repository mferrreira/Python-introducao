"""
Faça um jogo para o usuário adivinhnar qual a palavra secreta.

- Você vai propor uma palavra secreta 
qualquer e vai dar a possibilitade para
o usuário digitar apenas uma letra.

- Qual o usuário digitar uma letra, você
vai conferir se a letra digitada está 
na palavra secreta.

    - Se a letra digitada estiver 
    na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver 
    na palavra secreta; exiba *

Faça a contagem de tentativas do seu usuário
"""

palavra = 'papibaquigrafo'
TAMANHO_DA_PALAVRA = len(palavra)
progresso = TAMANHO_DA_PALAVRA * '*'
tentativas = 0

while True:

    print(f'Palavra: {progresso}')

    entrada = input('Digite uma letra da palavra: ')

    if len(entrada) > 1:
        print('Digite apenas uma letra!')
        continue

    i = 0
    for letra in palavra:
        if entrada == letra and progresso[i] == '*':
            novo_progresso = progresso[:i] + entrada + progresso[i+1:] 
            progresso = novo_progresso
        i+=1

    if '*' not in progresso:
        print(f'Você descobriu {palavra} com {tentativas} tentativas')
        break
    tentativas += 1