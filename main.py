#!python

# print('Bem-vindo!')
# import pacote.sub.arquivo

# import tipos.variaveis
# from tipos import variaveis, basicos
# import tipos.lista
# import tipos.tuplas
# import tipos.conjuntos
# import tipos.dicionario

# import operadores.unarios
# import operadores.aritmeticos
# import operadores.relacionais
# import operadores.atribuicao
# import operadores.logicos
# import operadores.ternario

# import controle.if_1
# import controle.if_2
# import controle.for_1
# import controle.while_1
# import controle.outros_exemplos

from funcoes import basico

basico.saudacao()
basico.saudacao('Maria')
basico.saudacao('João', 33)
basico.saudacao(idade=89)

a = basico.soma_e_multiplica(x=10, a=2, b=3)
b = basico.soma_e_multiplica(x=20, a=3, b=7)
resultado = a + b
print(resultado)
