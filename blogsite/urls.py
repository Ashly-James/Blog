from  django.urls import path
from . import views

urlpatterns=[
path('',views.index_load),
path('products',views.products),
path('services',views.services),
path('contact',views.contact),
path('registration',views.registration),
path('save_registration',views.save_registration),	
path('login',views.login),	
path('login_account',views.login_account),
path('admin_approval',views.admin_approval),
path('blog_post',views.blog_post),
path('user_edit_delete',views.user_edit_delete),
path('blog_edit',views.blog_edit),
path('logout_view',views.logout_view),
path('admin_blog_view',views.admin_blog_view),
path('admn_edit_delete',views.admn_edit_delete),
path('usre_back',views.usre_back),
path('like',views.like),
path('like_add',views.like_add),
path('admin_blog_edit',views.admin_blog_edit),
path('admin_back',views.admin_back),
# path('admin_back',views.admin_back),
]