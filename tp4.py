import subprocess


### Patrón Proxy ###
class Ping:
    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)
                print(result.stdout.decode('utf-8'))
        else:
            print("Dirección IP no válida para ping.")

    def executefree(self, ip_address):
        for _ in range(10):
            result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)
            print(result.stdout.decode('utf-8'))

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

### Patrón Bridge ###
class Lamina:
    def __init__(self, espesor, ancho, tren_laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir(self):
        return self.tren_laminador.producir(self)

class TrenLaminador:
    def producir(self, lamina):
        pass

class TrenLaminador5m(TrenLaminador):
    def producir(self, lamina):
        print(f"Lámina de {lamina.espesor}\" de espesor y {lamina.ancho} metros de ancho producida en tren de 5m.")

class TrenLaminador10m(TrenLaminador):
    def producir(self, lamina):
        print(f"Lámina de {lamina.espesor}\" de espesor y {lamina.ancho} metros de ancho producida en tren de 10m.")

### Patrón Composite ###
class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel):
        pass

class Producto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Producto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

### Patrón Decorator ###
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print(f"Valor: {self.valor}")

class OperacionDecorator:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        self.numero.imprimir()

class Sumar(OperacionDecorator):
    def imprimir(self):
        self.numero.valor += 2
        super().imprimir()

class Multiplicar(OperacionDecorator):
    def imprimir(self):
        self.numero.valor *= 2
        super().imprimir()

class Dividir(OperacionDecorator):
    def imprimir(self):
        self.numero.valor /= 3
        super().imprimir()

# Uso de los patrones
# 1. Patrón Proxy
proxy = PingProxy()
proxy.execute("192.168.0.1")  # Realiza ping a la dirección IP
proxy.execute("8.8.8.8")        # Realiza ping a otra dirección IP
proxy.execute("192.168.0.254")  # Realiza ping a www.google.com a través de executefree

# 2. Patrón Bridge
lamina_5m = Lamina(0.5, 1.5, TrenLaminador5m())
lamina_5m.producir()

lamina_10m = Lamina(0.5, 1.5, TrenLaminador10m())
lamina_10m.producir()

# 3. Patrón Composite
producto_principal = Producto("Producto Principal")

subconjunto1 = Producto("Subconjunto 1")
subconjunto2 = Producto("Subconjunto 2")
subconjunto3 = Producto("Subconjunto 3")

for i in range(4):
    subconjunto1.agregar(Componente(f"Pieza {i+1}"))
    subconjunto2.agregar(Componente(f"Pieza {i+1}"))
    subconjunto3.agregar(Componente(f"Pieza {i+1}"))

producto_principal.agregar(subconjunto1)
producto_principal.agregar(subconjunto2)
producto_principal.agregar(subconjunto3)

producto_principal.mostrar()

# 4. Patrón Decorator
numero = Numero(5)
numero.imprimir()

numero_suma = Sumar(numero)
numero_suma.imprimir()

numero_multi = Multiplicar(numero_suma)
numero_multi.imprimir()

numero_div = Dividir(numero_multi)
numero_div.imprimir()

"""
5. Utilidad del Patrón Flyweight
El patrón Flyweight se utiliza cuando se necesita manejar una gran cantidad de objetos
que comparten ciertas propiedades para reducir el uso de memoria y mejorar el rendimiento.
Un ejemplo de situación donde podría ser útil este patrón es en un editor de texto donde se necesitan representar una gran cantidad de caracteres.

En un editor de texto, cada carácter individual puede ser considerado como un objeto. 
Sin embargo, muchos caracteres, como letras y números, se repiten frecuentemente a lo largo del texto.
En lugar de crear un objeto separado para cada instancia de un carácter, 
se puede utilizar el patrón Flyweight para compartir instancias de objetos para los caracteres que son iguales.

Esto puede reducir significativamente el uso de memoria, ya que en lugar de tener miles de objetos de caracteres diferentes,
solo se necesitarían unos pocos objetos para representar todos los caracteres posibles. Además, al compartir instancias de objetos, 
también se puede mejorar el rendimiento, ya que se evita la sobrecarga de crear y destruir una gran cantidad de objetos.

"""