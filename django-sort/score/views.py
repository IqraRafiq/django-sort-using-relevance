from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.paginator import Paginator
from .models import Products

# Create your views here


@login_required
def index(request):
        
    products = Products.objects.score();

    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html', {'page_obj':page_obj})

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
 
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
