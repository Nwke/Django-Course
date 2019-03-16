import datetime
import os

from django.shortcuts import render
from django.views.generic import TemplateView

from app.settings import FILES_PATH


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        data_of_files = {'files': []}
        files = os.listdir(FILES_PATH)

        if date is None:
            for file in files:
                file_info = os.stat(os.path.join(FILES_PATH, file))
                data_of_files['files'].append({
                    'name': file,
                    'ctime': datetime.datetime.utcfromtimestamp(file_info.st_ctime),
                    'mtime': datetime.datetime.utcfromtimestamp(file_info.st_mtime)
                })
            return data_of_files
        else:
            year, month, day = date.split('-')
            gotten_data = datetime.datetime(int(year), int(month), int(day)).date()
            for file in files:
                file_info = os.stat(os.path.join(FILES_PATH, file))

                if datetime.datetime.utcfromtimestamp(file_info.st_ctime).date() == gotten_data:
                    continue

                data_of_files['files'].append({
                    'name': file,
                    'ctime': datetime.datetime.utcfromtimestamp(file_info.st_ctime),
                    'mtime': datetime.datetime.utcfromtimestamp(file_info.st_mtime)
                })

            return data_of_files


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = os.path.join(FILES_PATH, name)
    with open(f'{path}', encoding='utf8') as f:
        content_of_file = ''
        for line in f:
            content_of_file += line

    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': f'{content_of_file}'}
    )
