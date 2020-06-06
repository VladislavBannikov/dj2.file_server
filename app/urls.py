from datetime import datetime, date
from django.urls import path, register_converter
from app.views import file_list, file_content


# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value: date) -> str:
        return value.strftime("%Y-%m-%d")


register_converter(DateConverter, 'dc')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dc:date>', file_list, name='file_list'),
    path('file/<str:name>/', file_content, name='file_content'),
]
