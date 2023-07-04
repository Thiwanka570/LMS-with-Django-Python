from django.urls import path
from . import views

urlpatterns=[
    path('',views.reportdata,name="reportdata"),
    path('addbook/',views.addbook,name="addbook"),
    path('Return/',views.returnbooks,name="Return"),
    path('addmember/',views.addmember,name="addmember"),
    path('borrwdetails/',views.borrwdetails,name="borrwdetails"),
    path('reports/',views.reportdata, name="reportdata" ),
    path('Allbooks/',views.ViewAllbooks, name="ViewAllbooks" ),
    path('Allmembers/',views.ViewAllmembers, name="ViewAllmembers" ),
    path('All_borrow_books/',views.ViewAllbookborrws, name="ViewAllbookborrws"),
    path('updatemembers/<str:pid>/',views.updateMembers, name='updatemembers'),
    path('Memberlist/',views.Memberlist,name="Memberlist"),
    path('delete/<str:pid>',views.deleteMember,name="deletemember"),
    path('edit/<str:pid>',views.updatebooks,name="updatebooks"),
    path('deletebook/<str:pid>',views.deletebooks,name="deletebooks"),

]