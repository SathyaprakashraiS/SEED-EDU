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
from quespaper.models import *
from date.models import *
from other.models import *
#from django.contrib.main.custom import User

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
		model = Statecollege
		fields ='__all__'

class CcollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Citycollege
		fields ='__all__'

class CbcollegeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coursebasedcollege
		fields ='__all__'

#question papers
class PaperSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paper
		fields ='__all__'

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
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

class DateSerializer(serializers.ModelSerializer):
	class Meta:
		model = events
		fields ='__all__'

class QPbankSerializer(serializers.ModelSerializer):
	class Meta:
		model = QPM
		fields ='__all__'

class QpapersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paper
		fields ='__all__'

class NotesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notes
		fields ='__all__'

class TipsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tips
		fields ='__all__'

class OnlinecoursesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Onlinecourses
		fields ='__all__'

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Videos
		fields ='__all__'

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = AddquizT
		fields ='__all__'

class AttquizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qanswersheet
		fields ='__all__'

class QuizansSerializer(serializers.ModelSerializer):
	class Meta:
		model = AddquestionT
		fields ='__all__'

class QresultSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qanswersheet
		fields ='__all__'

class MockSerializer(serializers.ModelSerializer):
	class Meta:
		model = MockPM
		fields ='__all__'

class AttMockSerializer(serializers.ModelSerializer):
	class Meta:
		model = MockAnswer
		fields ='__all__'