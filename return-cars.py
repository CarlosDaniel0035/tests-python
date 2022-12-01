#O programa pede para o usuario inserir 4 modelos de carros seguidos, e em seguida dizer o consumo de cada carro na mesma sequencia
#E irá retornar o veiculo mais economico

carros = []
consumo = []

#função de repetição que só ira sair quando o usuario inserir 4 modelos de carros
def entrada_carro():
    while len(carros) < 4:
        cars = input("Modelo do carro:")
        carros.append(cars)
    return cars

#função para o usuario inserir o valor de consumo de cada carro esolhido na ordem
def entrada_consumo():
    for i in range(len(carros)):
        valor = int(input("Consumo do veiculo:"))
        consumo.append(valor)
    return valor

#função que irá retornar o veiculo mais economico
def economico():
    if consumo[0] < consumo[1] and consumo [0] < consumo[2] and consumo[0] < consumo[3]:
        return carros[0]

    elif consumo[1] < consumo[2] and consumo[1] < consumo[3]:
        return carros[1]

    elif consumo[2] < consumo[3]:
        return carros[2]

    else:
        return carros[3]

def main():
    entrada_carro()
    entrada_consumo()
    print(economico())
main()