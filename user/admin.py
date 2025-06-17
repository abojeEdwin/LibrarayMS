from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Author

# Register your models here.


# admin.site.register(models.User)

@admin.register(Author)
class AuthorAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "first_name", "last_name","email","phone"),
            },
        ),
    )

# admin.site.register(Author)
