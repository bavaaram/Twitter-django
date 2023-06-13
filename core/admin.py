from django.contrib import admin
from models import Post, User, Comment, Like, DisLike, Archieve, Follower, Friend

class UserImageInline(admin.TabularInline):
    model = User
    extra = 1


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'post']
    search_fields = ['username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

@admin.register(DisLike)
class DisLikeAdmin(admin.ModelAdmin):
    pass

# Register your models here.
