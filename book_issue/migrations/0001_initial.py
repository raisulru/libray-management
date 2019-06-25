# Generated by Django 2.2.2 on 2019-06-25 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('suggest_return_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('WITHDRAW', 'Withdraw'), ('RETURN', 'Return'), ('LATE', 'Late')], default='WITHDRAW', max_length=30)),
                ('accept_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='issue_book_for_accept_by', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='issue_book_for_book', to='book.Book')),
                ('issue_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='issue_book_for_issue_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='issue_book_for_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
