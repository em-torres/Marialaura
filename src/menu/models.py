from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from products.models import Product



# Create your models here.

class MenuQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class MenuManager(models.Manager):
    def get_queryset(self):
        return MenuQuerySet(self.model, using=self._db)

def upload_location(instance, filename):
    return "menu_week/%s/%s" %(instance.id, filename)


class MenuWeek(models.Model):
    week = models.CharField(max_length=120, null=True, blank=True)
    start_date = models.DateField(auto_now_add=False, auto_now=False, unique=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, unique=True)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_location,null=True, blank=True)

    object = MenuManager()

    def __unicode__(self):
        date = self.start_date.strftime('%d/%m/%y') + self.end_date.strftime(' to %d/%m/%y')
        return date

    def get_absolute_url(self):
        return reverse("menu_detail", kwargs={"pk": self.pk})

    def save(self):
        self.menu = unicode
        super(MenuWeek, self).save()

    def clean(self):
        day_start = (self.start_date).strftime("%j")
        day_end = (self.end_date).strftime("%j")
        if not day_start < day_end or not int(day_start) + 007 == int(day_end):
            raise ValidationError({'end_date': ValidationError('No hay 7 Dias de Diferencias')})

    def validate_unique(self, *args, **kwargs):
        super(MenuWeek, self).validate_unique(*args, **kwargs)

        qs = self.__class__._default_manager.filter(
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        )

        if not self._state.adding and self.pk is not None:
            qs = qs.exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError({
                NON_FIELD_ERRORS: ['overlapping date range', ],
            })


class Menu(models.Model):
    mo1 = models.ForeignKey(Product, related_name='mo1', null=True, blank=True)
    mo2 = models.ForeignKey(Product, related_name='mo2', null=True, blank=True)
    tu1 = models.ForeignKey(Product, related_name='tu1', null=True, blank=True)
    tu2 = models.ForeignKey(Product, related_name='tu2', null=True, blank=True)
    we1 = models.ForeignKey(Product, related_name='we1', null=True, blank=True)
    we2 = models.ForeignKey(Product, related_name='we2', null=True, blank=True)
    th1 = models.ForeignKey(Product, related_name='th1', null=True, blank=True)
    th2 = models.ForeignKey(Product, related_name='th2', null=True, blank=True)
    fr1 = models.ForeignKey(Product, related_name='fr1', null=True, blank=True)
    fr2 = models.ForeignKey(Product, related_name='fr2', null=True, blank=True)
    menu_week = models.ForeignKey(MenuWeek, related_name='menu_week')

    def get_absolute_url(self):
        return self.menu_week.get_absolute_url()
