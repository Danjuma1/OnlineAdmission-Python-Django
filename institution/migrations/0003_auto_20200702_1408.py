# Generated by Django 3.0.7 on 2020-07-02 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0002_auto_20200701_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admissionsession',
            options={'verbose_name': 'AdmissionSession', 'verbose_name_plural': '2. AdmissionSession'},
        ),
        migrations.CreateModel(
            name='InstitutionTransactionMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='transaction/')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institute_transaction', to='institution.InstitutionProfile')),
            ],
            options={
                'verbose_name': 'Institution Transaction',
                'verbose_name_plural': '3. Institution Transaction',
            },
        ),
    ]
