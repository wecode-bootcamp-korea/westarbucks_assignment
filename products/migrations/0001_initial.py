# Generated by Django 4.0.2 on 2022-02-11 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
            ],
            options={
                'db_table': 'drinks',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_mi', models.CharField(max_length=45)),
                ('size_fluid_ounce', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=5, max_digits=10)),
                ('sodium_mg', models.DecimalField(decimal_places=5, max_digits=10)),
                ('saturated_fat_g', models.DecimalField(decimal_places=5, max_digits=10)),
                ('sugars_g', models.DecimalField(decimal_places=5, max_digits=10)),
                ('protein_g', models.DecimalField(decimal_places=5, max_digits=10)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sizes')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=300)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.CreateModel(
            name='Allergy_drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
            ],
            options={
                'db_table': 'allergy_drink',
            },
        ),
        migrations.AddField(
            model_name='allergy',
            name='drinks',
            field=models.ManyToManyField(through='products.Allergy_drink', to='products.Drinks'),
        ),
    ]
