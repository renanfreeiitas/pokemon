import random


class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        self.level = level

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo
        print("{} PERDEU {} pontos de vida".format(pokemon, ataque_efetivo))
        print("")
        print("*******************")
        print("")

        if pokemon.vida <= 0:
            print("{} FOI DERROTADO!!!".format(pokemon))
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lancou um raio do trovao em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lancou uma bola de fogo na cabeca de {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print("{} lancou um jato de agua em {}".format(self, pokemon))
        return super().atacar(pokemon)