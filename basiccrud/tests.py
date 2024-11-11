from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from basiccrud.models import Todo
from basiccrud.serliazers import TodoSerializer


# Create your tests here.
# Tests for model
class TodoModel(TestCase):
    def setUp(self):
        Todo.objects.create(name='task 1')
        Todo.objects.create(name='task 2')
    
    def test_todo_task_name(self):
        obj1 = Todo.objects.get(name='task 1')
        obj2 = Todo.objects.get(name='task 2')

        self.assertEquals(obj1.name, 'task 1')
        self.assertEquals(obj2.name, 'task 2')

# Tests for serlializer



# Test serializer
class TodoSerializerTest(TestCase):
    def setUp(self) -> None:
        Todo.objects.create(name='task 1')
        Todo.objects.create(name='task 2')
        
    def test_todo_serializer(self):
        qs = Todo.objects.all()
        actual_serialized_data = TodoSerializer(qs, many=True)

        expected_serialized_data = [
            {"name":qs[0].name, "id":str(qs[0].id)},
            {"name":qs[1].name, "id":str(qs[1].id)}
        ]
        
        self.assertEqual(actual_serialized_data.data, expected_serialized_data)


# Test the view
class TodoViewTest(APITestCase):
    def setUp(self) -> None:
        Todo.objects.create(name='task 1')
        Todo.objects.create(name='task 2')

    def test_get_tasks(self):
        # Create two Tasks
        
        url = reverse('get-tasks')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 2)

    def test_create_todo(self):

        data = {"name":"task 3"}
        url = reverse('get-tasks')
        response = self.client.post(url, data)

        qs = Todo.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(qs.count(), 3)

    def test_patch_todo(self):

        data = {"name":"task 3"}
        url = reverse('put-tasks', kwargs={"id":"1"})
        response = self.client.patch(url, data)

        qs = Todo.objects.all()

        # Grab 1st object
        name = qs[0].name
        self.assertEqual(response.status_code, 200)
        self.assertEqual(qs.count(), 2)
        self.assertEqual(name, 'task 3')

    def test_put_todo(self):

        data = {"name":"task 3"}
        url = reverse('put-tasks', kwargs={"id":"1"})
        response = self.client.put(url, data)

        qs = Todo.objects.all()

        # Grab 1st object
        name = qs[0].name
        self.assertEqual(response.status_code, 200)
        self.assertEqual(qs.count(), 2)
        self.assertEqual(name, 'task 3')




