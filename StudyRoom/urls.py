from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerPage, name="register"),

    path('', home, name="home"),
    path('room/<str:pk>/', room, name="room"),
    path('profile/<str:pk>/', user_profile, name="user-profile"),

    # path('create-room/', create_room, name="create-room"),
    # path('update-room/<str:pk>/', update_room, name="update-room"),
    path('delete-room/<str:pk>/', delete_room, name="delete-room"),
    # path('message/<str:pk>/', message, name="message"),
    path('delete-message/<str:pk>/', delete_message, name="delete-message"),
    

    # path('update-user/', updateUser, name="update-user"),

    path('topics/', topics_page, name="topics"),
    path('activity/', activityPage, name="activity"),
]
