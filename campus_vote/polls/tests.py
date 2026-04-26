from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question, Choice


class QuestionModelTests(TestCase):
    """Model 欄位、__str__、ForeignKey 測試"""

    @classmethod
    def setUpTestData(cls):
        cls.q = Question.objects.create(
            title='是否需要增設飲水機？',
            pub_date=timezone.now(),
            description='校園共有 50 台飲水機，請問是否需要增設？',
            is_open=False,
        )
        cls.q_open = Question.objects.create(
            title='下學期社團博覽會要延長幾時上線？',
            pub_date=timezone.now(),
            description='請投票決定社團博覽會的上線時間。',
            is_open=True,
        )
        cls.c1 = Choice.objects.create(
            question=cls.q,
            choice_text='是，目前嚴重不足',
            votes=12,
        )
        cls.c2 = Choice.objects.create(
            question=cls.q,
            choice_text='否，已有足夠',
            votes=8,
        )
        cls.c3 = Choice.objects.create(
            question=cls.q,
            choice_text='可增設部分樓層',
            votes=3,
        )

    # ── model 欄位內容測試 ──
    def test_question_title_field(self):
        self.assertEqual(self.q.title, '是否需要增設飲水機？')

    def test_question_description_field(self):
        self.assertIn('飲水機', self.q.description)

    def test_question_is_open_false(self):
        self.assertFalse(self.q.is_open)

    def test_question_is_open_true(self):
        self.assertTrue(self.q_open.is_open)

    def test_choice_votes_field(self):
        self.assertEqual(self.c1.votes, 12)

    def test_choice_text_field(self):
        self.assertEqual(self.c1.choice_text, '是，目前嚴重不足')

    # ── __str__() 測試 ──
    def test_question_str(self):
        self.assertEqual(str(self.q), '是否需要增設飲水機？')

    def test_choice_str(self):
        self.assertEqual(str(self.c1), '是，目前嚴重不足')

    # ── ForeignKey 關聯正確性 ──
    def test_choice_fk_links_to_question(self):
        self.assertEqual(self.c1.question, self.q)

    def test_question_reverse_choice_set(self):
        choices = self.q.choice_set.all()
        self.assertIn(self.c1, choices)
        self.assertIn(self.c2, choices)
        self.assertIn(self.c3, choices)

    def test_choice_set_count(self):
        self.assertEqual(self.q.choice_set.count(), 3)


class PollsURLTests(TestCase):
    """URL by path / by name 測試"""

    @classmethod
    def setUpTestData(cls):
        cls.q = Question.objects.create(
            title='Test Question for URL',
            pub_date=timezone.now(),
            description='URL test description.',
            is_open=True,
        )

    def test_home_url_by_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_by_name(self):
        response = self.client.get(reverse('polls:home'))
        self.assertEqual(response.status_code, 200)

    def test_detail_url_by_path(self):
        response = self.client.get(f'/question/{self.q.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_detail_url_by_name(self):
        url = reverse('polls:question_detail', kwargs={'pk': self.q.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_stats_url_by_path(self):
        response = self.client.get('/stats/')
        self.assertEqual(response.status_code, 200)

    def test_stats_url_by_name(self):
        response = self.client.get(reverse('polls:stats'))
        self.assertEqual(response.status_code, 200)


class PollsTemplateTests(TestCase):
    """template name / template content 測試"""

    @classmethod
    def setUpTestData(cls):
        cls.q = Question.objects.create(
            title='社團博覽會投票',
            pub_date=timezone.now(),
            description='請選擇你偏好的社團博覽會舉辦方式。',
            is_open=True,
        )
        Choice.objects.create(question=cls.q, choice_text='實體舉辦', votes=5)
        Choice.objects.create(question=cls.q, choice_text='線上舉辦', votes=3)

    def test_home_template_name(self):
        response = self.client.get(reverse('polls:home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_template_name(self):
        url = reverse('polls:question_detail', kwargs={'pk': self.q.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'question_detail.html')

    def test_stats_template_name(self):
        response = self.client.get(reverse('polls:stats'))
        self.assertTemplateUsed(response, 'stats.html')

    def test_home_shows_question_title(self):
        """首頁能正確顯示資料庫建立的測試資料"""
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, '社團博覽會投票')

    def test_home_shows_choice_text(self):
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, '實體舉辦')

    def test_detail_shows_description(self):
        url = reverse('polls:question_detail', kwargs={'pk': self.q.pk})
        response = self.client.get(url)
        self.assertContains(response, '社團博覽會舉辦方式')

    def test_stats_shows_total_count(self):
        response = self.client.get(reverse('polls:stats'))
        self.assertContains(response, '問題總數')
