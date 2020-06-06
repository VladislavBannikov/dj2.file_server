from app.source import get_files, get_content
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        # 'files': [
        #     {'name': 'file_name_1.txt',
        #      'ctime': datetime.datetime(2019, 1, 1),
        #      'mtime': datetime.datetime(2017, 1, 2)}
        # ],
        'files': get_files(date=date),
        # 'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный

    }
    if date:
        context.update({'date': date})

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context=get_content(name)
    )
