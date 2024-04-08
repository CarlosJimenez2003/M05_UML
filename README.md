# M05_UML
M05_UML Carlos Jiménez Viso 
![alt text](image.png)

Classes Python: Cada classe UML s'ha convertit en una classe Python amb els seus respectius atributs i mètodes. Les classes es mantenen bastant semblants a la descripció en UML, amb cada atribut representat com una variable d'instància i cada mètode representat com una funció dins de la classe.

Relacions entre classes: Les relacions entre classes, com associacions, composicions i agregacions, s'han implementat a través dels atributs de les classes. Per exemple, a la classe Factura, l'atribut client és una instància de la classe Client, representant la relació d'associació entre Factura i Client.

Ús de datetime: S'ha importat el mòdul datetime per treballar amb dates i hores.

Instàncies de classes: S'han creat instàncies de les classes amb valors específics pels atributs, seguint la lògica del model UML.

La conversió del diagrama UML a Python implica traduir les entitats i relacions del diagrama en classes i atributs en Python, mantenint la lògica i les relacions definides en el model UML.


**Biblioteca**
![image](https://github.com/CarlosJimenez2003/Biblioteca/assets/145457166/a2bd2f7f-4d83-4148-98fb-98be68bbc885)

La classe **Categoria** defineix les categories en les quals es poden classificar els llibres, amb atributs com tipus i descripció. 
Això facilita l'organització i recerca de llibres per temes. 

**Prestec** s'encarrega dels préstecs de llibres, enregistrant la data d'inici i de devolució, així com els noms del llibre prestat i del lector. 
Això ajuda a controlar quins llibres estan en préstec i a qui s'han prestat. 

**Llibre** modela els llibres a la biblioteca, incloent detalls com el títol, any de publicació, categoria, autor i editorial. 
Aquesta classe permet emmagatzemar informació completa sobre cada llibre i facilita la seva gestió i recerca. 

**Autor** representa els autors dels llibres, amb atributs com nom i data de naixement. 
Això permet mantenir un registre dels creadors dels llibres i obtenir informació sobre ells. 

**Copia** gestiona còpies específiques de llibres a la biblioteca, identificades per un codi únic i una ubicació física. 
Això facilita el seguiment de cada exemplar d'un llibre i la seva disponibilitat per préstec. 

**Multa** registra les multes associades als préstecs de llibres, indicant la data d'inici i de finalització de la mateixa. 
Això ajuda a controlar i gestionar les sancions per retard en la devolució de llibres. 

**Editorial** representa les editorials de llibres, amb atributs com nom i nacionalitat. 
Això proporciona informació sobre les entitats que publiquen els llibres de la biblioteca. 

**Lector** modela les persones que utilitzen la biblioteca, registrant detalls com nom, cognoms, DNI i adreça. 
Això permet mantenir un registre dels usuaris i gestionar la seva interacció amb la biblioteca.
