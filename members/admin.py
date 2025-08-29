
from django.contrib import admin
from .models import Member, Media, Social

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class SocialInline(admin.TabularInline):
    model = Social
    extra = 1

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "title", "email")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "title", "summary", "location", "skills", "goals", "email")
    inlines = [MediaInline, SocialInline]

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("member", "type", "caption")

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("member", "platform", "url")
