from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views.home_views import home_page
from app.views.notes_view import create_note, delete_note, edit_note, details_note
from app.views.profile_views import profile_view, profile_create, profile_delete

urlpatterns = [
    path('', home_page, name='home page'),

    path('profile', profile_view, name='profile'),
    path('profile/create', profile_create, name='profile create'),
    path('profile/delete', profile_delete, name='profile delete'),

    path('note/create', create_note, name='create note'),
    path('note/edit/<int:pk>/', edit_note, name='edit note'),
    path('note/delete/<int:pk>/', delete_note, name='delete note'),
    path('note/details/<int:pk>/', details_note, name='details note')
]
