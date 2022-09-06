from rest_framework import serializers
from book.models import *
from college.models import *
from course.models import *
from date.models import *
from exam.models import *
from help.models import *
from main.models import *
from rankloc.models import *
from quespaper.models import *
from student.models import *
from teacher.models import *


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Books
		fields ='__all__'

class AcollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Allcollege
		fields ='__all__'

class TcollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Topcollege
		fields ='__all__'

class DcollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Degreecollege
		fields ='__all__'

class ScollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Allcollege
		fields ='__all__'

class CcollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Citycollege
		fields ='__all__'

class CbcollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coursebasedcollege
		fields ='__all__'

class ArtSerializer(serializers.ModelSerializer):
	class Meta:
		model = Art
		fields ='__all__'

class ScienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Science
		fields ='__all__'

class CommerceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Commerce
		fields ='__all__'

class EngineeringSerializer(serializers.ModelSerializer):
	class Meta:
		model = Engineering
		fields ='__all__'

class ProcourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Professional
		fields ='__all__'