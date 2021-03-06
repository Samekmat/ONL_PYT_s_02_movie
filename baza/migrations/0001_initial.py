# Generated by Django 3.1.6 on 2021-02-12 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baza.person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='ctors',
            field=models.ManyToManyField(related_name='roles', through='baza.Role', to='baza.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directed_by', to='baza.person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenplay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writen_by', to='baza.person'),
        ),
    ]
