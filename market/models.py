from django.db import models


class Generator(models.Model):
    edrpou = models.CharField("ЄДРПОУ:", max_length=11)
    name = models.CharField("Назва компанії:", max_length=250)
    address = models.CharField("Адреса компанії:", max_length=250)
    contacts = models.CharField("Контакти компанії:", max_length=250)
    koatuu = models.CharField(max_length=10)
    tonnes_total = models.FloatField()
    pzuv_total = models.FloatField()
    tonnes_1 = models.FloatField()
    tonnes_2 = models.FloatField()
    tonnes_3 = models.FloatField()
    tonnes_4 = models.FloatField()
    tonnes_total_2015 = models.FloatField()
    pzuv_total_2015 = models.FloatField()
    tonnes_1_2015 = models.FloatField()
    tonnes_2_2015 = models.FloatField()
    tonnes_3_2015 = models.FloatField()
    tonnes_4_2015 = models.FloatField()
    tonnes_total_2016 = models.FloatField()
    pzuv_total_2016 = models.FloatField()
    tonnes_1_2016 = models.FloatField()
    tonnes_2_2016 = models.FloatField()
    tonnes_3_2016 = models.FloatField()
    tonnes_4_2016 = models.FloatField()
    tonnes_total_2017 = models.FloatField()
    pzuv_total_2017 = models.FloatField()
    tonnes_1_2017 = models.FloatField()
    tonnes_2_2017 = models.FloatField()
    tonnes_3_2017 = models.FloatField()
    tonnes_4_2017 = models.FloatField()
    tonnes_total_2018 = models.FloatField()
    pzuv_total_2018 = models.FloatField()
    tonnes_1_2018 = models.FloatField()
    tonnes_2_2018 = models.FloatField()
    tonnes_3_2018 = models.FloatField()
    tonnes_4_2018 = models.FloatField()
    tonnes_total_2019 = models.FloatField()
    pzuv_total_2019 = models.FloatField()
    tonnes_1_2019 = models.FloatField()
    tonnes_2_2019 = models.FloatField()
    tonnes_3_2019 = models.FloatField()
    tonnes_4_2019 = models.FloatField()

    class Meta:
        ordering = ['tonnes_total']

    def __str__(self):
        return self.edrpou
