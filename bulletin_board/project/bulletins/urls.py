from django.urls import path
from .views import *


urlpatterns = [
    path('', BulletinsList.as_view(), name='bulletins_list'),
    path('<slug:slug>', BulletinView.as_view(), name='post_details'),
    path('<slug:slug>/update/', BulletinUpdate.as_view(), name='post_edit'),
    path('<slug:slug>/add-comment/', NewComment.as_view(), name='add-comment'),
    path('category/<slug:slug>', InCategoryList.as_view(), name='incategory_list'),
    path('my-comments/', CommentsView.as_view(), name='my_comments'),
    path('delete-comment/<int:pk>', delete_comment, name='delete_comment'),
    path('approve-comment/<int:pk>', approve_comment, name='approve_comment'),
]
