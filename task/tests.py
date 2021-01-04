from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from task.models import Task


class TaskTests(APITestCase):
    def setUp(self):
        Task.objects.create(name="hello")

    def test_create_task(self):
        data = {'name': 'test task'}
        url = reverse('task_create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(name__iexact='test task').count(), 1)

    def test_start_task(self):
        task = Task.objects.get(name="hello")
        url = reverse('task_detail', kwargs={'pk': task.id})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(Task.objects.get(name="hello").start_date, None)

    def test_end_task(self):
        task = Task.objects.get(name="hello")
        data = {'success': True}
        url = reverse('task_detail', kwargs={'pk': task.id})
        response = self.client.patch(url, data, format='json')
        task = Task.objects.get(name="hello")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(task.success, True)
        self.assertNotEqual(task.end_date, None)
