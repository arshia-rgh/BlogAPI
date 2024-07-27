from django.db.models.fields.files import FieldFile
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views import View
from ...models import Post

"""

Django CRUD API

"""


def serialize_post(post: Post):
    """
    custom serializer for handle FileField serializing

    """
    post_dict = model_to_dict(post)
    for field in post._meta.fields:
        if isinstance(getattr(post, field.name), FieldFile):
            post_dict[field.name] = getattr(post, field.name).url if getattr(post, field.name) else None
    return post_dict


class CrudPostView(View):
    def get(self, request, *args, **kwargs):
        """
            Handles GET requests. If a primary key (pk) is provided in the URL, returns the details of the specific post.
            Otherwise, returns a list of all posts.

            Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

            Returns:
            JsonResponse: A JSON response containing th
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
