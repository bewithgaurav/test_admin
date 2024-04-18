from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from .models import Page, Permission

# Register your models here.


class PagesForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

class PagesAdmin(admin.ModelAdmin):
    form = PagesForm

# admin.site.register(Pages, PagesUserAdmin)
admin.site.register(Page, PagesAdmin)

class PermissionsForm(forms.ModelForm):
    # select multiple pages
    pages = forms.ModelMultipleChoiceField(queryset=Page.objects.all(), widget=forms.CheckboxSelectMultiple)
    # select multiple users
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Permission
        fields = '__all__'

class PagesUserAdmin(admin.ModelAdmin):
    form = PermissionsForm

admin.site.register(Permission, PagesUserAdmin)