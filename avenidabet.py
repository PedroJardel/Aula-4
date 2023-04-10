import random
import os
# declara os vetores globais
apostadores = []
valores = []
placar = []
gol_caxias = []
gol_gremio = []


def ler_arquivo():
    # se o arquivo não existe, retorna
    if not os.path.isfile("apostas.txt"):
        return
# abre o arquivo para leitura
    with open("apostas.txt", "r") as arq:
        linhas = arq.readlines()

    for linha in linhas:
        partes = linha.split(";")
        apostadores.append(partes[0])
        placar = partes[1].split('x')
        gol_caxias.append(placar[0])
        gol_gremio.append(placar[1])
        valores.append(float(partes[2][0:-1]))


def salva_arquivo():
    with open("apostas.txt", "w") as arq:
        for nome, gol1, gol2, valor in zip(apostadores, gol_caxias, gol_gremio, valores):
            arq.write(f"{nome};{gol1}x{gol2};{valor}\n")


def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*30)


def cadastrar_aposta():
    titulo("Inclusão de Aposta")
    nome = input("Nome do Apostador: ")

    # forma que restringe erro do usuário
    # placar1 = int(input("Digite  a quantidade de Gols que o Caxias irá fazer: "))
    # placar2 = int(input("Digite  a quantidade de Gols que o Grêmio irá fazer: "))
    # placar = str(placar1)+"x"+str(placar2)

    # Forma para avaliação abaixo.
    placar_string = input("Digite o placar da aposta Ex:(1x1): ").lower()
    contador = 0
    for x in placar_string:
        if x == 'x':
            contador += 1
    if contador >= 1:
        partes = placar_string.split('x')
        for x in partes:
            numero = x.strip()
            if numero.isdigit():
                placar.append(numero)
        gol1 = placar[0]
        gol2 = placar[1]
    else:
        print("Formato do placar incorreto! Tente novamente")
        return

    valor = float(input("valor da Aposta: R$"))
    apostadores.append(nome)
    gol_caxias.append(gol1)
    gol_gremio.append(gol2)
    valores.append(valor)
    print()
    print("Ok! Aposta cadastrada com sucesso")


def listar_apostas():
    titulo("Lista de Apostas Cadastradas")
    print("Nº Nome do Apostador...... Placar Valor....")
    for x, (nome, gol1, gol2, valor) in enumerate(zip(apostadores, gol_caxias, gol_gremio, valores), start=1):
        print(f"{x:2} {nome:25} {gol1}x{gol2:3} {valor}")


def listar_resultado():
    titulo("Resultado das Apostas")
    print("Nº Nome............ Resultado")
    for x, (nome, gol1, gol2) in enumerate(zip(apostadores, gol_caxias, gol_gremio), start=1):
        if gol1 > gol2:
            print(f"{nome:20} Caxias")
        elif gol1 == gol2:
            print(f"{nome:20} Empate")
        else:
            print(f"{nome:20} Gremio")


def total_apostas():
    titulo("Total de Apostas Feitas")
    print("Nº de Apostas.......Total(R$)")
    print(f"{len(apostadores):5} {sum(valores):20}")


def apostas_por_resultado():
    titulo("Apostas por Resultado")
    print("Quant. de Apostas........ Resultado")
    total_apostas_caxias, total_apostas_gremio, total_apostas_empate = 0, 0, 0
    for x, (valor, gol1, gol2) in enumerate(zip(valores, gol_caxias, gol_gremio), start=1):
        if gol1 > gol2:
            total_apostas_caxias += valor
        elif gol1 == gol2:
            total_apostas_empate += valor
        else:
            total_apostas_gremio += valor
    print(f"R$ {total_apostas_caxias}{'':19}Caxias")
    print(f"R$ {total_apostas_empate}{'':20}Empate")
    print(f"R$ {total_apostas_gremio}{'':20}Gremio")


def resultado():
    titulo("Resultado Final")
    resultado = ['Caxias', 'Empate', 'Gremio']
    aleatorio = random.randrange(0, 3)
    total = sum(valores)
    total_parcial_caxias, total_parcial_empate, total_parcial_gremio = 0, 0, 0 
    print(f"Resultado: {resultado[aleatorio]}")
    print()
    print("Nº Nome.......... Quant Receber(R$)")
    for x, ( valor, gol1, gol2) in enumerate(zip(valores, gol_caxias, gol_gremio), start=1):
        if resultado[aleatorio] == 'Caxias':
            if gol1 > gol2:
                total_parcial_caxias += valor
        elif resultado[aleatorio] == 'Empate':
            if gol1 == gol2:
                total_parcial_empate += valor
        elif resultado[aleatorio] == 'Gremio':
            if gol1 < gol2:
                total_parcial_gremio += valor

    for x, (nome, valor, gol1, gol2) in enumerate(zip(apostadores, valores, gol_caxias, gol_gremio), start=1):
        if resultado[aleatorio] == 'Caxias':
            if gol1 > gol2:
                print(f"{x:2} {nome:20} R$ {(( valor / total_parcial_caxias)* total):,.2f}")
        elif resultado[aleatorio] == 'Gremio':
            if gol1 < gol2:
                print(f"{x:2} {nome:20} R$ {(( valor / total_parcial_gremio)* total):,.2f}")
        elif resultado[aleatorio] == 'Empate':
            if gol1 == gol2:
                print(f"{x:2} {nome:20} R$ {(( valor / total_parcial_empate)* total):,.2f}")

ler_arquivo()

while True:
    titulo("AvenidasBet – Controle de Apostas\nCaxias x Grêmio (Final do Gauchão 2023)", "=")
    print("1. Cadastrar Aposta")
    print("2. Listar Apostas")
    print("3. Listar Resultado")
    print("4. Total de Apostas")
    print("5. Apostas por Resultado")
    print("6. Resultado da Premiação")
    print("7. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        cadastrar_aposta()
    elif opcao == 2:
        listar_apostas()
    elif opcao == 3:
        listar_resultado()
    elif opcao == 4:
        total_apostas()
    elif opcao == 5:
        apostas_por_resultado()
    elif opcao == 6:
        resultado()
    else:
        salva_arquivo()
        break
