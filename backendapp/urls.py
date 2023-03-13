from django.urls import path
from backendapp import views

urlpatterns = [
   path('Frontend/',views.Frontend,name="Frontend"),

   path('LogAdmin/',views.LogAdmin,name="LogAdmin"),
   path('Loginpage/',views.Loginpage,name="Loginpage"),
   path('DisplayTable/',views.DisplayTable,name="DisplayTable"),
   path('pageEdit/<int:dataid>/',views.pageEdit,name="pageEdit"),
   path('updatePage/<int:dataid>/',views.updatePage,name="updatePage"),
   path('Deletedata/<int:dataid>/',views.Deletedata,name="Deletedata"),

   path('addpage/', views.addpage, name="addpage"),
   path('itempage/', views.itempage, name="itempage"),
   path('Itemdisp/',views.Itemdisp,name="Itemdisp"),
   path('EditItem/<int:dataid>/', views.EditItem, name="EditItem"),
   path('updateitem/<int:dataid>/',views.updateitem,name="updateitem"),
   path('DeleteItem/<int:dataid>/',views.DeleteItem,name="DeleteItem"),

   path('propage/',views.propage,name="propage"),
   path('Propagedetails/',views.Propagedetails,name="Propagedetails"),
   path('prodisp/',views.prodisp,name="prodisp"),
   path('Editpro/<int:dataid>/', views.Editpro, name="Editpro"),
   path('updatePro/<int:dataid>/',views.updatePro,name="updatePro"),
   path('Deletepro/<int:dataid>/',views.Deletepro,name="Deletepro"),

   path('USERlogin/',views.USERlogin,name="USERlogin"),
   path('adminlogin/',views.adminlogin,name="adminlogin"),
   path('adminlogout/',views.adminlogout,name="adminlogout"),
   path('Contactdisp/',views.Contactdisp,name="Contactdisp"),
   path('DeleteContact/<int:dataid>/',views.DeleteContact,name="DeleteContact"),

   path('divpage/',views.divpage,name="divpage"),
   path('divpagedetails/',views.divpagedetails,name="divpagedetails"),
   path('divdisp/',views.divdisp,name="divdisp"),
   path('divEdit/<int:dataid>/', views.divEdit, name="divEdit"),
   path('divupdate/<int:dataid>/',views.divupdate,name="divupdate"),
   path('sivDelete/<int:dataid>/',views.divDelete,name="divDelete"),
   path('Orderdisp/', views.Orderdisp, name="Orderdisp"),
   path('Deleteorder/<int:dataid>/', views.Deleteorder, name="Deleteorder")




]
