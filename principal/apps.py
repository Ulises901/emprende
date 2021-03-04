from django.apps import AppConfig


class producto(AppConfig):
    producto = 'principal'
    def inicialilizar(self,nom):
        self.nombre=nom

    def mostrar(self):
    print("Nombre: ",self.nombre)
precio = float(input("Ingrese precio del producto:$"))
cantidad_utilizada = float(input("Ingrese cantidad utilizada en kg-ml-unidades:"))
cantidad_inicial = float(input("Ingrese cantidad inicial en kg-ml-unidades:"))

producto = total = cantidad_utilizada * 1.00/ cantidad_inicial * precio

print("El total de la inversion de su producto es: $", total)
