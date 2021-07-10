
import interface


def main():

    print("\n=======================Bienvenue sur la CEDEAO App=============================\n")

    continuer = 1
    while continuer == 1:
        interface.menu()
        continuer = int(input("Voulez vous continuer? OUI= 1 et NON = 0\n"))


if __name__ == '__main__':
    main()
