import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():
    python_cat = add_cat(
        name='Python',
        views=128,
        likes=64
    )

    add_page(
        cat=python_cat,
        title="Offical Python Tutorial",
        url="http://docs.python.org/2/tutorial",
        views=64
    )

    add_page(
        cat=python_cat,
        title="How To Think Like A Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=128
    )

    add_page(
        cat=python_cat,
        title="Learn Python In 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python",
        views=40
    )

    django_cat = add_cat(
        name='Django',
        views=64,
        likes=32
    )

    add_page(
        cat=django_cat,
        title="Official Django Tutorial",
        url="http://docs.djangoproject.com/en/1.7/intro/tutorial01/",
        views=55
    )

    add_page(
        cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=250
    )

    add_page(
        cat=django_cat,
        title="How To Tango With Django",
        url="http://www.tangowithdjango.com/",
        views=98
    )

    frame_cat = add_cat(
        name="Other Frameworks",
        views=32,
        likes=16
    )

    add_page(
        cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org/"
    )

    add_page(
        cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=5
    )

    # Print out what we added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c

# Execute function
if __name__ == '__main__':
    print "Starting rango population script..."
    populate()
