from re import U
from django.contrib import admin
from .models import User
from django.contrib.auth import admin as auth_admin


admin.site.register(User, auth_admin.UserAdmin )
