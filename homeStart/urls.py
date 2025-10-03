from django.urls import path
from homeStart import views
from homeStart.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  
    context_object_name="message_list",
    template_name="homeStart/home.html",
)

urlpatterns = [
    path("", views.home, name="homeStart"),
    path("homeStart/<name>/", views.homeStart_there,name="homeStart_there"),
    path("home/", home_list_view, name="home"),
    path("about/", views.home, name="about"),
    path("contact/", views.home, name="contact"),
    path("log/", views.log_message, name="log"),
]
