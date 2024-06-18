# Generated by Django 5.0.6 on 2024-06-17 19:38

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoise',
            name='aklasheh_sal',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='paper_sal',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True, verbose_name='السعر'),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='print_count_one',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='print_count_two',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='slofan_count',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='taglid_count',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='taglid_sal',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='taksir_count',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='uv_count',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='invoise',
            name='zenk_sal',
            field=models.DecimalField(decimal_places=2, default=Decimal('42.5'), max_digits=15),
        ),
    ]