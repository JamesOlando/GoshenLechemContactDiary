from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.diary_form,name='diary_insert'), #GET and POST request for insert operation
    path('diary/<int:id>/',views.diary_form,name='diary_update'), #GET and POST request for update operation
    path('delete/<int:id>/',views.diary_delete,name='diary_delete'),
    path('list/',views.diary_list,name='diary_list') #GET request to retrieve and display all records
]