from django.db import models
from django.db.models.base import Model


class GenomeSequence(models.Model):
    genomeSequence = models.TextField(max_length=999999999)