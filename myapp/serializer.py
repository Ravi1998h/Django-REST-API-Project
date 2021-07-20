from  rest_framework import serializers
from myapp.models import Employee


class EmployeeSerializer(serializers.Serializer):
    #validation by validators
    def s(value):
        if value<10000:
            raise exeption('salary must be greter than 1000')
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=40)
    esal=serializers.FloatField(validators=[s])
    eaddr=serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance


        #Field level validation
    #def validate_esal(self,value):
        #if value<10000:
            #raise exeption('roll no must be above 10000')
        #return value


        #object level validation
    #def validate(self,data):  #data contains all fields
        #eno=data.get('eno')
        #esal=data.get('esal')
        #if eno<1000:
            #raise exeption ('eno must be greater than 1000')
        #return data
