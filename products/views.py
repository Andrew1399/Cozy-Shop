from django.shortcuts import render, get_object_or_404
from products.models import Product, Category
from cart.forms import CartAddItemForm

def index(request):
    return render(request, 'products/index.html')


def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'products/products_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddItemForm()
    return render(request, 'products/product_detail.html', {'product': product, 'cart_product_form': cart_product_form})


