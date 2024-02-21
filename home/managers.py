from django.db import models


class PersonAdultManager(models.Manager):
    def is_male(self):
        return self.filter(gender='male')

    def get_queryset(self):
        return super().get_queryset().filter(age__gte=18)



    # def adults(self):
    #     return self.filter(age__gte=18)
