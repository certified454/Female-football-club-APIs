from django.contrib import admin
from .models import JoinForm, SportGallery, Team, Fixtures, News
# Register your models here.


class JoinFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


class FixturesAdmin(admin.ModelAdmin):
    list_display = ('venue', 'kickoff', 'date_schedule')


admin.site.register(JoinForm, JoinFormAdmin)
admin.site.register(Team)
admin.site.register(SportGallery)
admin.site.register(Fixtures, FixturesAdmin)
admin.site.register(News)
