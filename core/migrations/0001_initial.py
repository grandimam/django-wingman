from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='WingmanSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('value', models.BooleanField(default=False)),
                ('cache_expiry', models.IntegerField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
