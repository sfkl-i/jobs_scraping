from django.contrib import admin

from .models import City, ProgrammingLanguage, Vacancy

admin.site.register(City)
admin.site.register(ProgrammingLanguage)
admin.site.register(Vacancy)