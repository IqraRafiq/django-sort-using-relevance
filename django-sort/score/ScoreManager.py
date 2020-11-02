from django.db import models
from django.db.models import Func, F

class WithScoreManager(models.Manager):
    def score(self):
        
        class Sin(Func):
            function = 'SIN'
        class Cos(Func):
            function = 'COS'
        class Round(Func):
            function = 'ROUND'
            template='%(function)s(%(expressions)s, 2)'

        radfid = F('id')
        Expression = Round(6.3710 * (Cos(radfid) +  Sin(radfid)))

        return self.get_queryset()\
            .annotate(relevance=Expression).order_by('relevance')