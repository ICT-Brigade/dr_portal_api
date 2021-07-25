from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from . import models


DEFAULT_LIST_COLS = ("created_at", "updated_at")


@admin.register(models.Token)
class TokenAdmin(admin.ModelAdmin):
	list_display = ("value", "type",) + DEFAULT_LIST_COLS


@admin.register(models.TokenType)
class TokenTypeAdmin(admin.ModelAdmin):
	list_display = ('value',) + DEFAULT_LIST_COLS


@admin.register(models.CampaignType)
class CampaignTypeAdmin(admin.ModelAdmin):
	list_display = ("value",) + DEFAULT_LIST_COLS


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("id", "description", "link",) + DEFAULT_LIST_COLS


@admin.register(models.Setting)
class SettingAdmin(admin.ModelAdmin):
	list_display = ("key", "value",)
