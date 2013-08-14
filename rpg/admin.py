from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from models import Title, Guild, Level
from django.contrib.auth.forms import UserChangeForm


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()


User = get_user_model()


class HeroAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ("avatar", 'exp', 'credits', "titles", "guilds")}),
    )


class TitleAdmin(admin.ModelAdmin):
    class Meta():
        model = Title
    fields = ("name", )


class GuildAdmin(admin.ModelAdmin):
    class Meta():
        model = Guild
    fields = ("name", )


class LevelAdmin(admin.ModelAdmin):
    class Meta():
        model = Level
    fields = ("exp", )

admin.site.register(User, HeroAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Guild, GuildAdmin)
admin.site.register(Level, LevelAdmin)
