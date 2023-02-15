def kilogramo_a_libra(kg):
   lb = kg * 2.204
   return lb
def libra_a_kilogramo(lb):
    kg = lb / 2.204
    return kg

def menu():
   print("1. pasar de kilogramos a libras")
   print("2. pasar de libras a kilogramos")
   opcion = input("-->")
   return opcion

op = menu()
if op == "kilogramos":
   kgrs = float(input("introduce kilogramos: "))
   conversion = kilogramo_a_libra(kgrs)
   print("son:", conversion, "libras")
elif op == "libras":
   lbs = float(input("introduce libras "))
   conversion = libra_a_kilogramo(lbs)
   print("son: ", conversion, "kilogramos")