from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CharField, ForeignKey, CASCADE, ManyToManyField
from apps.books import models
from apps.users.utils import avatar_path
from apps.shared.models import AbstractModel


class User(AbstractUser):
    avatar = models.ImageField(upload_to=avatar_path, default='humble.jpg')
    middle_name = CharField(max_length=128)


class BookShelf(AbstractModel):
    name = CharField(max_length=128)
    user = ForeignKey("users.User", CASCADE, 'bookshelf')
    books = ManyToManyField("books.Book", "bookshelves")
