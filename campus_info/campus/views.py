from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse


# ──────────────────────────────────────────────
# home/ ── function-based view（必須）
# ──────────────────────────────────────────────
def home_view(request):
    sections = [
        {
            'title': 'Club Directory',
            'desc': 'Browse campus clubs, advisors, officers, and recent activities.',
            'url': reverse('campus:clubs'),
        },
        {
            'title': 'Weekly Schedule',
            'desc': "Review this week's activity table with noted events for each time slot.",
            'url': reverse('campus:schedule'),
        },
        {
            'title': 'Frequently Asked Questions',
            'desc': 'See categorized questions built from view-provided context data.',
            'url': reverse('campus:faq'),
        },
    ]
    context = {'sections': sections}
    return render(request, 'home.html', context)


# ──────────────────────────────────────────────
# clubs/ ── CBV with get_context_data() override
# ──────────────────────────────────────────────
class ClubsView(TemplateView):
    template_name = 'clubs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubs'] = [
            {
                'name': 'Robotics Club',
                'advisor': 'Prof. Chen',
                'officers': [
                    {'name': 'Alice', 'role': 'President'},
                    {'name': 'Kevin', 'role': 'Vice President'},
                    {'name': 'Maria', 'role': 'Treasurer'},
                ],
                'recent_activities': [
                    'Line-following practice',
                    'Arduino workshop',
                    'Competition prep',
                ],
            },
            {
                'name': 'Photography Club',
                'advisor': 'Prof. Yang',
                'officers': [
                    {'name': 'Brian', 'role': 'President'},
                    {'name': 'Ella', 'role': 'Secretary'},
                    {'name': 'Rhea', 'role': 'Event Lead'},
                ],
                'recent_activities': [
                    'Night photo walk',
                    'Portrait basics',
                    'Editing clinic',
                ],
            },
            {
                'name': 'Music Club',
                'advisor': 'Prof. Lin',
                'officers': [
                    {'name': 'Sam', 'role': 'President'},
                    {'name': 'Sophie', 'role': 'Band Captain'},
                    {'name': 'Terry', 'role': 'Equipment Lead'},
                ],
                'recent_activities': [
                    'Choir rehearsal',
                    'Open mic night',
                    'Spring showcase',
                ],
            },
            {
                'name': 'Volunteer Service Club',
                'advisor': 'Prof. Hsu',
                'officers': [
                    {'name': 'Dana', 'role': 'President'},
                    {'name': 'Leo', 'role': 'Coordinator'},
                    {'name': 'Nora', 'role': 'Outreach Lead'},
                ],
                'recent_activities': [
                    'Beach cleanup',
                    'Food drive',
                    'Hospital visit',
                ],
            },
        ]
        return context


