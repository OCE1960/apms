from django.contrib import admin

from apms import models
from apms.presentation.forms import admin as app_admin


class APMSAdminSite(admin.AdminSite):
    site_header = "APMS Admin Site"
    site_title = "APMS site admin"
    index_title = "APMS Dashboard"


apms_admin_site = APMSAdminSite(name="admin")
apms_admin_site.register(models.User, app_admin.UserAdmin)
apms_admin_site.register(models.Role, app_admin.RoleAdmin)