from typing import List  # Importa List des de typing per a tipar les llistes
from datetime import datetime # Importa datetime per a treballar amb dates

class Client: # Classe que representa un client
    def __init__(self, id: int, nom: str, adreça: str, telèfon: str, correuElectrònic: str):
         # Constructor de la classe, inicialitza els atributs de la classe
        self.id = id #Identificador del client
        self.nom = nom #Nom del client
        self.adreça = adreça #Adreça del client
        self.telèfon = telèfon #Telefon del client
        self.correuElectrònic = correuElectrònic #Correu del client

class UsuariWeb: # Classe que representa un usuari web
    def __init__(self, id: int, login: str, contrasenya: str, estat: str):
        self.id = id # Identificador de l'usuari web
        self.login = login # Nom d'inici de sessió de l'usuari web
        self.contrasenya = contrasenya # Contrasenya de l'usuari web
        self.estat = estat # Estat de l'usuari web

class PaymentAccount: #Classe que representca un usuari web
    def __init__(self, id: int, client: Client):
        self.id = id # Identificador del compte de pagament
        self.client = client  # Client associat al compte de pagament

class Producte: # Classe que representa un producte
    def __init__(self, id: int, codi: str, nom: str, proveïdor: str):
        self.id = id # Identificador del producte
        self.codi = codi # Codi del producte
        self.nom = nom # Nom del producte
        self.proveïdor = proveïdor #Nom del proveïdor

class CartCompra: # Classe que representa un carret de compra
    def __init__(self, id: int, producte: Producte, quantitat: int, preu: float):
        self.id = id # Identificador del carret de compra
        self.producte = producte # Producte del carret de compra
        self.quantitat = quantitat # Quantitat del producte al carret
        self.preu = preu # Preu total dels productes al carret

class ShoppingCart:
    def __init__(self, id: int, UsuariWeb: UsuariWeb):
        self.id = id
        self.UsuariWeb = UsuariWeb  # Usuari web associat al carret de compra
        self.ítems: List[CartCompra] = [] # Llista d'ítems de compra al carret

class Pagament:
    def __init__(self, id: int, import_: float):
        self.id = id # Identificador del pagament
        self.import_ = import_ # Import del pagament

class Factura:
    def __init__(self, id: int, client: Client, adreçaFacturació: str, dataEmisió: datetime, dataTancament: datetime, pagament: Pagament):
        self.id = id  # Identificador de la factura
        self.client = client # Client associat a la factura
        self.adreçaFacturació = adreçaFacturació # Adreça de facturació
        self.dataEmisió = dataEmisió # Data d'emissió de la factura
        self.dataTancament = dataTancament # Data de tancament de la factura
        self.pagament = pagament # Pagament associat a la factura
        self.comandes: List[Comanda] = [] # Llista de comandes associades a la factura

class Comanda:
    def __init__(self, id: int, factura: Factura, dataComanda: datetime, dataEnviament: datetime, destinació: str, import_: float, estat: str):
        self.id = id # Identificador de la comanda
        self.factura = factura # Factura associada a la comanda
        self.dataComanda = dataComanda # Data de la comanda
        self.dataEnviament = dataEnviament # Data d'enviament de la comanda
        self.destinació = destinació # Destinació de la comanda
        self.import_ = import_ # Import de la comanda
        self.estat = estat # Estat de la comanda

# Asociaciones
# Creació d'una instància de la classe Client amb les dades especificades
client = Client(1, "Nombre", "Dirección", "Teléfono", "correo@example.com")

# Creació d'una instància de la classe UsuariWeb amb les dades especificades
usuari_web = UsuariWeb(1, "login", "contraseña", "activo")

# Creació d'una instància de la classe PaymentAccount amb un client associat
payment_account = PaymentAccount(1, client)

# Creació d'una instància de la classe Producte amb les dades especificades
producte = Producte(1, "001", "Producto", "Proveedor")

# Creació d'una instància de la classe CartCompra amb les dades especificades
cart_compra = CartCompra(1, producte, 2, 10.99)

# Creació d'una instància de la classe ShoppingCart amb un usuari web associat
shopping_cart = ShoppingCart(1, usuari_web)

# Afegir el carret de compra a la llista d'ítems del carro de compra
shopping_cart.ítems.append(cart_compra)

# Creació d'una instància de la classe Pagament amb l'import especificat
pagament = Pagament(1, 20.99)

# Creació d'una instància de la classe Factura amb les dades especificades
factura = Factura(1, client, "Dirección de facturación", datetime.now(), datetime.now(), pagament)

# Creació d'una instància de la classe Comanda amb les dades especificades
comanda = Comanda(1, factura, datetime.now(), datetime.now(), "Destino", 20.99, "pendiente")

# Afegir la comanda a la llista de comandes de la factura
factura.comandes.append(comanda)
