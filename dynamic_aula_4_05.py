#Ex.1 - função class
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

#Criando os objetos
p1 = Pessoa("ana", 25)
p2 = Pessoa("paulo", 30)

p1.apresentar()
p2.apresentar()
'''
##########################################################################
#Ex.2 - Se quiser utilizar uma lista com objetos que passam dentro da classe e que passam por uma estrutura de repetição, irá funcionar (foi o que eu entendi).
'''
pessoas = [
    Pessoa("ana", 25),
    Pessoa("Jacinto", 30),
    Pessoa("Dacueba", 69)
]
for pessoa in pessoas:
    pessoa.apresentar()
'''
##########################################################################
#Ex.3 - calcular área do retangulo
'''
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)

#Criando os objetos
r1 = Retangulo(4,2)
r2 = Retangulo(5,10)

print(f"A área do r1 é {r1.area()} e o seu perimetro é {r1.perimetro()}")
print(f"A área do r2 é {r2.area()} e o seu perimetro é {r2.perimetro()}")
'''
###################################################################################
#Ex.4 - calcular a área e perimetro do retângulo (utilizando apenas função def)
'''
def area_perimetro(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

print(area_perimetro(4,5))
'''
#####################################################################################
#EX.5 - Padronizar nomes e gerar emails
'''
class Usuario:
    def __init__(self, nome, dominio):
        self.nome = nome
        self.dominio = dominio
    def email(self):
        nome_formatado = self.nome.strip().lower().replace("",".")
        return f"{nome_formatado}@{self.dominio}"

#Criando os objetos
usu1 = Usuario("Claiton", "empresa.com")
usu2 = Usuario(input(), ".com.br")

print(usu1.email())
print(usu2.email())
'''
#################################################################################
#Exe.6 - Crie 3 objetos da classe Carro e armazene-os em uma lista. Depois, percorra a lista e exiba descriação de cada carro. Carro: Corolla, ano 2026, cor: azul.
'''
class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
    def apresentar(self):
        print(f"Marca do carro: {self.marca} | ano do carro: {self.ano} | Cor do carro: {self.cor}")
carros = [
    Carro("Corolla",2010,"Azul"),
    Carro("Ferrari",2020,"Vermelho"),
    Carro("Fiat",2005,"Roxo")
]
u1 = Carro(input("Informe a marca do carro:"), input("Insira o ano de fábricação: "),input("Diga a cor do carro: "))
u1.apresentar()
for carro in carros:
    carro.apresentar()
'''
#################################################################################
#Exe.7 - Crie uma classe Aluno com os atributos nome, nota1 e nota2. Adicione um metodo media() que retorne a media das notas. Depois, crie uma lista de alunos e mostre suas médias.

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):
        return (self.nota1 + self.nota2) / 2
    def apresentar(self):
        print(f"O aluno: {self.nome} | tirou a média: {self.media()}")

alunos = [
    Aluno("Claiton",5,5),
    Aluno("Rosangela",10,10),
    Aluno("Cleitin",8,6)
]

for aluno in alunos:
    aluno.apresentar()

#################################################################################
#Exe.8 - Integração com DataFrame: Use a classe Aluno para gerar um DataFrame. Com as colunas: Nome, Nota 1, Nota 2 e media.
import pandas as pd
dados_alunos = []
for aluno in alunos:
    dados_alunos.append({"Nome:":aluno.nome,
                         "Nota1:":aluno.nota1,
                         "Nota2:":aluno.nota2,
                         "Média:":aluno.media()})

df = pd.DataFrame(dados_alunos)
print(df)