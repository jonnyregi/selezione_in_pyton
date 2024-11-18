eta=int(input("inserisci la tua età"))
if eta<14:
    costo=10.0
else:
    if eta>65:
        costo=15.0
    else:
        costo=34.0
print("la tua età è", costo ,"euro")