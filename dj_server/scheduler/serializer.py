from rest_framework import serializers
 
from scheduler.models import Schedule
 
class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
 
    class Meta:
        model = Schedule
        fields = ('url', 'id', 'created', 'name', 'user')
        extra_kwargs = {
            'url': {
                'view_name': 'schedule:schedule-detail',
            }
}