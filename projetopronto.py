#missões
missao_planta = False
missao_jornal = False
missao_carne = False
#marcadores de missões
missao_planta_cumprida = False
missao_jornal_cumprida = False
missao_carne_cumprida = False
#itens
planta = "Bromélia Rara"
jornal = "Jornal de Biologia"
carne = "Carne do RU"
bolsa = set()

#funções para ajudar na organização do código
def sair():
    print("A)sair")
    while True:
        opcao = input()
        if opcao.upper() == "A":
            mapa()
            break
        else:
            print("Opção invalida!")
def escolha_de_dialogo_simples(opcao_a, opcao_b):
    while True:
        opcao = input()
        if opcao.upper() == "A":
            print(opcao_a)
            break
        elif opcao.upper() == "B":
            print(opcao_b)
            break
        else:
            print("Opção invalida!")
def pegar_item(item):
    global bolsa
    bolsa.add(item)
    print(f"'{item} foi adicionado a bolsa!'")
def entregar_item(item):
    global missao_planta
    global missao_planta_cumprida

    global missao_jornal
    global missao_jornal_cumprida

    global missao_carne
    global missao_carne_cumprida
    global bolsa
    bolsa.remove(item)
    if item == planta:
        missao_planta = False
        missao_planta_cumprida = True
    elif item == jornal:
        missao_jornal = False
        missao_jornal_cumprida = True
    elif item == carne:
        missao_carne = False
        missao_carne_cumprida = True
    print(f"'{item} foi retirado da bolsa!'")

#Mapa
def mapa():
    print("Mapa:")
    print("                  TRANSRURAL")
    print("  ;;;;    ;;;;    ;;;;    ;;;;    ;;;;    ;;;;")
    print(" ;;;;;;  ;;;;;;  ;;;;;;  ;;;;;;  ;;;;;;  ;;;;;;")
    print(",,|  |,,,,|  |,,,,|  |,,,,|  |,,,,|  |,,,,|  |,,")
    print("")
    print("     ___________             ____________")
    print(r"    /___________\   |    |  /____________\ ")
    print("    | ___  ____ |   |    |  | ___   ____ |")
    print("    | | |  |DB| |   |    |  | | |   |RU| |")
    print("   _________________|    |________________")
    print("    _  _  _  _  _  _  _  _  _  _  _  _  _")
    print("   _________________      ________________")
    print("     ____________   |    |    ____________")
    print(r"    /____________\  |    |   /____________\ ")
    print("    | ___   ____ |  |    |   | ___   ____ |")
    print("    | | |   |DQ| |  |    |   | | |   |DC| |")
    print(f"\nBolsa: {bolsa or ""}")
    print(f"\nMissões:")
    if missao_carne == True:
        print("- Conseguir uma carne do RU para Jorge.")
    if missao_jornal == True:
        print("- Conseguir algo para Mimi dormir em cima.")
    if missao_planta == True:
        print("- Conseguir uma planta rara na transrural para Everaldo.")
    if missao_carne == False and missao_jornal == False and missao_planta == False:
        print("- Sem missões por enquanto! ")
    while True:
        print(f"\nAonde você quer ir?\nA)Transrural\nB)Departamento de Biologia(DB)\nC)Restaurante Universitário(RU)\nD)Departamento de Química(DQ)\nE)Departamento de Computação(DC)")
        opcao = input()
        if opcao.upper() == "A":
            cenario_transrural()
            break
        elif opcao.upper() == "B":
            cenario_db()
            break
        elif opcao.upper() == "C":
            cenario_ru()
            break
        elif opcao.upper() == "D":
            cenario_dq()
            break
        elif opcao.upper() == "E":
            cenario_dc()
            break
        else:
            print("Opção invalida!")

