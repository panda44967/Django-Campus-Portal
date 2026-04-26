from django.test import SimpleTestCase
from django.urls import reverse


class CampusURLStatusCodeTests(SimpleTestCase):
    """URL status code tests"""

    def test_home_status_code(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_clubs_status_code(self):
        response = self.client.get('/clubs/')
        self.assertEqual(response.status_code, 200)

    def test_schedule_status_code(self):
        response = self.client.get('/schedule/')
        self.assertEqual(response.status_code, 200)

    def test_faq_status_code(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


class CampusReverseURLTests(SimpleTestCase):
    """reverse() by name tests"""

    def test_home_reverse(self):
        url = reverse('campus:home')
        self.assertEqual(url, '/home/')

    def test_clubs_reverse(self):
        url = reverse('campus:clubs')
        self.assertEqual(url, '/clubs/')

    def test_schedule_reverse(self):
        url = reverse('campus:schedule')
        self.assertEqual(url, '/schedule/')

    def test_faq_reverse(self):
        url = reverse('campus:faq')
        self.assertEqual(url, '/faq/')

    def test_about_reverse(self):
        url = reverse('campus:about')
        self.assertEqual(url, '/about/')


class CampusTemplateTests(SimpleTestCase):
    """assertTemplateUsed tests"""

    def test_home_template_used(self):
        response = self.client.get(reverse('campus:home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_clubs_template_used(self):
        response = self.client.get(reverse('campus:clubs'))
        self.assertTemplateUsed(response, 'clubs.html')

    def test_schedule_template_used(self):
        response = self.client.get(reverse('campus:schedule'))
        self.assertTemplateUsed(response, 'schedule.html')

    def test_faq_template_used(self):
        response = self.client.get(reverse('campus:faq'))
        self.assertTemplateUsed(response, 'faq.html')

    def test_about_template_used(self):
        response = self.client.get(reverse('campus:about'))
        self.assertTemplateUsed(response, 'about.html')


class CampusContentTests(SimpleTestCase):
    """assertContains tests"""

    def test_home_contains_hub(self):
        response = self.client.get(reverse('campus:home'))
        self.assertContains(response, 'Campus Activity Hub')

    def test_home_contains_club_directory(self):
        response = self.client.get(reverse('campus:home'))
        self.assertContains(response, 'Club Directory')

    def test_clubs_contains_robotics(self):
        response = self.client.get(reverse('campus:clubs'))
        self.assertContains(response, 'Robotics Club')

    def test_clubs_contains_photography(self):
        response = self.client.get(reverse('campus:clubs'))
        self.assertContains(response, 'Photography Club')

    def test_schedule_contains_monday(self):
        response = self.client.get(reverse('campus:schedule'))
        self.assertContains(response, 'Monday')

    def test_faq_contains_registration(self):
        response = self.client.get(reverse('campus:faq'))
        self.assertContains(response, 'Registration')

    def test_about_contains_about_title(self):
        response = self.client.get(reverse('campus:about'))
        self.assertContains(response, 'About This Site')

    def test_base_nav_links_present(self):
        response = self.client.get(reverse('campus:home'))
        self.assertContains(response, '/clubs/')
        self.assertContains(response, '/schedule/')
