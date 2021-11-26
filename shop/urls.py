from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "ShopHome" ),
    path('contactus/', views.contactus, name = "ContactUs" ),
    path('aboutus/', views.aboutus, name = "AboutUs" ),
    path("products/<int:myid>/", views.productview, name="ProductView"),
    path('search/', views.search, name = "Search" ),
    path('checkout/', views.checkout, name = "Checkout" ),
    path('tracker/', views.tracker, name = "Tracker" ),
    path('home/', views.index, name = "Home1")
    
]
