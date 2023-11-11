import random


def banco():
    return f"{random.randint(0, 999):03}".zfill(3)


def sucursal():
    return f"{random.randint(0, 9999):04}".zfill(4)


def cuenta():
    return f"{random.randint(0, 9999999999999):013}".replace(" ", "0")


def calcular(var1, var2, var3):
    verificador1 = (
            int(var1[0]) * 7
            + int(var1[1]) * 1
            + int(var1[2]) * 3
            + int(var2[0]) * 9
            + int(var2[1]) * 7
            + int(var2[2]) * 1
            + int(var2[3]) * 3
    )
    verificador1 = (10 - (verificador1 % 10)) % 10

    verificador2 = (
            int(var3[0]) * 3
            + int(var3[1]) * 9
            + int(var3[2]) * 7
            + int(var3[3]) * 1
            + int(var3[4]) * 3
            + int(var3[5]) * 9
            + int(var3[6]) * 7
            + int(var3[7]) * 1
            + int(var3[8]) * 3
            + int(var3[9]) * 9
            + int(var3[10]) * 7
            + int(var3[11]) * 1
            + int(var3[12]) * 3
    )
    verificador2 = (10 - (verificador2 % 10)) % 10

    return "CBU : {}{}{}{}{}".format(var1, var2, verificador1, var3, verificador2)


def generar():
    var1 = banco()
    var2 = sucursal()
    var3 = cuenta()
    return calcular(var1, var2, var3)


def main():
    print(generar())


if __name__ == "__main__":
    main()
