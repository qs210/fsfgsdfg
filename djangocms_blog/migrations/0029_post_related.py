# Generated by Django 1.10.5 on 2017-04-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_blog", "0028_auto_20170304_1040"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="related",
            field=models.ManyToManyField(blank=True, to="djangocms_blog.Post", verbose_name="Related Posts"),
        ),
    ]
