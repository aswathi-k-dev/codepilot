from rest_framework import serializers
from exams.models import Assessment

from datetime import date

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"
        read_only_fields = ["id","end_time","created_by"]

        def validate_exam_date(self,value):

            if value < date.today():
                raise serializers.ValidationError("previous date is not allowed")
            return value