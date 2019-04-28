from django.db import models


# Create your models here.
class Persons(models.Model):
    id = models.CharField(max_length=10, verbose_name='id',primary_key=True)
    subid = models.CharField(max_length=6, verbose_name='subid')
    name = models.CharField(max_length=80, verbose_name='name')
    countryId = models.CharField(max_length=50, verbose_name='countryId')
    gender = models.CharField(max_length=1, verbose_name='gender')

    class Meta:
        db_table = 'Persons'  # 表名
        verbose_name = '个人信息'
        verbose_name_plural = verbose_name
        ordering = ['id', 'subid']


class RanksAverage(models.Model):
    personId = models.CharField(max_length=10, verbose_name='personId')
    eventId = models.CharField(max_length=6, verbose_name='eventId')
    best = models.IntegerField( verbose_name='best')
    worldRank = models.IntegerField( verbose_name='worldRank')
    continentRank = models.IntegerField(verbose_name='continentRank')
    countryRank = models.IntegerField( verbose_name='countryRank')

    class Meta:
        db_table = 'RanksAverage'  # 表名
        verbose_name = '名次平均'
        verbose_name_plural = verbose_name
        ordering = ['eventId', 'worldRank']


class RanksSingle(models.Model):
    personId = models.CharField(max_length=10, verbose_name='personId')
    eventId = models.CharField(max_length=6, verbose_name='eventId')
    best = models.IntegerField( verbose_name='best')
    worldRank = models.IntegerField( verbose_name='worldRank')
    continentRank = models.IntegerField( verbose_name='continentRank')
    countryRank = models.IntegerField( verbose_name='countryRank')

    class Meta:
        db_table = 'RanksSingle'  # 表名
        verbose_name = '名次单次'
        verbose_name_plural = verbose_name
        ordering = ['eventId', 'worldRank']
