from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField
from apps.utils.image_storage import ImageStorage


class CategoryFirst(models.Model):
    name = models.CharField(max_length=20, verbose_name='类名', unique=True)

    class Meta:
        verbose_name = '一级类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @staticmethod
    def get_category_first():
        return CategoryFirst.objects.order_by('name').all()


class CategorySecond(models.Model):
    name = models.CharField(max_length=20, verbose_name='类名', unique=True)
    up = models.ForeignKey(
        CategoryFirst,
        related_name='down',
        on_delete=models.CASCADE,
        verbose_name='上级')

    class Meta:
        verbose_name = '二级类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @staticmethod
    def get_category_second(category_id):
        return CategorySecond.objects.get(id=category_id)


class Book(models.Model):
    category = models.ForeignKey(
        CategorySecond,
        related_name='books',
        on_delete=models.DO_NOTHING,
        verbose_name='类别')
    name = models.CharField(max_length=50, verbose_name='书名')
    image = models.ImageField(
        upload_to='books/%Y/%m/', storage=ImageStorage(), verbose_name='封面')
    author = models.CharField(max_length=100, verbose_name='作者')
    translator = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='译者')
    press = models.CharField(max_length=50, verbose_name='出版社')
    revision = models.PositiveSmallIntegerField(verbose_name='版次')
    published_date = models.DateField(verbose_name='出版日期')
    added_time = models.DateTimeField(auto_now_add=True, verbose_name='上架时间')
    page_numbers = models.PositiveSmallIntegerField(verbose_name='页数')
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='定价')
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='折后价')
    discount = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name='折扣')
    stock = models.PositiveIntegerField(verbose_name='存货量')
    sales = models.PositiveIntegerField(verbose_name='销售量')
    content_brief = UEditorField(blank=True, null=True, verbose_name='内容简介')
    author_brief = UEditorField(blank=True, null=True, verbose_name='作者简介')
    catalog = UEditorField(blank=True, null=True, verbose_name='目录')

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @staticmethod
    def get_new_hot_books(current_category=None):
        start = timezone.now().date() + timezone.timedelta(days=-30)
        if current_category:
            # new_hot_books = current_category.books.filter(
            #     added_time__gte=start).order_by('-sales').all()[:10]
            new_hot_books = current_category.books.order_by('-sales').all()[:10]
        else:
            # new_hot_books = Book.objects.filter(
            #     added_time__gte=start).order_by('-sales').all()[:10]
            new_hot_books = Book.objects.order_by('-sales').all()[:10]
        return new_hot_books

    @staticmethod
    def get_hot_books(current_category=None):
        if current_category:
            hot_books = current_category.books.order_by('-sales').all()[:10]
        else:
            hot_books = Book.objects.order_by('-sales').all()[:10]
        return hot_books

    @staticmethod
    def get_recommend_hot_books(current_category=None):
        import random
        if current_category:
            recommend_hot_books = current_category.books.order_by(
                '-sales').all()[:50]
        else:
            recommend_hot_books = Book.objects.order_by('-sales').all()[:50]
        indexes = list(range(len(recommend_hot_books)))
        random.shuffle(indexes)
        result = []
        for i in range(len(recommend_hot_books)):
            result.append(recommend_hot_books[indexes[i]])
        recommend_hot_books = result[:10]
        return recommend_hot_books

    @staticmethod
    def get_new_books(current_category=None):
        if current_category:
            new_books = current_category.books.order_by(
                '-added_time').all()[:10]
        else:
            new_books = Book.objects.order_by('-added_time').all()[:10]
        return new_books


class Comment(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='图书')
    from apps.users.models import UserProfile
    user = models.ForeignKey(
        UserProfile,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='用户')
    score = models.PositiveSmallIntegerField(default=5, verbose_name='评分')
    content = models.TextField(max_length=200, verbose_name='评论')
    published_time = models.DateTimeField(
        auto_now_add=True, verbose_name='发表时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book.name
