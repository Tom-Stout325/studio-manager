# Generated by Django 4.2.10 on 2024-02-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_tag_remove_invoice_client_order_invoice_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='app.product'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, max_length=100, null=True)),
                ('invoice', models.ManyToManyField(to='app.invoice')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='expense',
            field=models.ManyToManyField(blank=True, null=True, to='app.expense'),
        ),
    ]
