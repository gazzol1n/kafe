# Generated by Django 4.2.16 on 2024-10-29 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PR_8_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите категорию пиццы', max_length=200, verbose_name='Категория пиццы')),
            ],
        ),
        migrations.CreateModel(
            name='DoughType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите тип теста', max_length=50, verbose_name='Тип теста')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название ингредиента', max_length=100, verbose_name='Ингредиент')),
                ('is_vegetarian', models.BooleanField(default=False, help_text='Этот ингредиент вегетарианский?', verbose_name='Вегетарианский')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(help_text='Введите количество', verbose_name='Количество')),
                ('customer_name', models.CharField(help_text='Введите имя клиента', max_length=100, verbose_name='Имя клиента')),
                ('address', models.CharField(help_text='Введите адрес доставки', max_length=200, verbose_name='Адрес доставки')),
                ('phone_number', models.CharField(help_text='Введите номер телефона клиента', max_length=15, verbose_name='Номер телефона')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('status', models.CharField(default='Принят', help_text='Статус заказа', max_length=20, verbose_name='Статус заказа')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название пиццы', max_length=200, verbose_name='Название пиццы')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену пиццы', max_digits=6, verbose_name='Цена')),
                ('category', models.ForeignKey(help_text='Выберите категорию пиццы', on_delete=django.db.models.deletion.CASCADE, to='PR_8_APP.category', verbose_name='Категория')),
                ('dough_type', models.ForeignKey(help_text='Выберите тип теста', on_delete=django.db.models.deletion.CASCADE, to='PR_8_APP.doughtype', verbose_name='Тип теста')),
                ('ingredients', models.ManyToManyField(help_text='Выберите ингредиенты для пиццы', to='PR_8_APP.ingredient', verbose_name='Ингредиенты')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(help_text='Введите размер пиццы', max_length=20, verbose_name='Размер пиццы')),
                ('diameter', models.IntegerField(help_text='Введите диаметр пиццы в см', verbose_name='Диаметр (см)')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='status',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(help_text='Выберите размер пиццы', on_delete=django.db.models.deletion.CASCADE, to='PR_8_APP.pizzasize', verbose_name='Размер пиццы'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(help_text='Выберите пиццу', on_delete=django.db.models.deletion.CASCADE, to='PR_8_APP.pizza', verbose_name='Пицца'),
        ),
    ]