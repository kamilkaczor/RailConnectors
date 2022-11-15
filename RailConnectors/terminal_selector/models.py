from django.db import models

class Terminal(models.Model):
    project = models.CharField(max_length=30, choices=(
            ('Main PPL','Main PPL'),
            ('SAV','SAV'),
        )
    )
    DTR = models.CharField(max_length=15)
    connector_family = models.CharField(max_length=30, blank=True, null=True)
    cross_section_min = models.DecimalField(max_digits=3, decimal_places=2)
    cross_section_max = models.DecimalField(max_digits=3, decimal_places=2)
    plating = models.CharField(max_length=30, choices=(
            ('silver','silver'),
            ('gold','gold'),
            ('zinc', 'zinc'),
        )
    )
    gender = models.CharField(max_length=30, choices=(
            ('male', 'male'),
            ('female', 'female')
         )
    )
    manufacturer = models.CharField(max_length=30)
    manuf_number = models.CharField(max_length=30)
    insert_DTR = models.CharField(max_length=500)
    insert_size = models.CharField(max_length=100, blank=True, null=True)

class Connector(models.Model):
    project = models.CharField(max_length=30, choices=(
            ('Main PPL','Main PPL'),
            ('SAV','SAV'),
        )
    )
    insert_DTR = models.CharField(max_length=15)
    connector_description = models.CharField(max_length=30, blank=True, null=True)
    connector_manu = models.CharField(max_length=30)
    connector_manu_num = models.CharField(max_length=30)
    connector_family = models.CharField(max_length=30)
    coding = models.BooleanField(blank=True, null=True)
    insert_size = models.CharField(max_length=15, blank=True, null=True)
    insert_gender = models.CharField(max_length=30, default="none", choices=(
            ('male', 'male'),
            ('female', 'female')
         )
    )


class Wires(models.Model):
    wire = models.CharField(max_length=25)
    wire_cross_section = models.DecimalField(max_digits=5, decimal_places=2)

