# main.py

# Importa la clase desde el archivo mi_clase.py
from mi_clase import MiClase
from claseAlumno import Alumno

# Crea una instancia de la clase
mi_objeto = MiClase("Carlos")

# Llama al método de la clase
saludo = mi_objeto.saludar()
print(saludo)

alumno1 = Alumno("Juan", "Pérez", "Gómez", "12345678", 3)

# Obtener valores
print(alumno1.get_nombre())          # Juan
print(alumno1.get_apellido_paterno())  # Pérez
print(alumno1.get_apellido_materno())  # Gómez
print(alumno1.get_no_control())        # 12345678
print(alumno1.get_semestre())          # 3

# Modificar valores
alumno1.set_nombre("Carlos")
alumno1.set_semestre(4)



# Obtener los valores modificados
print(alumno1.get_nombre())          # Carlos
print(alumno1.get_semestre())        # 4
