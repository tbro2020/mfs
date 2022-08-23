from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(_("name"), max_length=120)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")