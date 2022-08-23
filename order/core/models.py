import requests
from django.db import models
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    product_id = models.PositiveIntegerField(_("Product"))
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def get_product(self):
        return requests.get(f"http://localhost:7000/products/{self.product_id}/").json()