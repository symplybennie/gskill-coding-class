from django.shortcuts import render

groups = ['fashion', 'accessories', 'electronics']


items = {
    'fashion': ['clothes', 'shoes', 'caps', 'bags'],
    'accessories': ['watches', 'necklaces', 'eye-glasses'],
    'electronics': ['laptops', 'desktops', 'mouse', 'ipads']
}
# Create your views here.


def products(request):
    item = {
        'items': items,
        'groups': groups
    }
    return render(request, 'ecommerce/products.html', item)