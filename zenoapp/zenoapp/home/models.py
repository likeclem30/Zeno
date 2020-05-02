from django.db import models


class TestData(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.CharField(max_length=45, blank=True, null=True)
    temperature = models.CharField(max_length=45, blank=True, null=True)
    duration = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_data'
