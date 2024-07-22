from django_extensions.db.models import ActivatorQuerySet, ActivatorModelManager


class CustomActivatorModelManager(ActivatorModelManager):
    pass


class CommentQuerySet(ActivatorQuerySet):
    pass


class CommentManager(CustomActivatorModelManager):
    pass
