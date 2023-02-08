from os import system
from re import search

blue = "\033[1;34m"
red = "\033[1;31m"
cancel = "\033[m"

dados_temp = list()
dados_cres_temp = list()
dados_decres_temp = list()

for x in range(5):
    while True:
        temperatura = str(input(f"Digite a {x+1}º dado da temperatura registrado: "))
        if(not search("^[+-]?[0-9]+$", temperatura)):
            print("Valor da primeira nota não é numerica, porfavor digite novamente.")
        else:
            temperatura = int(temperatura)
            dados_temp.append(temperatura)
            dados_cres_temp.append(temperatura)
            dados_decres_temp.append(temperatura)
            break

for i in range(len(dados_cres_temp)):
    for j in range(i+1, len(dados_cres_temp)):
        if dados_cres_temp[i] > dados_cres_temp[j]:
            dado = dados_cres_temp[i]
            dados_cres_temp[i] = dados_cres_temp[j]
            dados_cres_temp[j] = dado
            
for i in range(len(dados_decres_temp)):
    for j in range(i+1, len(dados_decres_temp)):
        if dados_decres_temp[i] < dados_decres_temp[j]:
            dado = dados_decres_temp[i]
            dados_decres_temp[i] = dados_decres_temp[j]
            dados_decres_temp[j] = dado

system('cls')

print(f"A ordem obitida dos dados são: {dados_temp};")
print(f"Os valores crescentes: {dados_cres_temp};")
print(f"Os valores decrescentes: {dados_decres_temp};")
print(f"Portanto o valor mínimo e máximo obtido foram respectivamente: {blue}{dados_cres_temp[0]}{cancel} e {red}{dados_decres_temp[0]}{cancel}.")
    
