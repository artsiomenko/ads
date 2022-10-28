import datetime

from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
import factory

from main.models import Ad, Rubric


class RubricFactory(DjangoModelFactory):
    class Meta:
        model = Rubric

    name = 'Real estate'


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'Angelika'
    email = 'angelichka21.02@gmail.com'
    password1 = 'SavoskoSasha21'
    password2 = 'SavoskoSasha21'
    first_name = 'Anzhalika'
    last_name = 'Artsiomenka'


class BbFactory(DjangoModelFactory):
    class Meta:
        model = Ad

    title = 'House'
    content = 'House'
    price = 50000000
    author = factory.SubFactory(UserFactory)
    rubric = factory.SubFactory(RubricFactory)



