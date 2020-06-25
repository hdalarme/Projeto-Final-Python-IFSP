import os
# Projeto Final do curso de Extensão "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.
# Turma: PROGPYTHON-202001
# Aluno: Helbertt Dalarme
# https://github.com/hdalarme/Projeto-Final-Python-IFSP

totalAlunos = 0
aprovadosM = 0
aprovadosF = 0
aprovados = 0
exame = 0
exameM = 0
exameF = 0
reprovados = 0
reprovadosM = 0
reprovadosF = 0
pecentutalAprovados = 0
pecentutalExame = 0
pecentutalReprovados = 0

cadastrar = input("Deseja iniciar lançamentos (S/N)? ")
while cadastrar.upper() != 'S' and cadastrar.upper() != 'N':
    cadastrar = input("Opção invalida, informe (S/N): ")

while cadastrar.upper() == 'S':
    nome = input("Informa o nome do aluno: ")
    sexo = input("Informe o sexo do aluno (M/F): ")
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        sexo = input("Opção invalida, informe (M/F): ")
    for cont in range (1,4):
        if cont==1:
            nota1 = int(input("Informe a Nota 1: "))
            while nota1<0 or nota1>10:
                nota1=int(input("Nota1 invalida, valor deve ser entre 0 e 10: "))
        elif cont==2:
            nota2 = int(input("Informe a Nota 2: "))
            while nota2 < 0 or nota2 > 10:
                nota2 = int(input("Nota2 invalida, valor deve ser entre 0 e 10: "))
        else:
            nota3 = int(input("Informe a Nota 3: "))
            while nota3 < 0 or nota3 > 10:
                nota3 = int(input("Nota3 invalida, valor deve ser entre 0 e 10: "))

    # calculo da média (nota1 + nota2 + nota3)/3
    media = (nota1 + nota2 + nota3)/3
    #print(str(media))
    print("A média de " + nome + " é " + format(media, '.2f'))

    #preenchendo informação
    if media>=7:
        aprovados += 1
        if sexo.upper() == "M":
            aprovadosM += 1
        else:
            aprovadosF += 1
    elif media<4:
        reprovados += 1
        if sexo.upper() == "M":
            reprovadosM += 1
        else:
            reprovadosF += 1
    else:
        exame += 1
        if sexo.upper() == "M":
            exameM += 1
        else:
            exameF += 1

    totalAlunos = aprovados+exame+reprovados
    pecentutalAprovados = (aprovados/totalAlunos)*100
    pecentutalExame = (exame/totalAlunos)*100
    pecentutalReprovados = (reprovados/totalAlunos)*100

    #limpa o log de processamento
    os.system('cls' if os.name == 'nt' else 'clear')

    cadastrar = input("Deseja efetuar outro lançamentos (S/N)? ")
    while cadastrar.upper() != 'S' and cadastrar.upper() != 'N':
        cadastrar = input("Opção invalida, informe (S/N): ")

else:
    print(" -- Fim do cadastro --")

if totalAlunos > 0:
    print(" *** Resultados ***")
    print(" *** PORCENTAGEM ***")
    #print('Quantidade percentual de alunos Aprovados: ' + str(pecentutalAprovados) + '%')
    print("Quantidade percentual de alunos Aprovados: %.2f" % pecentutalAprovados)
    #print("Quantidade percentual de Exame: " + str(exame/totalAlunos)+ '%')
    print("Quantidade percentual de alunos de Exame: %.2f" % pecentutalExame)
    #print("Quantidade percentual Reprovados: " + str(reprovados/totalAlunos)+ '%')
    print("Quantidade percentual de alunos Reprovados: %.2f" % pecentutalReprovados)

    print(" *** VALORES ABSOLUTOS ***")
    print("Quantidade de pessoas do sexo feminino Aprovadas: " + str(aprovadosF))
    print("Quantidade de pessoas do sexo masculino Aprovadas: " + str(aprovadosM))
    print("Quantidade de pessoas do sexo feminino de Exame: " + str(exameF))
    print("Quantidade de pessoas do sexo masculino de Exame: " + str(exameM))
    print("Quantidade de pessoas do sexo feminino Reprovadas: " + str(reprovadosF))
    print("Quantidade de pessoas do sexo masculino Reprovadas: " + str(reprovadosM))

os.system("pause")