# Cenário ru
def cenario_ru():
    global missao_jornal
    print("\nResturante Universitário(RU):\n")
    print(r"       /\___/\   _ ")
    print(r"      ( ° ^ ° ) / / ")
    print(r"      /       \/ / ")
    print(r"     (_|_|_|_|_)/")
    print("Mimi:")
    if missao_jornal == False and missao_jornal_cumprida == False:
        missao_jornal = True
        print(f"Oh, Olá! Você é novo por aqui, certo? Meu nome é Mimi, qual é o seu?\nA){nome.capitalize()}\nB)Prefiro não falar...")

        escolha_de_dialogo_simples(f"{nome.capitalize()}... que nome legal! O que te traz aqui?", "Hum...prefere manter o mistério, gosto disso! O que te traz aqui?")

        print(f"A)Um outro gato me mandou vir aqui atrás de carne.\nB)Será você teria um pedaço de carne sobrando?")

        escolha_de_dialogo_simples("Ha, será que é o Jorge? Ele sempre me pertuba pra dar um pouco de carne, ele deveria se mudar logo  pra cá!", "Até que tenho, há sempre muita comida por aqui,hihi...")

        print("Mas sabe, aqui tem um problema, mesmo com toda comida, não tantos lugares confortáveis para dar um cochilo...\nSe você me troxer algo que eu possa dormir em cima, posso te arranjar um pouco de carne, o que acha?"
              "\nA)Me parece ótimo!\nB)É o jeito né?")
        escolha_de_dialogo_simples("Sabia que poderia contar com você! Quando encontra não demore muito para volta!", "Hihi, não vai ser tão difícil encotrar, volte logo!")
        sair()
    elif missao_jornal == True and jornal not in bolsa:
        print("Oi! Ainda nada na busca?\nA)Ainda estou procurando.\nB)Tá meio difícil de encontrar, poderia me dar uma dica do que pode servir.")
        escolha_de_dialogo_simples("vê se não demora na busca, hihi", "Hum...Acho que algo como um jornal serve.")
        sair()
    elif missao_jornal == True and jornal in bolsa:
        print("Oh, esse jornal que você tá carregando aí me parece ótimo para dormir em cima! O que acha de me dar ele como parte do combinado?\nA)Seria perfeito!(entregar o jornal para Mimi)\nB)Acho que vou pensar mais a respeito.")
        while True:
            opcao = input()
            if opcao.upper() == "A":
                entregar_item(jornal)
                print("Hihi, ele realmente parece maravilhoso! Como combinado, aqui está o pedaço de carne, separei um dos bons!")
                pegar_item(carne)
                sair()
                break
            if opcao.upper() == "B":
                print("Poxa, sério? qualquer coisa se mudar de ideia estarei aqui.")
                sair()
                break
            else:
                print("Opção invalida!")
    elif missao_jornal_cumprida == True:
        print("Hihihi, oi de novo! Aquele jornal está fazendo milagres para o meu sono, muito obrigada!")
        sair()


def cenario_dc():
    global bolsa
    global carne
    global missao_carne
    global missao_carne_cumprida
    print("\nDepartamento de Computação(DC):\n")
    print(r"       /\___/\   _ ")
    print(r"      ( ¬ ^ ¬ ) / / ")
    print(r"      /       \/ / ")
    print(r"     (_|_|_|_|_)/")
    print("Jorge:")
    if missao_carne == True and missao_carne_cumprida == False and carne not in bolsa:
        print(f"Ei, há quanto tempo, já conseguiu a carne?\nA)Não.\nB)Estou quase conseguindo.")
        escolha_de_dialogo_simples(f"Volte quando conseguir.", "Hahaha, já consigo sentir o gostinho daquela carne!")
        sair()
    elif missao_carne == True and carne in bolsa:
        print(f"Ei, meu nariz não está me enganando né?{nome.capitalize()}, você conseguiu a carne!\nA)Sim.(dar a carne para Jorge)\nB)Não, acho que seu nariz tá enganado.")
        while True:
            opcao = input()
            if opcao.upper() == "A":
                entregar_item(carne)
                print(f"Siiiimm! Era esse cheirinho que eu estava sentindo! Mal posso esperar para comer...\n"
                      f"Acho que me passei um pouco,mas você me entende né? Essa carne é uma maravilha! De toda forma trato é trato. Vou te deixar manda o email."
                      f"\nA)entrar no computador e mandar o email.\nB)Acho que vou curtir mais um pouco minha vida de gato.")
                while True:
                    opcao = input()
                    if opcao.upper() == "A":
                        break
                    elif opcao.upper() == "B":
                        print("Haha, querendo curtir um pouco mais os charmes da vida felina né? Quando se cansar poode vir aqui mandar o email!")
                        sair()
                        break
                    else:
                        print("Opção invalida!")
                break
            elif opcao.upper() == "B":
                print("Hum, será que meu nariz está começando a me pregar peças? De qualquer forma, volte quando conseguir a carne.")
                sair()
                break
            else:
                print("Opção invalida!")

    elif missao_carne_cumprida == True:
        print("Pronto para aposentar as garras e mandar o email?\nA)Sim.(entrar no computador e mandar o email.)\nB)Ainda não")
        while True:
            opcao = input()
            if opcao.upper() == "A":
                break
            elif opcao.upper() == "B":
                print("Haha, querendo curtir um pouco mais os charmes da vida felina né? Quando se cansar poode vir aqui mandar o email!")
                sair()
                break
            else:
                print("Opção invalida!")


