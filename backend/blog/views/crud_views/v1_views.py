from django.db.models.fields.files import FieldFile
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views import View
from ...models import Post

"""

Django CRUD API

"""


def serialize_post(post: Post):
    post_dict = model_to_dict(post)
    for field in post._meta.fields:
        if isinstance(getattr(post, field.name), FieldFile):
            post_dict[field.name] = getattr(post, field.name).url if getattr(post, field.name) else None
    return post_dict


class CrudPostView(View):
    def get(self, request, *args, **kwargs):
        """
        If the pk has given returns only one object (DetailView)
        else returns all objects
        """
        pk = self.kwargs.get("pk")
        if not pk:
            query = Post.objects.all()
            data = {}
            for obj in query:
                obj_dict = serialize_post(obj)
                data[f'post_{obj.id}'] = obj_dict
            return JsonResponse(data)
        obj = Post.objects.get(pk=pk)
        obj_dict = serialize_post(obj)
        return JsonResponse(obj_dict)


    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def patch(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
