from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='題目標題')),
                ('pub_date', models.DateTimeField(verbose_name='發布時間')),
                ('description', models.TextField(verbose_name='題目描述')),
                ('is_open', models.BooleanField(default=True, verbose_name='是否開放')),
            ],
            options={
                'verbose_name': '投票題目',
                'verbose_name_plural': '投票題目',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='選項文字')),
                ('votes', models.IntegerField(default=0, verbose_name='票數')),
                ('question', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='polls.question',
                    verbose_name='所屬題目',
                )),
            ],
            options={
                'verbose_name': '選項',
                'verbose_name_plural': '選項',
                'ordering': ['-votes'],
            },
        ),
    ]