def cenario_db():
    global missao_planta
    print(r"       /\___/\        _")
    print(r"      ( - ^ - )____  / /")
    print(r"      /            \/ /")
    print(r"     (_|_|_|_|_______/")
    print("Everaldo:")
    if missao_planta == False and missao_planta_cumprida == False:
        missao_planta = True
        print(f"Ah, olá! Você é novo por aqui, certo? meu nome é Everaldo, eu era um professor do departamento até que passei um pouco do tempo da minha aposentadoria,hehe...\n"
              f"Achei que isso só acontecia com os alunos. Minha sorte foi que meus alunos me acharam parecido com quando eu era humano e me deram o mesmo nome, hehe, qual é o seu nome?\n"
              f"A){nome.capitalize()}.\nB)Meu nome não é importante.")

        escolha_de_dialogo_simples(f"Um nome interessante, parece nome de cientista,não acha?", f"Conviver com aquilo que ainda não sabemos é uma habilidade útil para quem trabalha com a ciência.")

        print("De qualquer forma, eu tinha uma pesquisa sabe? Pesquisava sobre uma bromélia rara que tem por aqui, queria continuar a pesquisa, mas a idade chega pra todo mundo, hehe\n"
              "e, depois da minha aposentadoria forçada, o labratório fechou a pesquisa e não temos mais dessa planta por aqui...\n"
              "Será que você poderia conseguir uma delas pra mim? Gostaria de continuar minha pesquisa e tem delas na Transrural, eu mesmo iria lá, mas minhas patas não são mais as mesmas.\n"
              "As bromélias que quero são listradinhas, Você quebraria esse galho pra mim?\nA)Claro, qualquer coisa pela ciência!\nB)Acho que um passeio pela Transrual não me faria mal...")

        escolha_de_dialogo_simples(f"Esse é o verdadeiro espírito de um cientista!", f"É bom para esticar as canelas e o ar de lá é mais fresco,hehe.")

        print("Te vejo novamente quando conseguir a planta.")
        sair()
    elif missao_planta == True and planta not in bolsa:
        print("Olá de novo, o que te traz aqui?\nA)Esqueci como era a planta...\nB)Só queria dar uma passadinha.")

        escolha_de_dialogo_simples("Oh, sem problemas, ela é uma espécie de bromélia e ela é listradinha, não deve ser muito difícil de encontrar na Transrural.", "É realmente difícil ficar longe por muito tempo desse prédio,hehe.")

        sair()
    elif missao_planta == True and planta in bolsa:
        print("Meus olhos não estão me enganando né? Faz tempo que eu não vejo essa belezura, mas você a encontrou!\nA)Sim.(Dar a planta para Everaldo.)\nB)Sim, mas acho que vou ficar mais um pouquinho com ela.")
        while True:
            opcao = input()
            if opcao.upper() == "A":
                entregar_item(planta)
                print("Hehe, graças a você vou poder continuar minha pesquisa. Sempre dê valor à ciência meu jovem, vou te dar esse jornal de biologia, vai que te inspira a fazer algo novo.")
                pegar_item(jornal)
                break
            elif opcao.upper() == "B":
                print("Hehe, é difícil se separar dela né? Vou te dar mais um tempo com ela.")
                break
            else:
                print("Opção invalida!")
        sair()
    elif missao_planta_cumprida == True:
        print("Olá de novo, espero que o jornal tenha sido útil. Se não se incomodar vou voltar para minha pesquisa, hehe...")
        sair()


