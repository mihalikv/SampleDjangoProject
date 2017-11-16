from django.contrib import admin

# Register your models here.
from news.models import Events, News


class EventsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Events, EventsAdmin)
admin.site.register(News, EventsAdmin)
