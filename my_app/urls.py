from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.index),
    path("register", views.register),
    path('log_in', views.log_in),
    path('log_out', views.log_out),
    path('user_page/<user_id>', views.user_page),
    path("success/<user_id>", views.success),
    path("add_quote/<user_id>", views.add_quote),
    path("add_fav/<quote_id>/<user_id>", views.add_fav),
    path('UnFavorite/<quote_id>/<user_id>', views.unfavorite),
    path("edit/<user_id>", views.edit),
    path('quotes/<user_id>/update', views.update),
    path('quotes/<quote_id>/<user_id>/destroy', views.destroy),
]