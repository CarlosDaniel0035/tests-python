#Recebe o valor da divida e em seguida recebe a quantidade de dias atrasados
#calcula e retorna a divida + 3% de multa + juros de 1% a cada dia de atraso

def valorPagamento(valor, dias):
    if dias > 0:
        taxa = (dias * (0.1/100)) * valor
        return (valor * 1.03) + taxa
    return valor

def main():
    valor = float(input("Valor da multa:"))
    dias = int(input("Dias Atrasados:"))
    print(valorPagamento(valor,dias))
main()