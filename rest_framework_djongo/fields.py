from bson import ObjectId
from bson.errors import InvalidId
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class ObjectIdField(serializers.Field):
    """ Field for ObjectId values """

    def to_internal_value(self, value):
        try:
            return ObjectId(smart_str(value))
        except InvalidId:
            raise serializers.ValidationError("'%s' is not a valid ObjectId" % value)

    def to_representation(self, value):
        return smart_str(value)


class EmbeddedField(serializers.Field):
    default_error_messages = {
        'not_a_dict': serializers.DictField.default_error_messages['not_a_dict'],
        'undefined_model': _('Document `{doc_cls}` has not been defined.'),
        'missing_class': _('Provided data has not `_cls` item.')
    }

    def to_internal_value(self, value):
        return value

    def to_representation(self, value):
        return value
