from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from . import models


DEFAULT_LIST_COLS = ("id", "created_at", "value")
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = DEFAULT_LIST_COLS

@admin.register(models.Keyword)
class KeywordAdmin(admin.ModelAdmin):
	list_display = DEFAULT_LIST_COLS


@admin.register(models.CampaignType)
class CampaignTypeAdmin(admin.ModelAdmin):
	list_display = DEFAULT_LIST_COLS


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("id", "created_at", "description", "link")
