from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):
	
	def test_new_superuser(self):
		db = get_user_model()
		super_user = db.objects.create_superuser(
			'testuser@super.com', 'user_name', 'firstname', 'password')
		
		self.assertEqual(super_user.email, 'testuser@super.com')
		self.assertEqual(super_user.user_name, 'username')
		self.assertEqual(super_user.first_name, 'firstname')
		self.assertTrue(super_user.is_superuser)
		self.assertTrue(super_user.is_staff)
		self.assertTrue(super_user.is_active)
		self.assertEqual(str(super_user.email), 'username')
		
		with self.assertRaises(ValueError):
			db.objects.create_superuser(
				email='testuser@super.com', user_name='user_name', first_name='firstname', password='password', is_superuser=False)
			
		with self.assertRaises(ValueError):
			db.objects.create_superuser(
				email='testuser@super.com', user_name='user_name', first_name='firstname', password='password', is_staff=False)
	
	
	def test_new_user(self):
		db = get_user_model()
		user = db.objects.create_user(
			'testuser@super.com', 'user_name', 'firstname', 'password')
		
		self.assertEqual(user.email, 'testuser@super.com')
		self.assertEqual(user.user_name, 'username')
		self.assertEqual(user.first_name, 'firstname')
		self.assertTrue(user.is_superuser)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_active)
		
		with self.assertRaises(ValueError):
			db.objects.create_user(
				email='', user_name='u', first_name='first_name', password='password')
