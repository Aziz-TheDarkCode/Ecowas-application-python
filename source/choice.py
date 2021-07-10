#importation du module choice
import country

def userChoice(choice):  
    if choice == 1:
        country.getCountry()
    elif choice == 2:
        country.newCountry()
    elif choice == 3:
        country.editCountry()
    elif choice == 4:
        country.deleteCountry()
    elif choice == 5:
        country.AllCountries()
    else :
        pass;