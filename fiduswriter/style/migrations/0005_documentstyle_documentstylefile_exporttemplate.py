# Generated by Django 2.2.3 on 2019-08-09 15:57

from django.db import migrations, models
import django.db.models.deletion
import style.models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0013_auto_20190808_1126'),
        ('style', '0004_auto_20190809_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default', help_text='The human readable title.', max_length=128)),
                ('slug', models.SlugField(default='default', help_text='The base of the filenames the style occupies.', max_length=20)),
                ('contents', models.TextField(default='', help_text='The CSS style definiton.')),
                ('document_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.DocumentTemplate')),
            ],
            options={
                'unique_together': {('slug', 'document_template')},
            },
        ),
        migrations.CreateModel(
            name='ExportTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default', help_text='The human readable title.', max_length=128)),
                ('file_type', models.CharField(choices=[('docx', 'DOCX'), ('odt', 'ODT')], max_length=5)),
                ('template_file', models.FileField(upload_to=style.models.template_filename)),
                ('document_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.DocumentTemplate')),
            ],
            options={
                'unique_together': {('title', 'document_template')},
            },
        ),
        migrations.CreateModel(
            name='DocumentStyleFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='A file references in the style. The filename will be replaced with the final url of the file in the style.', upload_to=style.models.documentstylefile_location)),
                ('filename', models.CharField(help_text='The original filename.', max_length=255)),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='style.DocumentStyle')),
            ],
            options={
                'unique_together': {('filename', 'style')},
            },
        ),
    ]
