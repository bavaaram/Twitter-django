from django.contrib import admin
from .models import User, Archive, Relation


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'biography']
    search_fields = ['username']


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    pass
# Register your models here.
