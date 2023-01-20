import random
import pickle

from pokemon import *

NOMES = [
    "pedro", "kily", "wesley", "diego", "renato", "gary", "jhon", "spider", "ranson", "hilbert",
    "patrick", "cris", "gary", "smith", "jorge", "mary", "christma", "kendall","yuri", "lorenzo", "toni", "junior",
]

POKEMONS = [
    PokemonFogo("charmander"),
    PokemonFogo("charmilion"),
    PokemonFogo("flarion"),
    PokemonEletrico("pikachu"),
    PokemonEletrico("raichu"),
    PokemonAgua("squirtle"),
    PokemonAgua("magicarp")
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], cash=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.cash = cash

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("\nPokemons de {}: ".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} Nao tem nenhum pokemon".format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador nao possui nenhum pokemon para ser escolhido.")

    def show_cash(self):
        print("voce possui ${}".format(self.cash))

    def ganhar_dinheiro(self, qtd):
        self.cash += qtd
        print("Voce ganhou ${}".format(qtd))
        self.show_cash()

    def batalhar(self, pessoa):
        print("\n{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} GANHOU A BATALHA!!!".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} GANHOU A BATALHA!!!".format(pessoa))
                    break
        else:
            print("Essa batalha nao pode ocorrer!")


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                opcao = input("Qual sua escolha? ")
                try:
                    opcao = int(opcao)
                    pokemon_escolhido = self.pokemons[opcao]
                    print("{} EU ESCOLHO VOCE!!!\n\n".format(pokemon_escolhido))
                    print("BATALHA INICIADA!!!\n\n")
                    return pokemon_escolhido
                except:
                    print("opcao invalida.")
        else:
            print("ERRO: Esse jogador nao possui nenhum pokemon para ser escolhido.")

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print("Um pokemon selvagem por perto: {}".format(pokemon))

            escolha = input("Deseja capturar esse pokemon?  (s/n)")
            if escolha == "s":
                if random.random() >= 0.5:
                    print("Pokemon capturado com sucesso!")
                    self.capturar(pokemon)
                else:
                    print("{} Pokemon fugiu!".format(pokemon))

            else:
                print("Ok, Boa viagem!")
        else:
            print("Essa exploracao nao deu em nada!")


class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)





