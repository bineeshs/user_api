from rest_framework.test import APIClient
from users.models import User
import io

client = APIClient()
url = '/api_user/upload-csv/'

def new_file():
    
    csv_data = """name,email,age
    alen,alen@example.com,40
    ally,ally@example.com,60"""
    file = io.StringIO(csv_data)
    file.name = 'test.csv'

    response = client.post(url, {'file': file}, format='multipart')
    print(response.status_code)
    print(response.data)
    print(User.objects.count())

def invalid_file():
    csv_data = """name,email,age
        John Doe,invalid_email,130"""
    file = io.StringIO(csv_data)
    file.name = 'test.csv'

    response = client.post(url, {'file': file}, format='multipart')
    print(response.status_code)
    print(response.data)
    print(User.objects.count())

def test_duplicate_email():
    User.objects.create(name='John Doe', email='john@example.com', age=30)
    csv_data = """name,email,age
        John Doe,john@example.com,30"""
    file = io.StringIO(csv_data)
    file.name = 'test.csv'

    response = client.post(url, {'file': file}, format='multipart')
    print(response.status_code)
    print(response.data)
    print(User.objects.count())

