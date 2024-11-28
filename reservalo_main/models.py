from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model 

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)  # Automatically set on creation.

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


# Modelo para Bicicletas
class Bicicleta(models.Model):
    TIPOS = [
        ('MTB', 'Mountain Bike'),
        ('URB', 'Urbana'),
        ('LTC', 'Electrica'),
        ('KID', 'Infantil'),
    ]
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('reservada', 'Reservada'),
        ('en reparacion', 'En reparación'),
    ]

    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=4, choices=TIPOS)
    color = models.CharField(max_length=20)
    tamanio = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='disponible')
    imagen = models.CharField(max_length=500,default="https://th.bing.com/th/id/OIP.8mLUw63EOxbQI8r_7SgRIQHaHa?w=193&h=192&c=7&r=0&o=5&dpr=1.3&pid=1.7")

    def __str__(self):
        return f"{self.modelo} ({self.tipo})"

# Modelo para Reservas
class Reserva(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='reservas')
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.RESTRICT, related_name='reservas')

    def __str__(self):
        return f"Reserva de {self.usuario} - {self.bicicleta}"

# Modelo para Pagos
class Pago(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField()
    reserva = models.ForeignKey(Reserva, on_delete=models.RESTRICT, related_name='pagos')
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='pagos')

    def __str__(self):
        return f"Pago de {self.usuario} por {self.monto}"

# Modelo para Inventario
class Inventario(models.Model):
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.RESTRICT, related_name='inventario')

    def __str__(self):
        return f"Inventario de {self.bicicleta}"

class Perfil(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')

    def __str__(self):
        return self.user.username
    
class Orden(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)

