from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.utils.timezone import now
from rest_framework import serializers


class EventAbstractModel(models.Model):
    date = models.DateTimeField(verbose_name="Termin", default=now)
    title = models.CharField(verbose_name="Nadpis", max_length=255)
    description = RichTextField(verbose_name="Popis")

    class Meta:
        abstract = True


class Events(EventAbstractModel):
    class Meta:
        verbose_name = "Udalost"
        verbose_name_plural = "Udalosti"


class News(EventAbstractModel):
    class Meta:
        verbose_name = "Novinka"
        verbose_name_plural = "Novinky"


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
