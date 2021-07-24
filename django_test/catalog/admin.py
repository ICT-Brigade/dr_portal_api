from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from . import models


DEFAULT_LIST_COLS = ("id", "created_at",)


@admin.register(models.Token)
class TokenAdmin(admin.ModelAdmin):
	list_display = DEFAULT_LIST_COLS + ("type", 'value')


@admin.register(models.TokenType)
class TokenTypeAdmin(admin.ModelAdmin):
	list_display = DEFAULT_LIST_COLS + ('value',)


@admin.register(models.CampaignType)
class CampaignTypeAdmin(admin.ModelAdmin):
	list_display = DEFAULT_LIST_COLS


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = DEFAULT_LIST_COLS + ("description", "link",)


@admin.register(models.Setting)
class SettingAdmin(admin.ModelAdmin):
	list_display = ("key", "value",)
