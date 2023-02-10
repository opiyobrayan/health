
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import CustomLoginView, home
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
   
    path('', home.as_view(), name='home'),
   
    
    path('workplan', views.workplan,name='workplan'),
    path('pdf/<int:pk>', views.view_pdf, name='view_pdf'),
    path('excel', views.display_excel, name='excel'),
    path('activity', views.activity, name='activity'),
    path('add-activity', views.add_activity, name='add-activity'),
    path('partners', views.partners, name='partners'),

]
