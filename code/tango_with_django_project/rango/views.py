from django.shortcuts import HttpResponse, render
from rango.models import Category, Page

def index(request):
    # get top 5 categories by number of likes
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {
        "categories": category_list,
        "pages": page_list,
    }

    return render(request, 'rango/index.html', context_dict)

def category(request, category_name_slug):
    context_dict = {}

    try:
        # try to find the category
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # get all related pages
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        # dealt with in template
        pass

    return render(request, 'rango/category.html', context_dict)


def about(request):
    context_dict = {"aboutmessage": "This is the about page."}

    return render(request, 'rango/about.html', context_dict)
