from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from rest_framework.viewsets import ReadOnlyModelViewSet

from news.models import NewsSerializer, EventsSerializer, Events, News


class EventsApiView(ReadOnlyModelViewSet):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()


class NewsApiView(ReadOnlyModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class IndexView(TemplateView):
    template_name = "index.html"