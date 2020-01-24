from django.test import TestCase
from .models import Book, Editorial

class EditorialModelTest(TestCase):

	@classmethod
	
	def setUpTestData(cls):
		Editorial.objects.create(name="Arbol")

	def test_name_label(self):
		title = Editorial.objects.get(id=1)
		field_label = title._meta.get_field('name').verbose_name
		self.assertEquals(field_label,'name')


	def test_title_max_length(self):
		title = Editorial.objects.get(id=1)
		max_length = title._meta.get_field('name').max_length
		self.assertEquals(max_length,100)


class BookModelTest(TestCase):

	@classmethod
	
	def setUpTestData(cls):
		editorial = Editorial.objects.create(name="Arbol")
		Book.objects.create(name="Don Quijote de la Mancha",autor="Cervantes", editorial=editorial)

	def test_title_label(self):
		title = Book.objects.get(id=1)
		field_label = title._meta.get_field('name').verbose_name
		self.assertEquals(field_label,'name')

	def test_autor_label(self):
		title = Book.objects.get(id=1)
		field_label = title._meta.get_field('autor').verbose_name
		self.assertEquals(field_label,'autor')

	def test_name_max_length(self):
		title = Book.objects.get(id=1)
		max_length = title._meta.get_field('name').max_length
		self.assertEquals(max_length,100)

	def test_autor_max_length(self):
		title = Book.objects.get(id=1)
		max_length = title._meta.get_field('autor').max_length
		self.assertEquals(max_length,100)

	def test_gender_label(self):
		title = Book.objects.get(id=1)
		field_label = title._meta.get_field('gender').verbose_name
		self.assertEquals(field_label,'gender')

	def test_gender_max_length(self):
		title = Book.objects.get(id=1)
		max_length = title._meta.get_field('gender').max_length
		self.assertEquals(max_length,100)



# Create your tests here.
