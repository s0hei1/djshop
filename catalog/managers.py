from django.db.models import QuerySet


class CategoryQuerySet(QuerySet):
    def visibility(self):
        return self.filter(visibility=True)
