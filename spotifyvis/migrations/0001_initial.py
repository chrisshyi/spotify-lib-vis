from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('genre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Artists',
                'verbose_name': 'Artist',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('year', models.PositiveSmallIntegerField()),
                ('popularity', models.PositiveSmallIntegerField()),
                ('runtime', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name_plural': 'Tracks',
                'verbose_name': 'Track',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='AudioFeatures',
            fields=[
                ('track', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='spotifyvis.Track')),
                ('danceability', models.DecimalField(decimal_places=2, max_digits=2)),
                ('energy', models.DecimalField(decimal_places=2, max_digits=2)),
                ('loudness', models.DecimalField(decimal_places=2, max_digits=2)),
                ('speechiness', models.DecimalField(decimal_places=2, max_digits=2)),
                ('acousticness', models.DecimalField(decimal_places=2, max_digits=2)),
                ('instrumentalness', models.DecimalField(decimal_places=2, max_digits=2)),
                ('valence', models.DecimalField(decimal_places=2, max_digits=2)),
                ('tempo', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
            options={
                'verbose_name_plural': 'AudioFeatures',
                'verbose_name': 'AudioFeatures',
            },
        ),
        migrations.AddField(
            model_name='track',
            name='artists',
            field=models.ManyToManyField(blank=True, to='spotifyvis.Artist'),
        ),
        migrations.AddField(
            model_name='track',
            name='users',
            field=models.ManyToManyField(blank=True, to='spotifyvis.User'),
        ),
    ]
