import datetime
from haystack import indexes
from rango.models import Category, Page

class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='title', document=True, use_template=True)

    def get_model(self):
        return Page

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated"""
        return self.get_model().objects.all()
