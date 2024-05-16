# Generated by Django 5.0.4 on 2024-05-10 04:14

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_salaries_zenk_sal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoise',
            name='aklasheh_sal',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='paper_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='عدد الافرخ'),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='paper_sal',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True, verbose_name='السعر'),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='print_count_one',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='print_count_two',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='slofan_count',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='taglid_count',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='taglid_sal',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='taksir_count',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='uv_count',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True),
        ),
    ]
