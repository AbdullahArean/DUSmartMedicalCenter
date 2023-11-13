from django.db import models


class DocumentBaseFactory(models.Model):
    common_variable = None

    class Meta:
        abstract = True

    @classmethod
    def create_document(cls, **kwargs):
        if cls.common_variable is None:
            raise NotImplementedError("Subclasses must define a value for common_variable")
        kwargs['common_variable'] = cls.common_variable
        return cls.objects.create(**kwargs)
