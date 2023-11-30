from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import MyModel
from .forms import MyModelForm
# Create your views here.
class my_template(TemplateView):
    template_name='myapp\my_template.html'
class MyModelCreateView(CreateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'myapp/my_model_create.html' 
    success_url = reverse_lazy('my_model_list') 
class MyModelUpdateView(UpdateView):
    model=MyModel
    form_class=MyModelForm
    template_name='myapp/my_model_update.html'
    success_url=reverse_lazy('my_model_list')
class MyModelDetailView(DetailView):
    model=MyModel
    form_class=MyModelForm
    template_name='myapp/my_model_detail.html'
    context_object_name = 'my_model'
class MyModelListView(ListView):
    model=MyModel
    form_class=MyModelForm
    template_name='myapp/my_model_list.html'
    context_object_name = 'my_model'

