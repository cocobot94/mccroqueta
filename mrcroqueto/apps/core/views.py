from apps.users.models import User
from django.views.generic.base import TemplateView
from apps.products.models import Products
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# @method_decorator(login_required, name="dispatch")


# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"


class AboutTemplateView(TemplateView):
    template_name = "core/about.html"


@method_decorator(login_required, name="dispatch")
class ContactTemplateView(TemplateView):
    template_name = "core/contact.html"


@method_decorator(login_required, name="dispatch")
class ModalTemplateView(TemplateView):
    template_name = "core/reservation.html"
