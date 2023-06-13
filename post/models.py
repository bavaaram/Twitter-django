from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Post(models.Model):
    text = models.TextField(_("post text"))
    publish_at = models.DateTimeField(_("publish at"),
                                      auto_now=False,
                                      auto_now_add=True)
    update_at = models.DateTimeField(_("update at"),
                                     auto_now=True,
                                     auto_now_add=False)
    tag = models.CharField(_("Tag"), max_length=50)
    user_id = models.ForeignKey("user.User",
                                verbose_name=_("User"),
                                on_delete=models.CASCADE)