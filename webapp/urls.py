from django.urls import path
from webapp import views

urlpatterns = [

    path('', views.Homepage, name="Homepage"),
    path('Aboutpage/', views.Aboutpage, name="Aboutpage"),
    path('Contactpage/', views.Contactpage, name="Contactpage"),
    path('Categ/', views.Categ, name="Categ"),
    path('DISPLAY/<itemCatg>/', views.DISPLAY, name="DISPLAY"),
    path('Categg/',views.Categg,name="Categg"),
    path('DISPLAYsubCAT/<procatg>/',views.DISPLAYsubCAT,name="DISPLAYsubCAT"),
    path('proSingle/<int:datasid>/',views.proSingle,name="proSingle"),
    path('Registration/',views.Registration,name="Registration"),
    path('ULogin/',views.ULogin,name="ULogin"),
    path('logIN/',views.logIN,name="logIN"),
    path('customerlogin/',views.customerlogin,name="customerlogin"),
    path('customerlogout/',views.customerlogout,name="customerlogout"),
    path('CONTACTSS/',views.CONTACTSS,name="CONTACTSS"),
    path('Payment/', views.Payment, name="Payment"),
    path('order/', views.order, name="order")
]
