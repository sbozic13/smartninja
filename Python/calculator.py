x = int(raw_input("Upisi vrijednost za x: "))
print "Vrijednost za x je:"
print x

operacija= raw_input("Odaberite operaciju: +,-,*,/ :")
print "Operacija je:"
print operacija

y_tekst = raw_input("Upisi vrijednost za y: ")
y = int(y_tekst)
print "Vrijednost za y je:"
print y

if operacija == "+":
    print "Zbroj x + y je:"
    print x + y
elif operacija == "-":
    print "Razlika x - y je:"
    print x - y
elif operacija == "*":
    print "Umnozak x * y je:"
    print x * y
elif operacija == "/":
    print "Kvocijent x / y je:"
    print x / y
else:
    print "Niste odabrali valjanu operaciju."