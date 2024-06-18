# Generated by Django 5.0.6 on 2024-06-17 18:48

import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم العميل')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='هاتف العميل')),
                ('receivedCash', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15, verbose_name='النقديه المتبقيه')),
                ('totalCash', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15, verbose_name='اجمالي النقديه')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='العملاء', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_type', models.CharField(max_length=50, verbose_name='الصنف')),
                ('count', models.IntegerField(verbose_name='العدد')),
                ('salary_of_one', models.DecimalField(decimal_places=1, max_digits=15, verbose_name='سعر الوحده')),
                ('total', models.CharField(max_length=50, verbose_name='الاجمالي')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
            ],
        ),
        migrations.CreateModel(
            name='Invoise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الفاتورة')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('done', models.BooleanField(default=False)),
                ('paper_taraf', models.CharField(blank=True, choices=[('العميل', 'العميل'), ('المطبعة', 'المطبعة')], max_length=50, verbose_name='الورق طرف')),
                ('paper_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='عدد الافرخ')),
                ('paper_sal', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True, verbose_name='السعر')),
                ('paper_type_one', models.CharField(blank=True, choices=[('كوشيه', 'كوشيه'), ('طبع', 'طبع'), ('استيكر', 'استيكر'), ('دوبلكس', 'دوبلكس'), ('برستول كوشيه', 'برستول كوشيه')], max_length=50, verbose_name='نوع الورق')),
                ('paper_type_two', models.CharField(blank=True, max_length=50)),
                ('paper_size_one', models.CharField(blank=True, max_length=10, verbose_name='مقاس القص 1')),
                ('paper_size_two', models.CharField(blank=True, max_length=10, verbose_name='مقاس القص 2')),
                ('zenk_taraf', models.CharField(blank=True, choices=[('العميل', 'العميل'), ('المطبعة', 'المطبعة')], max_length=50, verbose_name='الزنك طرف')),
                ('zenk_count', models.IntegerField(default=0)),
                ('zenk_sal', models.DecimalField(decimal_places=1, default=Decimal('42.5'), max_digits=15)),
                ('print_count_one', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('print_count_two', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('print_douple_face', models.BooleanField(default=False, verbose_name='تطبع و تقلب')),
                ('color_k', models.BooleanField(default=False)),
                ('color_y', models.BooleanField(default=False)),
                ('color_m', models.BooleanField(default=False)),
                ('color_c', models.BooleanField(default=False)),
                ('color_zahabi', models.BooleanField(default=False)),
                ('color_faddi', models.BooleanField(default=False)),
                ('color_sabgha', models.BooleanField(default=False)),
                ('color_warnish', models.BooleanField(default=False)),
                ('color_kohley', models.BooleanField(default=False)),
                ('color_special', models.CharField(blank=True, max_length=50)),
                ('color_back_k', models.BooleanField(default=False)),
                ('color_back_y', models.BooleanField(default=False)),
                ('color_back_m', models.BooleanField(default=False)),
                ('color_back_c', models.BooleanField(default=False)),
                ('color_back_zahabi', models.BooleanField(default=False)),
                ('color_back_faddi', models.BooleanField(default=False)),
                ('color_back_sabgha', models.BooleanField(default=False)),
                ('color_back_warnish', models.BooleanField(default=False)),
                ('color_back_kohley', models.BooleanField(default=False)),
                ('color_back_special', models.CharField(blank=True, max_length=50)),
                ('daftar_count', models.CharField(blank=True, max_length=50)),
                ('groups_count', models.CharField(blank=True, choices=[('25', '25'), ('33', '33'), ('50', '50'), ('100', '100'), ('150', '150'), ('200', '200')], max_length=50)),
                ('sorting', models.CharField(blank=True, choices=[('اول', 'اول'), ('اول + اخير', 'اول + اخير'), ('اول + وسط + اخير', 'اول + وسط + اخير'), ('اول + 2وسط + اخير', 'اول + 2وسط + اخير'), ('اول + 3وسط + اخير', 'اول + 3وسط + اخير')], max_length=50)),
                ('counting', models.CharField(blank=True, max_length=50)),
                ('slofan', models.CharField(blank=True, choices=[('مط', 'مط'), ('لامع', 'لامع')], max_length=50)),
                ('slofan_ckb', models.BooleanField(default=False)),
                ('slofan_geha', models.CharField(blank=True, max_length=50)),
                ('slofan_count', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('uv', models.CharField(blank=True, max_length=50)),
                ('uv_ckb', models.BooleanField(default=False)),
                ('uv_count', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('taksir', models.CharField(blank=True, choices=[('كامل', 'كامل'), ('نصف تكسيره', 'نصف تكسيره'), ('ريجه', 'ريجه')], max_length=50)),
                ('taksir_ckb', models.BooleanField(default=False)),
                ('taksir_count', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('forma', models.CharField(blank=True, max_length=50)),
                ('forma_ckb', models.BooleanField(default=False)),
                ('spot', models.CharField(blank=True, max_length=50)),
                ('spot_ckb', models.BooleanField(default=False)),
                ('film', models.CharField(blank=True, max_length=50)),
                ('film_ckb', models.BooleanField(default=False)),
                ('aklasheh', models.CharField(blank=True, choices=[('بصمه', 'بصمه'), ('كوفراج', 'كوفراج'), ('بصمه و كوفراج', 'بصمه و كوفراج')], max_length=50)),
                ('aklasheh_ckb', models.BooleanField(default=False)),
                ('aklasheh_sal', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('basma', models.CharField(blank=True, max_length=50)),
                ('basma_ckb', models.BooleanField(default=False)),
                ('taglid', models.CharField(blank=True, choices=[('كرتون', 'كرتون'), ('لف', 'لف'), ('لطش', 'لطش'), ('دبوس', 'دبوس'), ('لصق بونطه', 'لصق بونطه'), ('غراء', 'غراء')], max_length=50)),
                ('taglid_ckb', models.BooleanField(default=False)),
                ('taglid_count', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('taglid_sal', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=15, null=True)),
                ('tawdib', models.CharField(blank=True, max_length=50)),
                ('tawdib_ckb', models.BooleanField(default=False)),
                ('nakl', models.CharField(blank=True, max_length=50)),
                ('nakl_ckb', models.BooleanField(default=False)),
                ('tasmim', models.CharField(blank=True, max_length=50)),
                ('tasmim_ckb', models.BooleanField(default=False)),
                ('khadamat', models.CharField(blank=True, max_length=50)),
                ('khadamat_ckb', models.BooleanField(default=False)),
                ('salk', models.CharField(blank=True, max_length=50)),
                ('salk_ckb', models.BooleanField(default=False)),
                ('kas', models.CharField(blank=True, max_length=50)),
                ('kas_ckb', models.BooleanField(default=False)),
                ('total_cash', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('remaining_cash', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='الفواتير', to='api.client')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiseSalaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('y_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('m_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('c_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('zahabi_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('faddi_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('sapgha_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('warnish_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('kohley_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('special_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('slofan_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('taksir_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('UV_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('film_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('zenk_sal', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=15)),
                ('invoise', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_value', models.DecimalField(decimal_places=1, max_digits=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('push_way', models.CharField(choices=[('كاش', 'كاش'), ('محفظه الكترونيه', 'محفظه الكترونيه')], max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('y_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('m_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('c_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('zahabi_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('faddi_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('sapgha_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('warnish_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('kohley_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('special_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('slofan_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('taksir_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('UV_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('film_sal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('zenk_sal', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=15)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
