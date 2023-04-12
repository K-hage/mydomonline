from rest_framework import serializers

from core.models import Property, Entity


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(
        label='Значение',
        help_text='Введите значение')
    properties = serializers.SerializerMethodField(
        read_only=True,
    )

    def get_properties(self, obj):
        properties = obj.properties.all()
        return {prop.key: prop.value for prop in properties}

    def is_valid(self, *, raise_exception=False):
        self.initial_data['value'] = self.initial_data.pop("data[value]")
        return super().is_valid(raise_exception=raise_exception)

    class Meta:
        model = Entity
        fields = '__all__'
        read_only_fields = (
            'id',
            'modified_by',
        )
