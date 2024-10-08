# Generated by Django 4.2.2 on 2023-06-23 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_remove_product_amount_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.product1'),
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
