# Model field reference

__null__
 True값이면 database에 NULL값을 넣을 수 있다. Dufault는 Falsel이다.
 
 __blank__
 True값이면 null과는 다르게 ''빈 문자열과 같은 값을 넣을 수 있다.
 
 __choices__
 list나 tuple로 구성된 iterable 가능해야한다. 두 가지 요소로 묶여야 하는데 첫 번째 값은 모델에서 사용되는 실제 값이고, 두 번째 값은 사람이 읽기 편한 요소이다.
 
 
 	YEAR_IN_SHCOOL_CHOICES = (
	 	('FR', 'Freshman'),
	 	('SO', 'Sophomore'),
 		('FR', 'Junior'),
 		('FR', 'Senior'),
	 )

다음과 같이 사용할 수 있다.

	from django.db import models
	
	class Student(models.Model):
    	FRESHMAN = 'FR'
  	    SOPHOMORE = 'SO'
    	JUNIOR = 'JR'
    	SENIOR = 'SR'
    	YEAR_IN_SCHOOL_CHOICES = (
        	(FRESHMAN, 'Freshman'),
        	(SOPHOMORE, 'Sophomore'),
        	(JUNIOR, 'Junior'),
        	(SENIOR, 'Senior'),
    	)
    	year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
   		)

    	def is_upperclass(self):
        	return self.year_in_school in (self.JUNIOR, self.SENIOR)
        	
**db__column**
**db__index**
**db__tablespace**
**default**
**editable**

**error_messages**

**help_text**
**primary_key**
**unique**
**unique_for_date**
**unique_for_month**
**unique_for_year**
**verbose_name**
**validators**
**AutoFIeld**
**BigAutoField**
**BinaryField**
**BooleanField**
**CharField**
**CommaSeparatedIntegerFIeld**
**DateField**
**DateTimeField**
**DecimalField**
**DurationField**
**EmailFIeld**
**FileField**
**FilePathField**
**FloatField**
**ImageField**
**IntegerField**
**GenericIPAddressField**
**NullBooleanField**
**PositiveIntegerField**
**PositiveSmallIntegerField**
**SlugField**
**SmallIntegerField**
**TextField**
**TimeField**
**URLField**

