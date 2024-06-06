# upper coloca as letras minusculas em maiusculo
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


for letra in texto:
    if letra.upper() in VOGAIS:
        print (f"Ha essa vogal no texto {letra}")
else:
    print() #adiciona quebra de linha

#exemplo utilizando a funçao range
for numero in range(0,51,5):
    print (numero, end="")