# ──────────────────────────────────────────────
# schedule/ ── function-based view (巢狀資料)
# ──────────────────────────────────────────────
def schedule_view(request):
    schedule = [
        {
            'day': 'Monday',
            'periods': [
                {
                    'name': 'Morning',
                    'activities': [
                        {'name': 'Freshman orientation', 'location': 'Main Hall', 'online': False},
                        {'name': 'Coding warm-up', 'location': 'Lab 4', 'online': False},
                    ],
                },
                {
                    'name': 'Noon',
                    'activities': [
                        {'name': 'Free lab', 'location': 'Space 204', 'online': False},
                    ],
                },
                {
                    'name': 'Afternoon',
                    'activities': [
                        {'name': 'Basketball trial', 'location': 'Gym', 'online': False},
                        {'name': 'Debate prep', 'location': 'Room 401', 'online': False},
                    ],
                },
            ],
        },
        {
            'day': 'Tuesday',
            'periods': [
                {
                    'name': 'Morning',
                    'activities': [
                        {'name': 'English corner', 'location': 'Language Center', 'online': False},
                    ],
                },
                {
                    'name': 'Noon',
                    'activities': [
                        {'name': 'Scholarship briefing', 'location': 'Student Office', 'online': True},
                        {'name': 'Community lunch', 'location': 'Garden', 'online': False},
                    ],
                },
                {
                    'name': 'Afternoon',
                    'activities': [
                        {'name': 'Photography walk', 'location': 'Campus Gate', 'online': False},
                    ],
                },
            ],
        },
        {
            'day': 'Wednesday',
            'periods': [
                {
                    'name': 'Morning',
                    'activities': [
                        {'name': 'Math clinic', 'location': 'Room 303', 'online': False},
                        {'name': 'Resume review', 'location': 'Career Center', 'online': True},
                    ],
                },
                {
                    'name': 'Noon',
                    'activities': [
                        {'name': 'Club fair booth setup', 'location': 'Courtyard', 'online': False},
                    ],
                },
                {
                    'name': 'Afternoon',
                    'activities': [
                        {'name': 'Jazz rehearsal', 'location': 'Music Room', 'online': False},
                    ],
                },
            ],
        },
        {
            'day': 'Thursday',
            'periods': [
                {
                    'name': 'Morning',
                    'activities': [
                        {'name': 'Volunteer briefing', 'location': 'Room 110', 'online': True},
                    ],
                },
                {
                    'name': 'Noon',
                    'activities': [
                        {'name': 'Health workshop', 'location': 'Nursing Lab', 'online': False},
                    ],
                },
                {
                    'name': 'Afternoon',
                    'activities': [
                        {'name': 'Prototype testing', 'location': 'Maker Space', 'online': False},
                        {'name': 'Peer mentoring', 'location': 'Library', 'online': False},
                    ],
                },
            ],
        },
        {
            'day': 'Friday',
            'periods': [
                {
                    'name': 'Morning',
                    'activities': [
                        {'name': 'Morning assembly', 'location': 'Main Hall', 'online': False},
                    ],
                },
                {
                    'name': 'Noon',
                    'activities': [],  # 刻意留空，示範 {% empty %}
                },
                {
                    'name': 'Afternoon',
                    'activities': [
                        {'name': 'Movie discussion', 'location': 'Media Room', 'online': True},
                        {'name': 'Sports-day planning', 'location': 'Gym Office', 'online': False},
                    ],
                },
            ],
        },
    ]
    context = {'schedule': schedule}
    return render(request, 'schedule.html', context)


# ──────────────────────────────────────────────
# faq/ ── function-based view
# ──────────────────────────────────────────────
def faq_view(request):
    categories = [
        {
            'name': 'Registration',
            'questions': [
                {'q': 'How do I register for an event?',
                 'a': 'Visit the event page and click the Register button.'},
                {'q': 'Can I join more than one club at the same time?',
                 'a': 'Yes, there is no limit on club membership.'},
            ],
        },
        {
            'name': 'Attendance',
            'questions': [
                {'q': 'Do I need to sign in before each activity?',
                 'a': 'Yes, please scan the QR code at the entrance.'},
                {'q': 'What happens if an event moves online?',
                 'a': 'You will receive an email with the meeting link.'},
            ],
        },
        {
            'name': 'New Students',
            'questions': [
                {'q': 'Questions will be added soon.', 'a': ''},
            ],
        },
        {
            'name': 'Upcoming Events',
            'questions': [],  # 刻意留空，觸發 {% empty %}
        },
    ]
    context = {'categories': categories}
    return render(request, 'faq.html', context)


# ──────────────────────────────────────────────
# about/ ── TemplateView（必須）
# ──────────────────────────────────────────────
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About This Site'
        context['description'] = (
            'This demo project shows how to organize a small information site '
            'with function-based and class-based views.'
        )
        context['checklist'] = [
            'Only one app is used in this project.',
            'All templates extend base.html.',
            'The data comes from view context instead of hard-coded template blocks.',
        ]
        return context
