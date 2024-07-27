from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
)

from .model_managers import CommentManager


class Post(
    TitleDescriptionModel,
    TimeStampedModel,
    ActivatorModel,
):
    author = models.OneToOneField(to="auth.User", on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/", null=True, blank=True)


class Comment(
    TitleDescriptionModel,
    TimeStampedModel,
    ActivatorModel,
):
    approved = models.BooleanField(default=False)
    auther = models.ForeignKey(to="auth.User", on_delete=models.CASCADE)
    posts = models.ForeignKey(
        to=Post, related_name="comments", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    objects = CommentManager()


class Category(
    TitleDescriptionModel,
    ActivatorModel,
):
    posts = models.ManyToManyField(to=Post, related_name="categories")
    parent = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    class Meta:
        ordering = ("title",)


class Tag(TitleSlugDescriptionModel):
    posts = models.ManyToManyField(to=Post, related_name="Tags")

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
