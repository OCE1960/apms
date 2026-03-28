from django.contrib import admin

from apms import models

class RoleUserInline(admin.TabularInline):
    model = models.RoleUser
    extra = 1
