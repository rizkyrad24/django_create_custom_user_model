from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserCustom
from django.utils.translation import gettext_lazy as _
# Register your models here.

class UserAdminCustom(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "email", "phone", "password1", "password2"),},
        ),
    )
    list_display = ("username", "email", "phone", "first_name", "last_name", "is_staff")
    search_fields = ("username", "first_name", "last_name", "email", "phone")

admin.site.register(UserCustom, UserAdminCustom)