from haystack import indexes
from .models import Staff

class StaffIndex(indexes.SearchIndex, indexes.Indexable):
    # text = indexes.EdgeNgramField(document=True, use_template=True)
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    # w_tel = indexes.CharField(model_attr='w_tel')
    # p_tel = indexes.CharField(model_attr='p_tel')

    # publish = indexes.DateTimeField(model_attr='publish')

    def get_model(self):
        return Staff

    def index_queryset(self, using=None):
        return self.get_model().objects.all()