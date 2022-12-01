from django.contrib import admin
from topper.models import InsertSymbols
# Register your models here.

@admin.register(InsertSymbols)
class AdminInsertSymbols(admin.ModelAdmin):
    list_display = ['symbol','exchange']

