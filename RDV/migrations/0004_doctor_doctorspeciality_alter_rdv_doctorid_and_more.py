# Generated by Django 4.1.4 on 2022-12-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RDV', '0003_rdv_doctorid_rdv_patientid'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='DoctorSpeciality',
            field=models.CharField(default='Généraliste', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rdv',
            name='DoctorId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='PatientId',
            field=models.IntegerField(),
        ),
    ]
