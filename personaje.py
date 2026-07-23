from sistema import Atributos, Contrasena

class Personaje:
    def __init__(self, nombre, clase_personaje, vida_maxima, ataque_base, clave_secreta):
        self.nombre = nombre
        self.clase_personaje = clase_personaje.lower()
        # aca creo que el personaje "Tenga" atributos y una constraseña
        self.atributos = Atributos(vida_maxima, ataque_base)
        self.contrasena = Contrasena(clave_secreta)