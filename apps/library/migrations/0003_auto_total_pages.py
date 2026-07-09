from django.db import migrations, models


WORDS_PER_READER_PAGE = 140


def recalculate_total_pages(apps, schema_editor):
    Book = apps.get_model('library', 'Book')

    for book in Book.objects.all():
        word_count = len((book.text or '').split())
        total_pages = 1

        if word_count:
            total_pages = max(
                1,
                (word_count + WORDS_PER_READER_PAGE - 1) // WORDS_PER_READER_PAGE,
            )

        Book.objects.filter(pk=book.pk).update(total_pages=total_pages)


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='total_pages',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
        migrations.RunPython(recalculate_total_pages, migrations.RunPython.noop),
    ]
