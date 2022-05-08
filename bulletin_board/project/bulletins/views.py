from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from project_files.settings import DEFAULT_FROM_EMAIL
from .filters import CommentsFilter
from .forms import PostForm, CommentCreateForm
from .models import Bulletin, Comment


class BulletinsList(ListView):
    model = Bulletin
    template_name = 'adds-list.html'
    context_object_name = 'bulletins'
    queryset = Bulletin.objects.all().order_by('title').select_related('category')


class InCategoryList(ListView):
    model = Bulletin
    template_name = 'adds-list.html'
    context_object_name = 'bulletins'

    def get_queryset(self):
        return Bulletin.objects.filter(category__slug=self.kwargs['slug']).order_by('title')


class BulletinView(DetailView):
    model = Bulletin
    template_name = 'post-details.html'
    context_object_name = 'post'

    def get_object(self, *args, **kwargs):
        obj = Bulletin.objects.get(slug=self.kwargs['slug'])
        return obj

    def get_context_data(self, *args, **kwargs):
        comments = Comment.objects.filter(post=self.get_object(), approved=True)
        return {
            **super().get_context_data(**kwargs),
            'comments': comments
        }


class BulletinUpdate(UpdateView):
    form_class = PostForm
    template_name = 'post-update.html'

    def get_object(self, **kwargs):
        return Bulletin.objects.get(slug=self.kwargs['slug'])


class NewComment(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CommentCreateForm
    template_name = 'post-update.html'
    success_message = 'Ваш отклик будет опубликован после одобрения его автором объявления'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Bulletin, slug=self.kwargs['slug'])
        return super(NewComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_details', kwargs={'slug': self.kwargs['slug']})


class CommentsView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'replies-list.html'
    context_object_name = 'comments'

    def get_filter(self):
        return CommentsFilter(self.request.GET, request=self.request, queryset=Comment.objects.filter(
            post__author=self.request.user).select_related('post'))

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        _filter = CommentsFilter(self.request.GET, request=self.request, queryset=Comment.objects.filter(
            post__author=self.request.user))
        return {
            **super().get_context_data(**kwargs),
            'filter': _filter
        }


def delete_comment(request, **kwargs):
    Comment.objects.get(pk=kwargs['pk']).delete()
    return redirect('my_comments')


def approve_comment(request, **kwargs):
    comment = Comment.objects.get(pk=kwargs['pk'])
    comment.approved = True
    comment.save()
    send_mail(subject='УРА!', message='Ваш отклик был принят автором объявления.', from_email=DEFAULT_FROM_EMAIL,
              recipient_list=[comment.author.email], fail_silently=True)
    return redirect('my_comments')
