class Atributos:
    def __init__(self, vida_maxima, ataque_base, mana_actual=50):
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima
        self.ataque_base = ataque_base
        self.mana_actual = mana_actual
    
    def recibir_dano(self, cantidad):
        self.vida_actual -= cantidad
    
    def curar(self, cantidad):
        self.vida_actual += cantidad


class Contrasena:
    def __init__(self, clave_secreta):
        self.clave_secreta = clave_secreta
    
    def validar_login(self):
        """Este es el bucle para hacer los intentos de sesion del login"""
    intentos = 3
    while intentos > 0:
        intento = input("Ingrese porfavor la contraseña: ")
        if intento == self.clave_secreta:
            print("Acceso concedido")
            return True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes:", {intentos})
            return False

class Dano:
    @staticmethod ##Lo que hago al agregar este metodo es crear una funcion dentro de la Clase pero que este aislada,
    ##               provocando que no se rompa el resto de las cosas
    def calcular_dano(atacante, defensor):
        """Aca voy a calcular el daño con condicionales anidados segun clases"""
        ##Pato qlo me costo sangre hacer logica de esto
        daño_final = 0
        uno = atacante.clase_personaje
        dos = defensor.clase_personaje
        tres = atacante.atributos
        cuatro = defensor.atributos

        if uno == "war":
            if dos in ["war", "mage", "archer"]:
                daño_final = tres.ataque_base + 5
            else:
                daño_final = tres.ataque_base + 5
        
        elif uno == "mage":
            if tres.mana_actual >= 10:
                tres.mana_actual -= 10
                if dos in ["war", "mage", "archer"]:
                    daño_final = tres.ataque_base * 2
                else:
                    daño_final = tres.ataque_base * 2
                    print(f"[-10 de Mana] {atacante.nombre} realiza magia. Mana restante{tres.mana_actual}")
            else:
                print(f"[Aviso]: {atacante.nombre} no tiene mana. Ataque debil -1000 de aura tambien xd.")
                daño_final = tres.ataque_base // 2
        
        elif uno == "archer":
            if dos in ["war", "mage", "archer"]:
                daño_final = tres.ataque_base
            else:
                daño_final = tres.ataque_base
        
        else:
            daño_final = tres.ataque_base
        
        tres.recibir_dano(daño_final)
        return daño_final
