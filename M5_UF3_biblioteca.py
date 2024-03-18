from datetime import datetime #importem la llibreria datetime


class Categoria: # Definició de la classe Categoria
    def __init__(self, definicio):
        self.definicio = definicio # Inicialitza l'atribut definicio de la categoria

    def get_definicio(self): # Mètode per obtenir la definició de la categoria
        return self.definicio


class Editorial: # Definició de la classe Editorial
    def __init__(self, nom, nacionalitat):
        self.nom = nom # Inicialitza l'atribut nom de l'editorial
        self.nacionalitat = nacionalitat # Inicialitza l'atribut nacionalitat de l'editorial

    def get_nom(self):
        return self.nom # Mètode per obtenir el nom de l'editorial

    def get_nacionalitat(self):
        return self.nacionalitat # Mètode per obtenir la nacionalitat de l'editorial

 
class Autor: # Definició de la classe Autor
    def __init__(self, nom, data_naixement): 
        self.nom = nom # Inicialitza l'atribut nom de l'autor# Inicialitza l'atribut nom de l'autor
        self.data_naixement = data_naixement # Inicialitza l'atribut data_naixement de l'autor

    def get_nom(self):
        return self.nom # Mètode per obtenir el nom de l'autor

    def get_data_naixement(self):
        return self.data_naixement


class Llibre: # Definició de la classe Llibre
    def __init__(self, titol, any):
        self.titol = titol
        self.any = any
        self.categoria = None  # Categoria del llibre
        self.autor = None      # Autor del llibre
        self.editorial = None # Editorial del llibre

    def get_titol(self):
        return self.titol

    def get_any(self):
        return self.any


class Copia: # Definició de la classe Copia
    def __init__(self, codi, ubicacio):
        self.codi = codi
        self.ubicacio = ubicacio

    def get_codi(self):
        return self.codi

    def get_ubicacio(self):
        return self.ubicacio


class Prestec: # Definició de la classe Prestec
    def __init__(self, data_inici, data_final, llibre, lector):
        self.data_inici = data_inici
        self.data_final = data_final
        self.llibre = llibre # Llibre prestat
        self.lector = lector # Lector que fa el préstec

    def get_data_inici(self):
        return self.data_inici

    def get_data_final(self):
        return self.data_final

    def get_llibre(self):
        return self.llibre

    def get_lector(self):
        return self.lector


class Lector: # Definició de la classe Lector
    def __init__(self, nom, cognoms, dni, adreca):
        self.nom = nom
        self.cognoms = cognoms
        self.dni = dni
        self.adreca = adreca
        self.prestecs_actius = [] # Llista de préstecs actius per a aquest lector

    def get_nom(self):
        return self.nom

    def get_cognoms(self):
        return self.cognoms

    def get_dni(self):
        return self.dni

    def get_adreca(self):
        return self.adreca

    def afegir_prestec(self, prestec): # Mètode per afegir un préstec actiu al lector
        if len(self.prestecs_actius) < 3:
            self.prestecs_actius.append(prestec)
        else:
            print("El lector ya tiene 3 préstamos activos.")


class Multa: # Definició de la classe Multa
    def __init__(self, data_inicial, data_final, lector):
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.lector = lector

    def get_data_inicial(self):
        return self.data_inicial

    def get_data_final(self):
        return self.data_final

    def get_lector(self):
        return self.lector
