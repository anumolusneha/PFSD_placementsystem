from django.contrib import admin
from .models import User, Company, Job, Application, PlacementRecord


admin.site.register(User)
admin.site.register(Company)        # ✅ Add this line
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(PlacementRecord)