import os
from django.conf import settings
from datetime import datetime

path = settings.FILES_PATH


def get_files(date=None):
    files_stat = []
    files = os.listdir(path)
    for f in files:
        st = os.stat(os.path.join(path, f))
        ctime_datetime = datetime.fromtimestamp(st.st_ctime)
        mtime_datetime = datetime.fromtimestamp(st.st_mtime)
        if not date or (date == ctime_datetime.date() or date == mtime_datetime.date()):
            files_stat.append({'name': f, 'ctime': ctime_datetime, 'mtime': mtime_datetime})
    return files_stat


def get_content(file_name):
    file_path = os.path.join(path, file_name)
    with open(file_path) as f:
        content = f.read()
    return {'file_name': file_name, 'file_content': content}
