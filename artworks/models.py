from django.db import models


class Artwork(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to='artworks')
    price = models.FloatField(verbose_name="Precio")

    # Fecha de creacion
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado")

    # Fecha de actualizacion
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Ultima actualizacion")

    class Meta:
        verbose_name = "Artwork"
        verbose_name_plural = "Artworks"

        ordering = ['-created']  # Lo ordena de manera descendente

    def __str__(self):
        return self.title


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    email = models.EmailField(verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    address = models.CharField(max_length=200, verbose_name="Calle y Numero",
                               help_text='<span class="font-italic" style="font-size: 0.9rem">Nombre de la calle y numero</span>')
    suburb = models.CharField(max_length=200, verbose_name="Colonia o Fraccionamiento",
                              help_text='<span class="font-italic" style="font-size: 0.9rem">Nombre de la colonia o fraccionamiento</span>')
    total = models.DecimalField(verbose_name="Total", max_digits=50, decimal_places=10,
                                help_text='<span class="text-danger" style="font-size: 0.9rem">Cantidad a pagar por su pedido</span>')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)
