"""Cette partie affiche le meenu """

def menu():
    print("=======================Bienvenue sur la CEDEAO app=============================")
    while True:
        try:
            print("1.Afficher un pays membre")
            print("2.Ajouter un nouveau pays")
            print("3.Modifier un pays membre")
            print("4.Supprimer un pays membre")
            uChoice = int(input("Que voulez vou faire ?\n"))     
            if uChoice in range(1,4):
                print("good u can continue")
                break
        except:    
            pass
            print ('\nChoix Incorrect !')

