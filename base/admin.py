from django.contrib import admin
from .models import JoinForm, SportGallery, Team
# Register your models here.


class JoinFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


admin.site.register(JoinForm, JoinFormAdmin)
admin.site.register(Team)
admin.site.register(SportGallery)
