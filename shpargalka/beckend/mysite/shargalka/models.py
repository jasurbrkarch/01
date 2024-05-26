from django.db import models

class Shargalka(models.Model):

    savol = models.CharField('savol',max_length=200)
    javob = models.CharField('javob',max_length=200)
