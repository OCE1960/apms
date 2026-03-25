from django.contrib import admin

class RoleAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_at"
    empty_value_display = "--"
    list_display = ["name", "display_name", "created_at", "updated_at"]