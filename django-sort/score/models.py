from django.db import models

class Products(models.Model):

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
