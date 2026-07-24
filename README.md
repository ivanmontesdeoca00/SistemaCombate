# ⚔️ Sistema de Combate RPG en Python
Un sistema de combate interactivo por consola (CLI) desarrollado íntegramente en Python. Este proyecto simula la creación, gestión y enfrentamiento de personajes estilo RPG, aplicando sólidos conceptos de **Programación Orientada a Objetos (POO)**.

##  Características Principales

-  **Creación de Personajes:** Permite crear personajes asignando nombre, clase (`Warrior`, `Mage`, `Archer`), puntos de vida, ataque base y una contraseña de seguridad.
-  **Sistema de Autenticación (Login):** Acceso seguro al menú de acciones de cada personaje mediante validación de contraseña con límite de intentos.
-  **Mecánicas de Combate Dinámicas:** Sistema de cálculo de daño (aislamiento de lógica) con variaciones según la clase. Por ejemplo, los magos consumen maná y tienen bonificaciones de daño.
-  **Diccionario de Guerra:** Un registro en tiempo real (Log) que guarda el historial de ataques y estadísticas de la sesión de juego, demostrando el uso eficiente de diccionarios.
-  **Interfaz de Menú Interactiva:** Navegación fluida a través de la terminal usando bucles y control de estados (manejo de sesión de usuario).

## Arquitectura del Proyecto

El proyecto sigue un diseño modular para separar las responsabilidades, facilitando la escalabilidad y la lectura del código:

- `main.py`: Punto de entrada de la aplicación.
- `menu.py`: Gestiona la interfaz de usuario en la terminal, los menús de creación/login, el estado de la sesión y el historial de batallas.
- `personaje.py`: Define el modelo de datos de los jugadores, integrando composición de clases.
- `sistema.py`: Contiene la lógica de negocio pura, cálculo de daño mediante métodos estáticos (`@staticmethod`), manejo de atributos y el sistema de seguridad.

##  Instalación y Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/SistemaCombate.git
   ```
2. Navegar al directorio del proyecto:
   ```bash
   cd SistemaCombate
   ```
3. Ejecutar el script principal:
   ```bash
   python main.py
   ```

##  Aprendizajes y Habilidades Aplicadas

- **POO:** Clases, objetos, métodos estáticos, instanciación y composición.
- **Estructuras de Datos:** Manejo de diccionarios para simular una base de datos local en memoria y registros temporales.
- **Control de Flujo y Errores:** Manejo de excepciones (`try-except`) para validación de inputs de usuario, bucles `while` y condicionales lógicos anidados.
- **Modularidad:** Importación de módulos propios y separación estricta de responsabilidades.

##  Próximas Mejoras (Roadmap)

- [ ] Implementar base de datos SQLite o archivos JSON para persistencia de los personajes tras cerrar el programa.
- [ ] Agregar sistema de niveles y puntos de experiencia (XP).
- [ ] Incorporar inventario y objetos consumibles (Pociones de vida/maná).

---
*Desarrollado con ☕ y 🐍 por Ivan K. Montes de Oca || https://www.linkedin.com/in/iv%C3%A1n-kevin-montes-de-oca-74986a24b/ *


<img width="468" height="163" alt="image" src="https://github.com/user-attachments/assets/e31c819a-7162-4564-8d8e-f797fb633a56" />
<img width="464" height="192" alt="image" src="https://github.com/user-attachments/assets/ec6218ff-eae9-4ffb-9540-2b6e6359efa0" />
<img width="388" height="355" alt="image" src="https://github.com/user-attachments/assets/2116f661-87a7-40cc-b5f7-b2353aad6a1c" />
<img width="458" height="207" alt="image" src="https://github.com/user-attachments/assets/302f518e-3bab-4e32-921e-6b5253df0a3d" />
<img width="609" height="58" alt="image" src="https://github.com/user-attachments/assets/6894c06f-942b-4ec0-846b-895f88def39b" />
