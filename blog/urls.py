from django.urls import path
from .views import Homeview,Article_page,Add_post,UpdateViewform,Sign_up,Log_in,Logout,Contact,Addcommentview,ab,LikeView


urlpatterns = [
    path('',Homeview.as_view(),name='home'),
    path('article/<int:pk>',Article_page.as_view(),name ='article'),
    path('add_post/',Add_post.as_view(),name='about'),
    path('add_post/edit/<int:pk>',UpdateViewform.as_view(),name = 'update'),
    path('signup/',Sign_up, name='signup'),
    path('login/',Log_in,name="login"),
    path('logout/',Logout,name="logout"),
    path('contact/',Contact.as_view(),name="contact"),
    path('article/<int:pk>/comment',Addcommentview.as_view(),name='add_comment'),
    path('about/',ab,name="aboutt"),
    path('like/<int:pk>',LikeView,name="like_post")    
]
