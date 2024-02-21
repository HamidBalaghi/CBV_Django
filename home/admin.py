from django.contrib import admin
from .models import Person
from .forms import PersonAdminForm


# Register your models here.


# admin.site.register(Person)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')
    form = PersonAdminForm
