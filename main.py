""" exercice se servant des listes via la recherche de palindrome"""
#### Fonction secondaire


def ispalindrome(p):
    """paramaetre: p un string correspondant a notre chaine de charactere
     return: boolean true ou false declarant si p est un palindrome """
    p = p.lower()
    table = str.maketrans("éèêëâàäîïûüôöç", "eeeeaaaiiuuooc")
    table2 = str.maketrans("",""," _-,;:.?!'")
    p = p.translate(table)
    p = p.translate(table2)

    print (p)

    return bool(p[::-1]==p)


#### Fonction principale


def main():
    """fonction main"""

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
