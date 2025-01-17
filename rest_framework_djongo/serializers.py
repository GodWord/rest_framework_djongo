from django.db import models
from djongo import models as djo_models
from rest_framework import fields as drf_fields
from rest_framework import serializers

from . import fields as drf_djo_fields


class GenericDjongoSerializer(serializers.ModelSerializer):
    """
    Serializer for GenericDjongoModel.
    """
    serializer_field_mapping = {
        models.AutoField: drf_fields.IntegerField,
        models.BigIntegerField: drf_fields.IntegerField,
        models.BooleanField: drf_fields.BooleanField,
        models.CharField: drf_fields.CharField,
        models.CommaSeparatedIntegerField: drf_fields.CharField,
        models.DateField: drf_fields.DateField,
        models.DateTimeField: drf_fields.DateTimeField,
        models.DecimalField: drf_fields.DecimalField,
        models.DurationField: drf_fields.DurationField,
        models.EmailField: drf_fields.EmailField,
        models.Field: drf_fields.ModelField,
        models.FileField: drf_fields.FileField,
        models.FloatField: drf_fields.FloatField,
        models.ImageField: drf_fields.ImageField,
        models.IntegerField: drf_fields.IntegerField,
        models.NullBooleanField: drf_fields.BooleanField,
        models.PositiveIntegerField: drf_fields.IntegerField,
        models.PositiveSmallIntegerField: drf_fields.IntegerField,
        models.SlugField: drf_fields.SlugField,
        models.SmallIntegerField: drf_fields.IntegerField,
        models.TextField: drf_fields.CharField,
        models.TimeField: drf_fields.TimeField,
        models.URLField: drf_fields.URLField,
        models.UUIDField: drf_fields.UUIDField,
        models.GenericIPAddressField: drf_fields.IPAddressField,
        models.FilePathField: drf_fields.FilePathField,

        djo_models.ObjectIdField: drf_djo_fields.ObjectIdField,
        djo_models.EmbeddedField: drf_djo_fields.EmbeddedField,
        djo_models.GenericObjectIdField: drf_djo_fields.ObjectIdField,
        djo_models.JSONField: drf_fields.JSONField,
        # djo_models.ArrayField: drfd_fields.ObjectIdField,
        # djo_models.ArrayReferenceField: drf_djo_fields.ObjectIdField,

    }

    def get_default_field_names(self, declared_fields, model_info):
        return (
                list(declared_fields.keys())
                + list(model_info.fields_and_pk.keys())
        )


class EmbeddedSerializer(GenericDjongoSerializer):
    """
    Serializer for Embedded.
    """
    _saving_instances = False

    def get_unique_together_validators(self):
        # skip the valaidators
        return []

# class JSONField(serializers.Field):
#     def to_representation(self, value):
#         return value


# default_error_messages = {
#     'invalid_type': _("Geometry must be a geojson geometry or a geojson coordinates, got {input_value}."),
#     'invalid_geotype': _("Geometry expected to be '{exp_type}', got {geo_type}."),
# }
# valid_geo_types = {
#     'Point': me_fields.PointField,
#     'LineString': me_fields.LineStringField,
#     'Polygon': me_fields.PolygonField,
#     'MultiPoint': me_fields.MultiPointField,
#     'MultiLineString': me_fields.MultiLineStringField,
#     'MultiPolygon': me_fields.MultiPolygonField
# }
#
# def __init__(self, geo_type, *args, **kwargs):
#     assert geo_type in self.valid_geo_types
#     self.mongo_field = self.valid_geo_types[geo_type]
#     super(GeoJSONField, self).__init__(*args, **kwargs)
