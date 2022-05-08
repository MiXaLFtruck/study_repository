import django_filters
from .models import Comment, Bulletin


def bulletins(request):
    if request is None:
        return Bulletin.objects.none()

    author = request.user
    return Bulletin.objects.filter(author=author)


class CommentsFilter(django_filters.FilterSet):
    post = django_filters.ModelChoiceFilter(field_name='post', lookup_expr='exact', queryset=bulletins)

    class Meta:
        model = Comment
        fields = ['post']
