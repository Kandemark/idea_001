from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin
from .models import Applicant
from .models import product

admin.site.register(Applicant)

admin.site.register(product)