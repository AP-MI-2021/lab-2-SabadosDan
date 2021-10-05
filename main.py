import math
def get_leap_years(start: int , end: int) -> list[int]:
    '''
    Returneaza toti anii bisectii intre anul start si anul end
    :param start: primul an
    :param end: ultimul an
    :return: lst : lista de numere intregi care reprezinta anii bisecti dintre start si end
    '''
    lst=[]
    for i in range(start, end+1):
        if i % 4 == 0:
            lst.append(i)
    return lst


def test_get_leap_years():
    '''
    Functia de test al functiei get_leap_years()
    '''
    assert get_leap_years(2004,2008) == [2004,2008]
    assert get_leap_years(1985,2000) == [1988,1992,1996,2000]
    assert get_leap_years(2001,2003) == []


test_get_leap_years()


def get_perfect_squares(start: int, end: int) -> list[int]:
    '''
    Returneaza toate patratele cuprinse intre 2 numere date
    :param start: primul numar
    :param end: ultimul numar
    :return: lst : lista de numere intregi care reprezinta patratele perfecte cuprinse intre primul si ultimul numar
    '''
    lst = []
    for i in range(start, end + 1):
        if math.sqrt(i)*math.sqrt(i)==int(math.sqrt(i))*int(math.sqrt(i)):
            lst.append(i)
    return lst


def test_get_perfect_squares():
    '''
    Functia de test al functiei get_perfect_squares
    '''
    assert get_perfect_squares(15,30) == [16,25]
    assert get_perfect_squares(65,80) == []
    assert get_perfect_squares(1,16) == [1,4,9,16]


test_get_perfect_squares()


def main():
    '''
    Meniu
    '''
    should_Run=True
    while (should_Run==True):
        print("Optiunea 1: Afiseaza toti anii bisecti intre doi ani dati.")
        print("Optiunea 2: Afiseaza toate patratele perfecte dintr-un interval inchis dat.")
        print("Optiunea x: Iesire")
        optiune = input("Alege o optiune de mai sus: ")
        if optiune == "1":
            print("Citeste anii intre care doresti sa se afiseze anii bisecti: ")
            primul_an = int(input("Primul an:"))
            ultimul_an = int(input("Ultimul an:"))
            if get_leap_years(primul_an, ultimul_an) == []:
                print("Nu exista ani bisecti")
            else:
                print("*Anii bisecti dintre ", primul_an, " si ", ultimul_an, " sunt : ")
                print(get_leap_years(primul_an, ultimul_an ))
        elif optiune == "2":
            print("Citeste numerele intre care doresti sa se afiseze toate patratele perfecte: ")
            primul_numar = int(input("Primul numar: "))
            ultimul_numar = int(input("Al doilea numar: "))
            if get_perfect_squares(primul_numar, ultimul_numar) == []:
                print ("Nu exista patrate perfecte")
            else:
                print("Patratele perfecte cuprinse in [",primul_numar, ",", ultimul_numar,"] sunt: ")
                print(get_perfect_squares(primul_numar,ultimul_numar))
        elif optiune=="x":
            should_Run=False
        else:
            print("Ai introdus o optiune GRESITA!!! Te rog alege alta din cele prezentate mai sus.")


main()