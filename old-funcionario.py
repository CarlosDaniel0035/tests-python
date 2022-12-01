#O programa pede para informar o codigo de cada funcionario e em seguida sua idade
#Após todos digitar o codigo e a idade de cada funcionario digite: 0
#Irá retornar o funcionario mais velho e o mais jovem

def ponto(coisa,casas=2):
  pedacos = coisa.split(",")
  return round(int(pedacos[0]) + (float(pedacos[1])/(10**len(pedacos[1]))),casas)


funcionarios = []
wcodigo = 1
while (wcodigo):
  wcodigo = int(input("Informe o codigo do funcionario ou 0 para terminar"))
  if wcodigo:
    widade = int(input("Informe a idade"))
    funcionarios.append( { 'Codigo': wcodigo, 'Idade':widade}  )


mais_velho = -1
mais_novo = 999

for x in funcionarios:
  if x['Idade'] > mais_velho:
    qual_mais_velho = x['Codigo']
    mais_velho = x['Idade']
  if x['Idade'] < mais_novo:
    qual_mais_novo = x['Codigo']
    mais_novo = x['Idade']

print()
print("O mais novo é",qual_mais_novo,"e tem",mais_novo,"anos de idade")
print("O mais velho é",qual_mais_velho,"e tem",mais_velho,"anos de idade")