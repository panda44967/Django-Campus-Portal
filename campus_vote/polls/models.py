from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name='題目標題')
    pub_date = models.DateTimeField(verbose_name='發布時間')
    description = models.TextField(verbose_name='題目描述')
    is_open = models.BooleanField(default=True, verbose_name='是否開放')

    class Meta:
        ordering = ['pub_date']
        verbose_name = '投票題目'
        verbose_name_plural = '投票題目'

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='所屬題目',
    )
    choice_text = models.CharField(max_length=200, verbose_name='選項文字')
    votes = models.IntegerField(default=0, verbose_name='票數')

    class Meta:
        ordering = ['-votes']
        verbose_name = '選項'
        verbose_name_plural = '選項'

    def __str__(self):
        return self.choice_text
