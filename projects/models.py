from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to='projects')
    link = models.URLField(
        verbose_name="Url mas informacion", null=True, blank=True)

    # Fecha de creacion
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado")

    # Fecha de actualizacion
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Ultima actualizacion")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

        ordering = ['-created']  # Lo ordena de manera descendente

    def __str__(self):
        return self.title
