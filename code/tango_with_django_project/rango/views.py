from django.shortcuts import HttpResponse, render
from rango.models import Category, Page
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm, PageSearchForm

def index(request):
    # get top 5 categories by number of likes
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {
        "categories": category_list,
        "pages": page_list,
    }

    # get number of visits from session
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        # if more than one day
        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits

    context_dict['visits'] = visits

    return render(request, 'rango/index.html', context_dict)

def category(request, category_name_slug):
    context_dict = {}

    try:
        # try to find the category
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        context_dict['category_name_slug'] = category.slug

        # get all related pages
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        # dealt with in template
        pass

    return render(request, 'rango/category.html', context_dict)


def about(request):
    visits = request.session.get('visits')
    context_dict = {
        'aboutmessage': "This is the about page.",
        'visits': visits
    }

    return render(request, 'rango/about.html', context_dict)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return to homepage
            return index(request)
        else:
            print form.errors
    else:
        # display form
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'rango/add_page.html', context_dict)

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})

def root(request):
    form = PageSearchForm(request.GET)
    results = form.search()

    return render(request, 'search/search_root.html',{
        'search_query': search_query,
        'pages': results,
    })
