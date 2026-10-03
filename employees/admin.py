from django.contrib import admin
from .models import Department,Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display=["id","full_name","email","designation","salary","joining_date","is_active","manager"]
    # this cls shoulb be passed to regiester admin
    list_filter = ["manager"]
    search_fields = ["full_name","email"]
    list_editable = ["is_active","salary"]
    list_display_links = ["full_name","email"]
    ordering = ["id"]  # for descending order -> ["-id"]

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)

