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


def is_palindrome(n) -> bool:
    '''
    Determina daca un numar este palindrom
    :param n: numar intreg
    :return: True sau False
    '''
    copie = n
    invers=0
    while copie:
        invers=invers*10+copie%10
        copie=copie//10
    if invers == n:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(233) == False
    assert is_palindrome(123321) == True
    assert is_palindrome(5) == True
    assert is_palindrome(2145126) == False


def main():
    '''
    Meniu
    '''
    test_get_leap_years()
    test_get_perfect_squares()
    test_is_palindrome()
    should_Run=True
    while (should_Run==True):
        print("Optiunea 1: Afiseaza toti anii bisecti intre doi ani dati.")
        print("Optiunea 2: Afiseaza toate patratele perfecte dintr-un interval inchis dat.")
        print("Optiunea 3: Determina daca un numar este palindrom.")
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
        elif optiune == "3":
            n = int(input("Introdu numarul pe care doresti sa-l verifici daca este palindrom: "))
            print(is_palindrome(n))
        elif optiune=="x":
            should_Run=False
        else:
            print("Ai introdus o optiune GRESITA!!! Te rog alege alta din cele prezentate mai sus.")


if __name__ == '__main__':
    main()