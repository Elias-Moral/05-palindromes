#### Fonction secondaire


def ispalindrome(p):
    table = str.maketrans("éèêâàäîïûüôöç", "eeeaaaiiuuooc")
    table = str.maketrans("", "", " ")
    p = texte.translate(table)


    if (p[::-1]==p){
        return true
    }
    else{
        return False
    }

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
