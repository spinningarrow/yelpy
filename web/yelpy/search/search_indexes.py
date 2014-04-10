__author__ = 'user'

from haystack import indexes
from search.models import foodslistings
from search.models import artslistings
from search.models import shopslistings

class FoodIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    is_claimed = indexes.CharField(model_attr='is_claimed', null=True)
    rating = indexes.CharField(model_attr='rating', null=True)
    mobile_url = indexes.CharField(model_attr='mobile_url', null=True)
    rating_image_url = indexes.CharField(model_attr='rating_image_url', null=True)
    review_count = indexes.CharField(model_attr='review_count', null=True)
    name = indexes.CharField(model_attr='name', null=True)
    rating_image_url_small = indexes.CharField(model_attr='rating_image_url_small', null=True)
    url = indexes.CharField(model_attr='url', null=True)
    is_closed = indexes.CharField(model_attr='is_closed', null=True)
    phone = indexes.CharField(model_attr='phone', null=True)
    snippet_text = indexes.CharField(model_attr='snippet_text', null=True)
    image_url = indexes.CharField(model_attr='image_url', null=True)
    categories = indexes.CharField(model_attr='categories', null=True)
    display_phone = indexes.CharField(model_attr='display_phone', null=True)
    rating_image_url_large = indexes.CharField(model_attr='rating_image_url_large', null=True)
    identifier = indexes.CharField(model_attr='identifier', null=True)
    snippet_image_url = indexes.CharField(model_attr='snippet_image_url', null=True)
    location = indexes.CharField(model_attr='location', null=True)
    deals = indexes.CharField(model_attr='deals', null=True)

    def get_model(self):
        return foodslistings

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ArtsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    is_claimed = indexes.CharField(model_attr='is_claimed', null=True)
    rating = indexes.CharField(model_attr='rating', null=True)
    mobile_url = indexes.CharField(model_attr='mobile_url', null=True)
    rating_image_url = indexes.CharField(model_attr='rating_image_url', null=True)
    review_count = indexes.CharField(model_attr='review_count', null=True)
    name = indexes.CharField(model_attr='name', null=True)
    rating_image_url_small = indexes.CharField(model_attr='rating_image_url_small', null=True)
    url = indexes.CharField(model_attr='url', null=True)
    is_closed = indexes.CharField(model_attr='is_closed', null=True)
    phone = indexes.CharField(model_attr='phone', null=True)
    snippet_text = indexes.CharField(model_attr='snippet_text', null=True)
    image_url = indexes.CharField(model_attr='image_url', null=True)
    categories = indexes.CharField(model_attr='categories', null=True)
    display_phone = indexes.CharField(model_attr='display_phone', null=True)
    rating_image_url_large = indexes.CharField(model_attr='rating_image_url_large', null=True)
    identifier = indexes.CharField(model_attr='identifier', null=True)
    snippet_image_url = indexes.CharField(model_attr='snippet_image_url', null=True)
    location = indexes.CharField(model_attr='location', null=True)
    deals = indexes.CharField(model_attr='deals', null=True)

    def get_model(self):
        return artslistings

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class ShopsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    is_claimed = indexes.CharField(model_attr='is_claimed', null=True)
    rating = indexes.CharField(model_attr='rating', null=True)
    mobile_url = indexes.CharField(model_attr='mobile_url', null=True)
    rating_image_url = indexes.CharField(model_attr='rating_image_url', null=True)
    review_count = indexes.CharField(model_attr='review_count', null=True)
    name = indexes.CharField(model_attr='name', null=True)
    rating_image_url_small = indexes.CharField(model_attr='rating_image_url_small', null=True)
    url = indexes.CharField(model_attr='url', null=True)
    is_closed = indexes.CharField(model_attr='is_closed', null=True)
    phone = indexes.CharField(model_attr='phone', null=True)
    snippet_text = indexes.CharField(model_attr='snippet_text', null=True)
    image_url = indexes.CharField(model_attr='image_url', null=True)
    categories = indexes.CharField(model_attr='categories', null=True)
    display_phone = indexes.CharField(model_attr='display_phone', null=True)
    rating_image_url_large = indexes.CharField(model_attr='rating_image_url_large', null=True)
    identifier = indexes.CharField(model_attr='identifier', null=True)
    snippet_image_url = indexes.CharField(model_attr='snippet_image_url', null=True)
    location = indexes.CharField(model_attr='location', null=True)
    menu_provider = indexes.CharField(model_attr='menu_provider', null=True)
    menu_date_updated = indexes.CharField(model_attr='menu_date_updated', null=True)

    def get_model(self):
        return shopslistings

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
