from django.db import models
from django.utils.translation import gettext as _

from django.db import models
from uuid import uuid4
from django.utils.translation import gettext as _


# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(_("id"), editable=False, primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class DatetimeMixin:
    create_at = models.DateTimeField(_("Created at"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("Updated at"), auto_now=True, auto_now_add=False

                                     )
class User(models.Model):
    username = models.CharField(_("Username"), max_length=50)
    image = models.ImageField(_("Profile Image"), upload_to='image')
    bio = models.TextField(_("Bio"))

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username


class Comment(models.Model):
    text = models.TextField(_("Comment"))
    time = models.DateField(_("Timestamp"), auto_now=False, auto_now_add=True)
    post_id = models.ForeignKey("core.Post", verbose_name=_(""), on_delete=models.CASCADE)
    user_id = models.ForeignKey("core.User", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.text


class Post(models.Model):
    text = models.TextField(_("Text"))
    publish_date = models.DateField(_("Publish date"), auto_now=False, auto_now_add=True)
    update_date = models.DateField(_("Update Date"), auto_now=True, auto_now_add=False)
    tag = models.CharField(_("Tags"), max_length=50)
    user_id = models.ForeignKey("core.User", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.text


class Like(models.Model):
    user_id = models.ForeignKey("core.User", verbose_name=_(""), on_delete=models.CASCADE)
    post_id = models.ForeignKey("core.Post", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return self.user_id


class DisLike(models.Model):
    user_id = models.ForeignKey("core.User", verbose_name=_(""), on_delete=models.CASCADE)
    post_id = models.ForeignKey("core.Post", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("DisLike")
        verbose_name_plural = _("DisLikes")

    def __str__(self):
        return self.user_id


class Follower(models.Model):
    user_id = models.ForeignKey("core.User", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Follower")
        verbose_name_plural = _("Followers")

    def __str__(self):
        return self.user_id


class Friend(models.Model):
    user_id = models.ForeignKey("core.User", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Friend")
        verbose_name_plural = _("Friends")

    def __str__(self):
        return self.user_id


class Archive(models.Model):
    post_id = models.ForeignKey("core.Post", verbose_name=_(""), on_delete=models.CASCADE)
    user_id = models.ForeignKey("core.User", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Archive")
        verbose_name_plural = _("Archives")

    def __str__(self):
        return self.post_id

# Create your models here.
