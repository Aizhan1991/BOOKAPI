from rest_framework.serializers import ModelSerializer
from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # все поля
        # exclude = 'title'           # все кроме,(исключени)
        


