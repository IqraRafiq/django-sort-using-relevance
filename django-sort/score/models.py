from django.db import models
from score.ScoreManager import WithScoreManager
class Products(models.Model):
    
    objects = WithScoreManager()
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

        
