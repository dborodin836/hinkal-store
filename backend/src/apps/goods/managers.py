from django.db import models


class DishManager(models.Manager):
    """
    Manager for the Dish model for handling common tasks.
    """

    def best_selling(self, amount: int):
        """
        Return specified amount of best-selling products.
        """
        return self.order_by('-times_bought')[:amount]
