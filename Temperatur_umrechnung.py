#Geg.: Temparatur in Celsius C
#Ges.: Temperatur in Kelvin K
# K=C+273,15

def get_temperature():
    while True:
        C=input("Gib eine Temperatur in Grad Celsius an: ")
        try:
            C=float(C)
            return C
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur.")

def conver_to_kelvin(C):
    K= C + 273.15
    return K

if __name__ == "__main__":
    C=get_temperature()
    print("Das sind " + str(conver_to_kelvin(C)) + " Kelvin")
