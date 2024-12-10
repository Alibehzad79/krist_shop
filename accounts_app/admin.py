from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts_app.models import CustomUser, UserProfile, Address

# Register your models here.


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number")
    inlines = [AddressInline]
