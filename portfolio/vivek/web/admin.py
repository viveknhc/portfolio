from django.contrib import admin
from web.models import PersonalDetails,Experience,SkillSett,Education,Service,Projects,Contact
# Register your models here.


admin.site.register(PersonalDetails)
admin.site.register(SkillSett)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Service)
admin.site.register(Projects)
admin.site.register(Contact)