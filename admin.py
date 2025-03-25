from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMembership

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)
admin.site.register(Student)
admin.site.register(OrgMembership)

admin.ACS.register(College)
admin.ACS.register(Program)
admin.ACS.register(Organization)
admin.ACS.register(Student)
admin.ACS.register(OrgMembership)

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)
admin.site.register(Student)
admin.site.register(OrgMembership)
