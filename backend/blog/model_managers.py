from django_extensions.db.models import ActivatorQuerySet, ActivatorModelManager

"""
Used django-extension model manager style 
"""


class CommentQuerySet(ActivatorQuerySet):
    """
    Inheritance from ActivatorQuerySet to add :

    approved: returns the approved comments

    unapproved: returns the unapproved comments
    """

    def approved(self):
        return self.filter(approved=True)

    def unapproved(self):
        return self.filter(approved=False)


class CommentManager(ActivatorModelManager):
    """
    approved: return approved comments

    unapproved: return unapproved comments
    """

    def get_queryset(self):
        return CommentQuerySet(model=self.model, using=self._db)

    def approved(self):
        return self.get_queryset().approved()

    def unapproved(self):
        return self.get_queryset().unapproved()
