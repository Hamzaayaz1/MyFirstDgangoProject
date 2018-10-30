from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here
from blog.models import Products


# View for index page
class IndexView(generic.ListView):
    context_object_name = 'product_list'
    template_name = 'blog/index.html'

    def all(self):
        return self.get_queryset()


class ProductEntry(CreateView):
    model = Products
    fields = ['product_title', 'product_price', 'product_description']


class ProductUpdate(UpdateView):
    model = Products
    fields = ['product_title', 'product_price', 'product_description']


class ProductDelete(DeleteView):
    model = Products
    success_url = reverse('blog:index')
