from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

class AdminCustomization(UserAdmin):

    model = User
    list_filter = ("type",)
    list_display = ["email", "type","subject" ]


admin.site.register(User,AdminCustomization)