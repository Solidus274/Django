from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from adminapp.forms import ProductEditForm
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    fields = '__all__'


class UsersUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'

        return context


class UsersDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('adminapp:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'

        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_create.html'
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:products')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукты/редактирование'

        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     content = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', content)
#
#
# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     content = {'title': title, 'update_form': user_form}
#
#     return render(request, 'adminapp/user_update.html', content)
#
#
# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, \
#                                           instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:user_update', \
#                                                 args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#     content = {'title': title, 'update_form': edit_form}
#
#     return render(request, 'adminapp/user_update.html', content)
#
#
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         # user.delete()
#         # вместо удаления лучше сделаем неактивным
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#
#     content = {'title': title, 'user_to_delete': user}
#
#     return render(request, 'adminapp/user_delete.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     pass
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     pass
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категория/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[category.pk]))
#
#     content = {'title': title, 'category_to_delete': category}
#
#     return render(request, 'adminapp/category_delete.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk=None):
#     title = 'админка/продукт'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     content = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', content)
#
#

#
#
# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     content = {'title': title, 'object': product, }
#
#     return render(request, 'adminapp/product_read.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'продукт/редактирование'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     content = {'title': title,
#                'update_form': edit_form,
#                'category': edit_product.category
#                }
#
#     return render(request, 'adminapp/product_update.html', content)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
#
#     content = {'title': title, 'product_to_delete': product}
#
#     return render(request, 'adminapp/product_delete.html', content)
