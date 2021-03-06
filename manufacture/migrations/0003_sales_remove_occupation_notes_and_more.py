# Generated by Django 4.0.6 on 2022-07-15 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0002_remove_calculationpu_fio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=40)),
                ('size', models.CharField(max_length=40)),
                ('pair', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=40)),
                ('status', models.CharField(choices=[('Новый', 'Новый'), ('В процессе', 'В процессе'), ('Собран', 'Собран'), ('Отгружен', 'Отгружен'), ('Оплачен', 'Оплачен')], max_length=40)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=40)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
            ],
        ),
        migrations.RemoveField(
            model_name='occupation',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='salarytotal',
            name='firm_social_fund',
        ),
        migrations.RemoveField(
            model_name='working_out',
            name='defective_machines',
        ),
        migrations.RemoveField(
            model_name='working_out',
            name='marriage_workers',
        ),
        migrations.AddField(
            model_name='salarytotal',
            name='oklad_fact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='working_out',
            name='machines_defect',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='working_out',
            name='workers_defect',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='monthly_salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employer_ocupation', to='manufacture.occupation'),
        ),
        migrations.AlterField(
            model_name='salarytotal',
            name='fact_work_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='salarytotal',
            name='occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salary_total_occupation', to='manufacture.occupation'),
        ),
        migrations.AlterField(
            model_name='salarytotal',
            name='oklad_nachislen',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='salarytotal',
            name='oklad_social_fund',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='salarytotal',
            name='working_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='working_out',
            name='Say_marriage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='working_out',
            name='kol_vo',
            field=models.IntegerField(default=0),
        ),
    ]
