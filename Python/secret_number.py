# -*- coding: utf-8 -*-

print "Pogodite tajni broj i osvojite nagrade!"

secret = 249

guess = int(raw_input("Tajni broj je: "))

if secret == guess:
    print "Čestitamo! Pogodili ste tajni broj!"
else:
    print "Niste pogodili tajni broj. Pokušajte ponovno!"