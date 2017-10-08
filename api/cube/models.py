from django.db import models
from django.utils.translation import ugettext as _


class Cube(models.Model):
    """Cube model

    Attributes:
        dimension = Dimension of the cube
        matrix = Status current of the matrix 3D
        created_at = Is the date when the object is created.
            (Note: Automatically generated when the object is created.).
        updated_at = Is the date when the object is updated (Note: Automatically created).
            (Note: Automatically generated when the object is updated.).
    """
    dimension = models.IntegerField(verbose_name=_('dimension'))
    matrix = models.TextField(verbose_name=_('matrix'))
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('cube')
        verbose_name_plural = _('cubes')

    def __str__(self):
        return self.name
