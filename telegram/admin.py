from django.contrib import admin

from telegram.models import TelegramChat, TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TelegramChat)
class TelegramChatAdmin(admin.ModelAdmin):
    pass
