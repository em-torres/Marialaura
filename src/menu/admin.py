from django.contrib import admin

from .models import MenuWeek, Menu

class MenuWeekinLine(admin.TabularInline):
    model = Menu
    max_num = 1


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu_week','mo1','mo2','tu1','tu2','we1','we2','th1','th2','fr1','fr2']
    #inlines = [MenuWeekinLine]

    class Meta:
        model = Menu

class MenuWeekAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','week','active']
    inlines = [MenuWeekinLine]
    ordering = ['start_date']

    class Meta:
        model = MenuWeek

#admin.site.register(Menu,MenuAdmin)

admin.site.register(MenuWeek,MenuWeekAdmin)