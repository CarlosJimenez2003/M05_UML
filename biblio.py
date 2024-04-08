# Definició de la classe Categoria que representa una categoria de llibre
class Categoria:
    def __init__(self, tipus, definicio):
        self.tipus = tipus          # Tipus de categoria
        self.definicio = definicio  # Definicio de la categoria


# Definició de la classe Prestec que representa un préstec de llibre
class Prestec:
    def __init__(self, data_inici, data_fi, nom_llibre, nom_lector):
        self.data_inici = data_inici  # Data d'inici del préstec
        self.data_fi = data_fi        # Data de finalització del préstec
        self.nom_llibre = nom_llibre  # Nom del llibre prestat
        self.nom_lector = nom_lector  # Nom del lector que ha realitzat el préstec


# Definició de la classe Llibre que representa un llibre de la biblioteca
class Llibre:
    def __init__(self, titol, any, categoria, autor, editorial):
        self.titol = titol          # Títol del llibre
        self.any = any              # Any de publicació del llibre
        self.categoria = categoria  # Categoria del llibre (objecte de la classe Categoria)
        self.autor = autor          # Autor del llibre (objecte de la classe Autor)
        self.editorial = editorial  # Editorial del llibre (objecte de la classe Editorial)


# Definició de la classe Autor que representa un autor de llibres
class Autor:
    def __init__(self, nom, data_naixement):
        self.nom = nom              # Nom de l'autor
        self.data_naixement = data_naixement  # Data de naixement de l'autor


# Definició de la classe Copia que representa una còpia específica d'un llibre
class Copia:
    def __init__(self, codi_copia, ubicacio):
        self.codi_copia = codi_copia  # Codi identificador de la còpia
        self.ubicacio = ubicacio      # Ubicació física de la còpia a la biblioteca


# Definició de la classe Multa que representa una multa associada a un préstec
class Multa:
    def __init__(self, data_inici, data_finalitzacio):
        self.data_inici = data_inici              # Data d'inici de la multa
        self.data_finalitzacio = data_finalitzacio  # Data de finalització de la multa


# Definició de la classe Editorial que representa una editorial
class Editorial:
    def __init__(self, nom, nacionalitat):
        self.nom = nom                    # Nom de la editorial
        self.nacionalitat = nacionalitat  # Nacionalitat de la editorial


# Definició de la classe Lector que representa una persona que llegeix llibres
class Lector:
    def __init__(self, nom, cognoms, dni, adreca):
        self.nom = nom              # Nom del lector
        self.cognoms = cognoms      # Cognoms del lector
        self.dni = dni              # DNI del lector
        self.adreca = adreca        # Adreça del lector
