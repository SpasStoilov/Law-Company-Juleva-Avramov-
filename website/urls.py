from django.urls import path
from website.views import home_page, about_page, clients_page, contacts_page, test_page, consultation_page

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('clients/', clients_page, name="clients"),
    path('contacts/', contacts_page, name="contacts"),
    path('consultation/', consultation_page, name="consultation"),
    path('test/', test_page)
]
