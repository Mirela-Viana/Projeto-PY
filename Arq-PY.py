print('olá jovens')
Anoatual = 2023
nascimento = 1997
nascimentojovem = 2006

def calculoIdade (nascimento , Anoatual):
 idade = Anoatual - nascimento
 return idade

idade = calculoIdade(nascimento , Anoatual)
idadejovem = calculoIdade(nascimentojovem , Anoatual)

print (' idade é' + str(idade))
print ('idade jovem' + str(idadejovem))


