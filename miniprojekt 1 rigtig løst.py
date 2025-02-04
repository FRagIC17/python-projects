from random import randint


korrektTal=randint(0, 100)
antalGæt = 0
gættetTal = True
print(korrektTal)

while gættetTal == True:
    gætTal = int(input('Gæt et tal mellem 1 og 100: '))
    if gætTal == korrektTal:
        print('tilykke du gættede korrekt!')
        antalGæt += 1
        print('du brugte: ' + str(antalGæt) + ' gæt for at finde tallet')
        break

    if abs(gætTal) < 0 or gætTal > 100:
        print('ugyldigt tal prøv igen')
    elif abs(gætTal) > 50:
        print('Meget langt forbi!')
        antalGæt += 1
        print('du har nu brugt ' + str(antalGæt) + ' gæt')
    elif abs(gætTal) > 19 or abs(gætTal) < 49:
        print('Du er ikke helt ved siden af!')
        antalGæt += 1
        print('du har nu brugt ' + str(antalGæt) + ' gæt')
    else:
        print('tampen brænder!')

    if antalGæt > 9:
        print('du har ikke flere gæt, det korrekte tal var: ' + str(korrektTal))




