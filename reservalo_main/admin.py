from django.contrib import admin
from .models import Usuario, Bicicleta, Reserva, Pago, Inventario
from django.contrib.auth.admin import UserAdmin
from .models import Perfil
from .models import Orden

# Register your models here.
admin.site.register(Usuario,UserAdmin)
admin.site.register(Bicicleta)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(Inventario)
admin.site.register(Perfil)
admin.site.register(Orden)
