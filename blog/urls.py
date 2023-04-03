from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug>/remove/', views.post_remove, name='post_remove'),
    path('category/<str:slug>/', views.category, name='category'),


    # create blogs
    path('signup/', views.signup_request, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('editprofile/',views.edit_profile,name='editprofile'),

    # path('edit/',views.edit_profile,name='edit'),
]