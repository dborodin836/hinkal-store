import datetime
import pytz
from django.test.testcases import TestCase

from src.apps.goods.models import Dish, Category


class CategoryModelTest(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name="test")

    def test_str(self):
        self.assertEqual(str(self.category), self.category.name)


class DishModelTest(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name="test")
        self.dish1 = Dish.objects.create(
            title="test1",
            description="test1",
            price=120.12,
            times_bought=11210,
            created_at=datetime.datetime(1, 1, 1, 1, 1, tzinfo=pytz.UTC),
            category=category,
        )
        self.dish2 = Dish.objects.create(
            title="test2",
            description="test2",
            price=120.121,
            times_bought=10,
            created_at=datetime.datetime(1, 1, 1, 1, 1, tzinfo=pytz.UTC),
            category=category,
        )
        self.dish3 = Dish.objects.create(
            title="test3",
            description="test3",
            price=120.121,
            times_bought=101,
            created_at=datetime.datetime(1, 1, 1, 1, 1, tzinfo=pytz.UTC),
            category=category,
        )

    def test_best_selling(self):
        q = Dish.objects.best_selling_active(10)
        self.assertEqual(list(q), [self.dish1, self.dish3, self.dish2])
        self.assertTrue(
            all(q[index - 1].times_bought > q[index].times_bought for index in range(1, len(q)))
        )

    def test_str(self):
        self.assertEqual(self.dish1.title, str(self.dish1))
