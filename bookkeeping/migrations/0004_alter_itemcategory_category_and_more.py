# Generated by Django 4.2.3 on 2023-09-20 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0003_alter_itemcategory_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.category'),
        ),
        migrations.AlterField(
            model_name='recordcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.category'),
        ),
        migrations.AlterField(
            model_name='recordcategory',
            name='record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.record'),
        ),
    ]