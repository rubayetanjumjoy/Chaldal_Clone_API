from django_elasticsearch_dsl import Document
from .models import *
from django_elasticsearch_dsl.registries import registry
@registry.register_document
class PostDocument(Document):
    class Index:
        name="catagory"
        settings={
            'number_of_shards':1,
            'number_of_replicas':0
        }
    class Django:
        model = Catagory

        fields = [
           'name'
        ]
@registry.register_document
class PostDocumentProduct(Document):
    class Index:
        name="products"
        settings={
            'number_of_shards':1,
            'number_of_replicas':0
        }
    class Django:
        model = Product

        fields = [
            'id',
           'title',
           'description',
            'image',
            'price'
        ]