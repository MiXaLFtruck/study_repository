import os
from datetime import datetime
from django.utils import timezone

from project_files import settings

DJANGO_SETTINGS_MODULE = settings

# path = os.environ['PATH'].split(';')
# for _ in path:
#     print(_)

print(datetime.now())
# print(timezone.now())
