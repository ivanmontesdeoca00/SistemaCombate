## Aca voy a hacer el sistema interactivo con powershell para que en main.py se pueda correr

from personaje import Personaje
from sistema import Dano

class Menu:
    def __init__(self):
        self.base_datos = {} ##Diccionario para guardar los pjs creados
        self.usuario_actual = None

    def iniciar(self):
        ##Bucle principal del menu
        while True:
            print("\n" + "="*30)
            print("="*30)
            print("1- Crear PJ")
            print("2- Logearte")
            print("3- Salir del sistema")
            opcion = input("Seleccione una opcion del 1 al 3: ").strip()

            if opcion == "1":
                self.menu_creacion()
            elif opcion == "2":
                self.menu_login()
            elif opcion == "3":

                print("Cerrar juego, nos vemos pibe")
                break
            else:
                print("Opcion invalida, escribi de nuevo una opcion del 1 al 3")
    
    def menu_creacion(self):
        print("\n _____ CREACION DEL PERSONAJE ______")
        nombre = input("Ingrese el nombre de su personaje: ").strip()

        
        if nombre in self.base_datos:
            print("Nose puede elegir este nombre porque ya existe")
            return
        
        clase_personaje = input("Clase (war, mage, archer): ").strip().lower()
        if clase_personaje not in ["war" , "mage" , "archer"]:
            print("Clase inexistente, se te asignara war por defecto")
            clase_personaje = "war"
        
        
        try:
            vida = int(input("Puntos de vida maxima: "))
            ataque = int(input("Puntos de ataque base: "))
        except ValueError:
            print("Valores no validos, se te asignara 100 de vida y 10 de ataque por defecto xd")
            vida, ataque = 100, 10
        
        clave_secreta = input("Crea una contraseña para tu personaje: ").strip()

        # Aca voy a hacer las instancias del personaje para guardarlo

        nuevo_personaje = Personaje(nombre, clase_personaje, vida, ataque, clave_secreta)
        self.base_datos[nombre] = nuevo_personaje
        print(f"Personaje {nombre} creado exitosamente!")

    def menu_login(self):
        ##Segundo menu para acceder al iniciar sesion de forma correcta
        print("\n--- LOGIN DE PERSONAJE ---")
        nombre = input("Nombre de personaje: ").strip()
        
        #  aca verifico si existe el pj
        if nombre not in self.base_datos:
            print("El personaje no se encontro en la base de datos")
            return

        personaje_solicitado = self.base_datos[nombre]
        
        # aca se valida la clave si es verdadera o mala
        if personaje_solicitado.seguridad.validar_login():
            
            self.usuario_actual = personaje_solicitado
            
            print(f"Sesion iniciada: {self.usuario_actual.nombre} ({self.usuario_actual.clase_personaje})")

            # paso al menu de acciones
            self.menu_acciones()

    def menu_acciones(self):
        while True:
            print("\n" + "-"*30)
            print(f"Sesion iniciada: {self.usuario_actual.nombre} ({self.usuario_actual.clase_personaje})")
            print(f"Vida: {self.usuario_actual.atributos.vida_actual} - Maná: {self.usuario_actual.atributos.mana_actual}")
            print("-"*30)
            print("1 - Atacar a otro personaje")
            print("2 - Ver todas mis datos")
            print("3 - Cerrar Sesion")

            opcion = input("Elegi una accion del 1 al 3: ").strip()

            if opcion == "1":
                objetivo_nombre = input("Ingrese el nombre de a quién desea atacar: ").strip()
                if objetivo_nombre == self.usuario_actual.nombre:
                    print("No puedes atacarte a ti mismo.")
                elif objetivo_nombre in self.base_datos:
                    defensor = self.base_datos[objetivo_nombre]


                    # aca invocamos la clase Dano pasando las dos instancias
                    from sistema import Dano
                    daño_causado = Dano.calcular_dano(self.usuario_actual, defensor)
                    print(f"\n Le pegaste {daño_causado} de daño a {defensor.nombre}!")
                    print(f"A {defensor.nombre} le quedan {defensor.atributos.vida_actual} de vida")
                else:
                    print("El objetivo no existe pelotudo")
            
            elif opcion == "2":
                atacante = self.usuario_actual.atributos
                print("\n--- TUS ESTADISTICAS DALEEEEEEEEE ---")
                print(f"Clase: {self.usuario_actual.clase_personaje.capitalize()}")

                print(f"Vida Actual/maxima: {atacante.vida_actual}/{atacante.vida_maxima}")
                print(f"Ataque de Base: {atacante.ataque_base}")
                print(f"Mana Actual: {atacante.mana_actual}")
            
            elif opcion == "3":
                self.usuario_actual = None
                print("Secion cerrada bien")
                break
            else:
                print("Opcion no valida boludito de feria")
