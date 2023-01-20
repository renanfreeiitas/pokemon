import pickle

from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print("Ola {}, voce podera escolher agora o pokemon que ira te acompanhar nessa jornada!".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonAgua("Charmander", level=1)
    squirtle = PokemonFogo("Squirtle", level=1)

    print("Voce possui tres opcoes: ")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        opcao = input("Qual sua escolha? \n")

        if opcao == "1":
            player.capturar(pikachu)
            break
        elif opcao == "2":
            player.capturar(charmander)
            break
        elif opcao == "3":
            player.capturar(squirtle)
            break
        else:
            print("Opcao invalida")


def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar jogo")
        print(error)


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso.")
            return player
    except:
        print("Novo por aqui? ")


if __name__ == "__main__":
    print("**************************************")
    print("Bem-vindo ao game Pokemon RPG de terminal")
    print("**************************************")

    player = carregar_jogo()

    if not player:
        nome = input("Olá, qual é o seu nome: ")
        player = Player(nome)
        print("Olá {}, esse é um mundo habitado por pokemons,\n"
              "a partir de agora sua missão é se tornar um mestre dos pokemons!\n".format(player))
        print("Capture o máximo de pokemons que conseguir e lute com seus inimigos\n")
        player.show_cash()

        if player.pokemons:
            print("Já ví que você tem alguns pokemons\n")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokemon, portanto precisa escolher um\n")
            escolher_pokemon_inicial(player)

        print("Pronto, agora que você já possui um pokemon, enfrente seu arqui-rival desde o jardim da infância Gary\n")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("**************************************")
        print("1 - Explorar")
        print("2 - Batalhar")
        print("3 - Mostrar Pokemons")
        print("0 - Sair do jogo")
        print("**************************************")
        escolha = input("O que deseja fazer? ")

        if escolha == "0":
            print("FECHANDO O JOGO.")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        else:
            print("Escolha invalida!")
