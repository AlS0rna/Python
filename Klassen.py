class MyClass:
    zahl=42
    string ="Zeichenkette"

    #Konstruktor
    def __init__(self,new_buch="a"): #default wert wird 
        self.buchstabe=new_buch

    def funk(self, neuezahl):
        self.zahl=neuezahl 



instanz=MyClass("b")
instanz2=MyClass("c")

instanz.funk(1337) # => funk(instanz;1337)



print(str(instanz.zahl) + str(instanz.buchstabe) + str(instanz.string))
print(str(instanz2.zahl) + str(instanz2.buchstabe) + str(instanz2.string))
