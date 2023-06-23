from django.db import models


class Cliente(models.Model):
    rut = models.CharField (max_length=10)
    nombres = models.TextField()
    apellidos = models.TextField()
    telefono = models.TextField()
    celular = models.IntegerField(max_length=9)
    direccion = models.TextField()
    email = models.EmailField()
    ##descripcion = models.ForeignKey(Descripcion, on_delete=models.PROTECT)
    ##nueva = models.BooleanField()


    def __str__(self):
        return self.rut

class Login(models.Model):
    email = models.ForeignKey(Cliente, on_delete=models.PROTECT)



    def __str__(self):
        return self.email

opciones_consultas = [
  [0, "consulta"],
  [1, "reclamo"],
  [2, "sugerencia"],
  [3, "felicitaciones"]
]

class Contacto(models.Model):
  nombres = models.TextField(max_length=80)
  apellidos = models.TextField(max_length=80)
  email = models.EmailField()
  tipo_consulta = models.PositiveSmallIntegerField(choices=opciones_consultas)
  mensaje = models.TextField()
  avisos = models.BooleanField()

  def __str__(self):
    return self.nombres


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    Fecha_cad = models.DateField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre