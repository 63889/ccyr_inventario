from django.db import models

class Plantel(models.Model):
    id_plantel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=140)
    correo = models.TextField()
    contraseña = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    id_plantel = models.ForeignKey(
        Plantel,
        on_delete=models.CASCADE
    )
class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    id_plantel = models.ForeignKey(Plantel, on_delete=models.CASCADE)

class Registro(models.Model):
    id_registro = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(
        auto_now_add=True
    )
    id_departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE
    )
    id_plantel = models.ForeignKey(
        Plantel,
        on_delete=models.CASCADE
    )
    tipo = models.CharField(max_length=200)
    nota = models.CharField(max_length=200)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    modelo = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    no_serie = models.CharField(max_length=200)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    id_plantel = models.ForeignKey(Plantel, on_delete=models.CASCADE)

class Pedidos(models.Model):
    id_pedido=models.AutoField(primary_key=True,unique=True)
    fecha=models.DateTimeField()
    descripcion=models.CharField(max_length=200)
    id_plantel=models.ForeignKey(Plantel, on_delete=models.CASCADE)

class Detalle_Pedidos(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True),
    id_pedido = models.ForeignKey(
        Pedidos,
        on_delete=models.CASCADE
    )
    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )
    cantidad = models.IntegerField()

class registro_producto(models.Model):
    id_rp = models.AutoField(primary_key=True, unique=True)
    id_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()







    