from django.contrib import admin
from leaves.models import Holidays, LeaveDetails,Leavestructure, Leavetype, Linktoleavetype, AssignLeaveStructure, Upload_list
# Register your models here.

admin.site.register(Leavestructure)
admin.site.register(Leavetype)
admin.site.register(Linktoleavetype)
admin.site.register(AssignLeaveStructure)
admin.site.register(Holidays)
admin.site.register(Upload_list)
admin.site.register(LeaveDetails)