from django.contrib import admin
from .models import Lehmanuser
from .models import Department
from .models import Course
from .models import Coursesection
from .models import Student
from .models import Instructor
from .models import Alumni


# Register your models here.
admin.site.register(Lehmanuser)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Coursesection)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Alumni)