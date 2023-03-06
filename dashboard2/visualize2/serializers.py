from rest_framework import serializers
from .models import DataData

class DataDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataData
        fields = ['id','end_year','intensity','sector','topic','url','region','start_year','impact','insight','added','published','country','relevance','pestle','source','title','likelihood']