import json
from task import models
from graphene_django.utils.testing import GraphQLTestCase

class TaskManagerTestCase(GraphQLTestCase):
    GRAPHQL_URL = "http://localhost:8000/graphql"

    def setUp(self):
        super().setUp()
        user = models.User(
            username='test_user2',
            email='g@g.com',
        )
        user.set_password('password')
        user.save()

    def test_create_user(self):
        response = self.query(
            '''
            mutation createUser($username: String!, $email: String!, $password: String!) {
                createUser(username: $username, email: $email, password: $password) {
                    user {
                        id
                        username
                        email
                    }
                }
            }
            ''',
            op_name='createUser',
            variables= {'username': "test_user", 'password': 'password', 'email': 'g@g.com'}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(content["data"]["createUser"]['user']["username"],"test_user")
        self.assertIsNotNone(content["data"]["createUser"]['user']["id"])

    def test_token_auth_mutation(self):
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
            variables={'username': 'test_user2', 'password': 'password'}
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertIsNotNone(content["data"]["tokenAuth"]['token'])

    def test_token_auth_mutation_failing(self):
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
            variables={'username': 'test_user4', 'password': 'password'}
        )

        content = json.loads(response.content)
        self.assertResponseHasErrors(response)
        self.assertEqual(content["errors"][0]["message"],"Please enter valid credentials")
        self.assertEqual(content["data"]["tokenAuth"], None)





