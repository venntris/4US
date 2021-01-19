
define p = Character("Prowadząca", who_color="#CC0066")

# The game starts here.

label start:

    scene rozdzial1 with dissolve
    pause
    scene scene1a with dissolve
    pause

    label name:
    $ name = renpy.input("Jak masz na imię?")
    if name == "":
        "Podaj imię, pole jest puste."
        jump name
    name "Mam na imię [name]."
    pause

    name "Zobaczmy co jest w telewizji..."

    show prowadzaca with dissolve
    pause

    p "... wytwórnia KDEntertainment oczekuje na zgłoszenia do programu przetrwania. "
    p "Szukamy dziesięciu kandydatek, które zmierzą się ze sobą w różnych zadaniach. Cztery z nich zadebiutują w nowym koreańskim zespole 4:us!"

    $ confidence = 0
    menu:
        "Nie ma na co czekać!":
            $ confidence += 1
        "Nie wiem czy się do tego nadaję...":
            $ confidence += 0

    if confidence == 1:
        "Twoja pewność siebie wzrasta!"
    else:
        "Musisz być bardziej pewna siebie!"
    "Twoja pewność siebie wynosi [confidence]."
