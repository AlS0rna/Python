import matplotlib.pyplot as plt
import numpy as np
import Temperatur_umrechnung

def plot():
    x=np.linspace(0, 20, 100)
    plt.plot(x, np.sin(x))
    plt.show()

if __name__ == "__main__":
    
    C=Temperatur_umrechnung.get_temperature()
    print("Das sind " + str(Temperatur_umrechnung.conver_to_kelvin(C)) + " Kelvin")
    