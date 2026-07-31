peso = 10
frete = 10
frete2 = 20
frete3 = 30
totalpeso = 0
totalfrete = 0
print("Digite o peso do pacote..")
peso = float(input())
if peso >= 1:
    for i in range(0, 10 + 1, 1):
        print("Digite o peso do pacote novamente.. ")
        peso = float(input())
        print("Digite o destino(Nacional ou internacional)")
        destino = input()
        if destino == "inter":
            print("Destino intrenacional..")
            if peso < 2:
                print("categoria: Leve ")
                print("seu frete seria de : " + str(frete * 1.2))
            else:
                if peso < 10:
                    print("categoria padrão")
                    print("seu frete = 24")
                else:
                    print("categoria: pesado")
                    print("seu frete = 36")
                print("categoria: padrão")
        else:
            print("Destino nacional..")
            if peso < 2:
                print("categoria: Leve ")
                print("seu frete seria de : " + str(frete))
            else:
                if peso < 10:
                    print("categoria padrão")
                    print("seu frete seria de : " + str(frete2 * 1.2))
                else:
                    print("categoria: pesado")
                    print("seu frete seria de : " + str(frete3 * 1.2))
                print("categoria: padrão")
        totalpeso = totalpeso + peso
        totalfrete = totalfrete + frete
    ticketmedio = totalfrete / 10
    print("///       ///")
    print("total peso: " + str(totalpeso))
    print("faturamento final: " + str(totalfrete))
    print("ticket médio: " + str(ticketmedio))
else:
    print("Digite o peso do seu pacote..")
