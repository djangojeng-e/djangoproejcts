# Generated by Django 2.2.7 on 2019-11-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패캠 사용자', 'verbose_name_plural': '패캠 사용자'},
        ),
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='test@email.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
