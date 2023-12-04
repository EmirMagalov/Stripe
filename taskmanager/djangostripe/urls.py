from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path("cloth/<slug:slug>",views.clothslug,name="slug"),
    path("session",views.session,name="session"),
    path("basket",views.basket,name="basket"),
    path("delbasket",views.sessiondel,name="delbasket"),
    path("mens",views.mens,name="mens"),
    path("womens",views.womens,name="womens"),
    path("check",views.chek,name="check")
]