# Generated by Django 4.1.4 on 2023-01-05 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RDV', '0005_alter_rdv_doctorid_alter_rdv_patientid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rdv',
            old_name='DoctorId',
            new_name='RdvDoctor',
        ),
        migrations.RenameField(
            model_name='rdv',
            old_name='PatientId',
            new_name='RdvPatient',
        ),
    ]
