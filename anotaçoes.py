# Operadores de repetição anotações 

# Identação e os blocos de comando 
# A estética, identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em python ela exerce um segundo papel, através da Identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

# Bloco de comando
# As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e o fim do bloco. Em Java e C por exemplo, utilizamos chaves:
# Ex:
# Bloco em Java
# Void sacar (double valor) {// início do bloco do método
#           If (this.saldo >= valor) {// inicio do bloco do if 
# 		this.saldo -= valor
#            }//fim do bloco do if 
# } // fim do bloco do método 

# Utilizando espaços 
# Existe uma convenção em python, que define as boas práticas para a escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de Identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.
# Ex:
# Bloco em python
# Def sacar (self, valor: float) None: # inicio do bloco do método
# 	If self.saldo >= valor: #inicio do bloco do if
# 		self.saldo -= valor
# 	#fim do bloco if
# # fim do bloco método 




# Estruturas condicionais

# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.
# If
# Para criar uma estrutura condicional simples, composta por um único desvio
# Else
# Para criar uma estrutura condicional com dois desvios
# Elif
# Em alguns cenários queremos mais de dois desvios, aí utilizamos o elif 

# If aninhado
# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else 

# If ternário
# O if ternário permite escrever uma condição em uma única linha

# Estruturas de repetição
# São estruturas utilizadas para repetir um trecho de código um determinado número de vezes.

# Comando for 
# É usado para percorrer um objeto iterável. Faz sentido usar o for quando sabemos previamente e o numero exato de vezes que será executado.
# Else é uma função do for
# Range é uma função do for, built-in do python é usada pra produzir uma sequência de números inteiros a partir de um inicio para um fim. Ela recebe 3 argumentos: stop(obrigatório), start (opcional) e step (opcional).





# Comando while 
# O comando while é usado para repetir um bloco de código varias vezes. Faz sentido usar quando na sabemos o numero exato de vezes que nosso bloco deve ser executado.
 

