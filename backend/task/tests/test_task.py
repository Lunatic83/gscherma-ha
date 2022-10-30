
import json
# from task.schema import schema
from task import models
from unittest import skip

from graphene_django.utils.testing import GraphQLTestCase

class TaskManagerTestCase(GraphQLTestCase):
    GRAPHQL_URL = "http://localhost:8000/graphql"

    def setUp(self):
        super().setUp()
        user = models.User(
            username='test_user',
            email='g@g.com',
        )
        user.set_password('password')
        user.save()

        response = self.query(
            '''
            mutation tokenAuth($username: String!, $password: String!) {
                tokenAuth(username: $username, password: $password) {
                token
                user {
                        id
                        username
                    }
                }
            }
            ''',
            op_name='tokenAuth',
            variables={'username': 'test_user', 'password': 'password'}
        )

        content = json.loads(response.content)
        self.token = content["data"]["tokenAuth"]['token']

    
# 1. create a task
    def test_create_task(self):
        response = self.query(
            '''
            mutation createTask($title: String!, $content: String!, $isCompleted: Boolean!) {
                createTask(title: $title, content: $content, isCompleted: $isCompleted) {
                    task {
                        id
                    }
                }
            }
                
            ''',
            op_name='createTask',
            headers={'HTTP_AUTHORIZATION': 'JWT '+self.token},
            variables= {'title': "Title Task", 'content': 'content task', 'isCompleted': True}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertIsNotNone(content["data"]["createTask"]['task']["id"])

    def test_create_task_failing_missing_title(self):
        response = self.query(
            '''
            mutation createTask( $content: String!, $isCompleted: Boolean!) {
                createTask( content: $content, isCompleted: $isCompleted) {
                    task {
                        id
                    }
                }
            }
                
            ''',
            op_name='createTask',
            headers={'HTTP_AUTHORIZATION': 'JWT '+self.token},
            variables= {'content': 'content task', 'isCompleted': True}
        )
        content = json.loads(response.content)
        self.assertResponseHasErrors(response)
        self.assertIsNotNone(content["errors"][0]["message"])


# 2. fetch a create task
    def test_fetch_created_task(self):
        title = "Title Task"
        content = "content task"
        is_completed = False

        response_create = self.query(
            '''
            mutation createTask($title: String!, $content: String!, $isCompleted: Boolean!) {
                createTask(title: $title, content: $content, isCompleted: $isCompleted) {
                    task {
                        id
                    }
                }
            }
                
            ''',
            op_name='createTask',
            headers={'HTTP_AUTHORIZATION': 'JWT '+self.token},
            variables= {'title': title, 'content': content, 'isCompleted': is_completed}
        )
        content_create = json.loads(response_create.content)
        task_id = content_create["data"]["createTask"]['task']["id"]

        response_query = self.query(
            '''
                query taskById($id: ID!) {
                    taskById(id: $id) {
                        id
                        title
                        content
                        isCompleted
                    }
                }

            ''',
            op_name='taskById',
            headers={'HTTP_AUTHORIZATION': 'JWT '+self.token},
            variables= {'id': task_id}
        )

        content_query = json.loads(response_query.content)
        self.assertResponseNoErrors(response_query)
        self.assertIsNotNone(content_query["data"]["taskById"]["id"])
        self.assertEqual(content_query["data"]["taskById"]["title"], title)
        self.assertEqual(content_query["data"]["taskById"]["content"], content)

    def test_fetch_failing_created_task(self):
        response_query = self.query(
            '''
            query taskById($id: ID!) {
                taskById(id: $id) {
                    id
                    title
                    content
                    isCompleted
                }
            }

            ''',
            op_name='taskById',
            headers={'HTTP_AUTHORIZATION': 'JWT '+self.token},
            variables= {'id': '1000'}
        )

        content_query = json.loads(response_query.content)
        self.assertResponseHasErrors(response_query)
        self.assertIsNotNone(content_query["errors"][0]["message"])



# 3. fetch a list of task from a user
    def test_fetch_all_tasks(self):
        response = self.query(
            '''
            mutation createTask($title: String!, $content: String!, $isCompleted: Boolean!) {
                createTask(title: $title, content: $content, isCompleted: $isCompleted) {
                    task {
                        id
                    }
                }
            }
                
            ''',
            op_name='createTask',
            headers={'HTTP_AUTHORIZATION': 'JWT '+self.token},
            variables= {'title': "Title Task", 'content': 'content task', 'isCompleted': True}
        )

        response = self.query(
            '''
            query allTasks{
                allTasks {
                    id
                    title
                    isCompleted
                }
            }
            ''',
            op_name='allTasks',
            headers={'HTTP_AUTHORIZATION': 'JWT '+self.token},            
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(len(content["data"]['allTasks']), 1)
