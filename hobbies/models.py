from django.db import models


class Hobby(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to='hobbies')
    video = models.FileField(verbose_name="Video", upload_to='hobbies', max_length=200, null=True, blank=True)
    # link = models.URLField(
    #     verbose_name="Url mas informacion", null=True, blank=True)

    # Fecha de creacion
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado")

    # Fecha de actualizacion
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Ultima actualizacion")

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"

        ordering = ['-created']  # Lo ordena de manera descendente

    def __str__(self):
        return self.title
