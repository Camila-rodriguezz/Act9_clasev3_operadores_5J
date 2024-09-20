print("Act 9 clases v2")
print("Camila Rodriguez Mat: 22308051281300")
# zona de class
class Operadores1300:
    # zona de funciones
    def suma1300(self,C,R):
        s1300=C+R
        print(f"La suma de {C} + {R} = {s1300}")
    def resta1300(self,C,R):
        r1300=C-R
        print(f"La resta de {C} - {R} = {r1300}")
    def multi1300(self,C,R):
        m1300=C*R
        print(f"La multiplicacion de {C} * {R} = {m1300}")
    def div1300(self,C,R):
        d1300=C/R
        print(f"La division de {C} / {R} = {d1300}") 
    def modulo1300(self,C,R):
        mod1300=C%R
        print(f"El modulo de {C} % {R} = {mod1300}")
    def expon1300(self,C,R):
        e1300=C**R
        print(f"El exponente de {C} ** {R} = {e1300}")
    def cociente1300(self,C,R):
        c1300=C//R
        print(f"El cociente de {C} // {R} = {c1300}")
        
# zona de creacion del objeto
operarodriguez=Operadores1300()

# zona de uso de objetos
print("Funcion suma")
operarodriguez.suma1300(5,4)
print("\nFuncion resta")
operarodriguez.resta1300(10,3)
print("\nFuncion multiplicacion")
operarodriguez.multi1300(2,6)
print("\nFuncion division")
operarodriguez.div1300(15,5)
print("\nFuncion modulo")
operarodriguez.modulo1300(5,2)
print("\nFuncion exponente")
operarodriguez.expon1300(7,2)
print("\nFuncion cociente")
operarodriguez.cociente1300(13,2)