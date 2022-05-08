from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Bulletin, Comment


class BulletinAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Bulletin
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class BulletinAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = BulletinAdminForm


admin.site.register(Category, CategoryAdmin)
admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(Comment)
