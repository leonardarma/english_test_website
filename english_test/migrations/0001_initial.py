# Generated by Django 3.2.13 on 2022-07-11 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Partie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('joueur', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='english_test.joueur')),
            ],
        ),
        migrations.CreateModel(
            name='Verbe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_verbale', models.CharField(max_length=200)),
                ('participe_passe', models.CharField(max_length=200)),
                ('preterit', models.CharField(max_length=200)),
                ('traduction', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('code_postal', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse_participe_passe', models.CharField(max_length=200)),
                ('reponse_preterit', models.CharField(max_length=200)),
                ('date_envoie', models.DateTimeField(auto_now_add=True)),
                ('date_reponse', models.DateTimeField()),
                ('partie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='english_test.partie')),
                ('verbe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='english_test.verbe')),
            ],
        ),
        migrations.AddField(
            model_name='joueur',
            name='ville',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='english_test.ville'),
        ),
    ]
