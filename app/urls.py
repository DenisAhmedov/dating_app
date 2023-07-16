from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from app.views import ClientCreateView, Logout, GetAllClients, ClientView, MatchView

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('clients/create', ClientCreateView.as_view(), name='signup'),
    path('list/', GetAllClients.as_view(), name='clients_list'),
    path('clients/<int:pk>', ClientView.as_view()),
    path('clients/<int:pk>/match', MatchView.as_view(), name='match'),
]