def cenario_transrural():
    if missao_planta == False and missao_planta_cumprida == False:
        print ("Você vê um lugar bastante arborizado, o clima é agradável. Há muitas plantas, mas você não reconhece nenhuma.")
        sair()
    elif missao_planta == True and planta not in bolsa:
        print("Você vê um lugar bastante arborizado, o clima é agradável.\nA)Procurar a planta.\nB)sair")
        while True:
            opcao = input()
            if opcao.upper() == "A":
                print("Você procura e, depois de um tempo, encontra uma planta que combina com a descrição de Everaldo.\nVocê a pega com cudaido e coloca na bolsa.")
                pegar_item(planta)
                sair()
                break
            if opcao.upper() == "B":
                mapa()
                break
            else:
                print("Opção invalida!")
    elif missao_planta_cumprida == True or planta in bolsa:
        print("Você vê um lugar bastante arborizado, o clima é agradável. Há muitas plantas. Você vê ao longe uma planta igual a que você pegou para Everaldo.")
        sair()


def cenario_dq():
    print("É o departamento de química, não tem muita coisa pra fazer por aqui...")
    sair()

#começo do jogo
print("Jubilados:")
print('"Na crença popular de nossas universidades, quando alguém é jubilado, essa pessoa se transforma em um gato ou cachorro."')
while True:
    print("Antes de começar-mos\nEste jogo usa a letra que você digita como forma de escolher entre as opções, independente se forem maiúsculas ou minúsculas, ok?\n"
          "Escolha a opção de acordo:")
    print("A)Não entendi.\nB)Entendi perfeitamente.")
    escolha = input()
    if escolha.upper() == "B":
        print("Muito bem! vamos dar proseguimento ao jogo...")
        break
    elif escolha.upper() == "A":
        print("Vamos tentar de novo...")
    else:
        print("Opção invalida!")

print("...Você é um aluno de computação e está na aula do último horário. Já é sua quarta vez pagando essa cadeira e você está por um fio de ser reprovado por falta.")
print("Você está com muito sono, só esperando o momento do professor fazer a chamada,mas os seus olhos estão tão pesados...\n"
      "E no momento que eles falham, você cai num sono profundo...\n\n")
print("'Ei, você está bem?'")
print("Você olha na direção da voz, e tudo o que consegue ver é um gato te olhando de cima.")
print(r"       /\___/\   _ ")
print(r"      ( ¬ ^ ¬ ) / / ")
print(r"      /       \/ / ")
print(r"     (_|_|_|_|_)/")
print("'Você é novo, né? Prazer, meu nome é Jorge. É um pouco difícil a adaptação a nova vida felina, mas logo você vai pegar o jeito!")
print("Por incrível que pareça a voz está saindo do gato, você se sente estranho e até um pouco...peludo?! Vocẽ realmente se transformou em um gato!!!")
print("'Hahaha, é comum ficar confuso no começo, mas vai se acostumar, qual o seu nome?")
nome = input()
print(f"{nome.capitalize()}? Que nome interessante, sei que é uma pergunta meio indelicada, mas o que te fez ser jubilado?\nA)Acho que dormi no meio da chamada...\nB)Ainda não tenho certeza...")

escolha_de_dialogo_simples(f"Hahaha, que má sorte! No meu caso, eu gostava tanto do RU que acabei atrasando minha conclusão até que não pude mais hahaha...", f"Hahaha, de toda forma, no meu caso, eu gostava tanto do RU que acabei atrasando minha conclusão até que não pude mais hahaha...")

print("Sabe,eu acho que posso te ajudar nessa. Acho que mandando um email pra pessoa certa o seu jubilamento pode ser retirado."
      f"\nEu poderia conseguir um computador numa sala vaga pra você mandar esse email,mas tudo tem um preço né?\n Eu estava pensando aqui, "
      f"se você conseguir uma carne do RU pra mim, eu posso quebrar essa pra você, o que você acha?\nA)Pode deixar comigo!\nB)Que outra escolha eu tenho?")

escolha_de_dialogo_simples(f"Hahaha, esse é o espírito! Aqui está o mapa daqui. Quando tiver a carne venha aqui que eu deixo mandar o email.", f"Hahaha, de toda forma, aqui está o mapa daqui, venha quando quiser mandar o email e tiver a carne.")

missao_carne = True
mapa()
#fim do jogo
print(f"Você digita o email com dificuldade com suas patinhas e consegue envia-lo...\n\n"
      f"Você acorda na sua sala de aula, humano novamente, com o professor chamando por você na chamada.")