from django.urls import path   
from . import views
urlpatterns = [
    path('', views.root, name='root'),
    path ('blog/', views.index, name='index'),
    #/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
    path('blog/new/', views.new, name='new'),
    path('blog/create/', views.create, name='create'),
    path('blog/<int:number>/', views.show, name='show'),
    path('blog/<int:number>/delete/', views.destroy, name='destroy' )

]
