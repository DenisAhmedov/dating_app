from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from app.views import ClientCreateView, Logout

urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('clients/create/', ClientCreateView.as_view(), name='signup'),
]
