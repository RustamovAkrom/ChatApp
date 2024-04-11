from django.contrib import admin
from .models import User, UserProfile, UserAvatars, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'id']


@admin.register(UserAvatars)
class UserAvatarsAdmin(admin.ModelAdmin):
    list_display = ['avatar', 'id']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['video', 'descriptions', 'id']