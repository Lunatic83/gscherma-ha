import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from task import models, types


# Mutation sends data to the database

# Customize the ObtainJSONWebToken behavior to include the user info
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class CreateUser(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = models.User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class CreateTask(graphene.Mutation):
    task = graphene.Field(types.TaskType)

    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        is_completed = graphene.Boolean(required=True)
    
    @login_required
    def mutate(self, info, title='', content='', is_completed=False):
        user = info.context.user
        user_obj = models.User.objects.get(username__iexact=user)

        task = models.Task(
            title=title,
            content=content,
            is_completed= is_completed,
            user_id=user_obj.id,
        )
        task.save()

        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    task = graphene.Field(types.TaskType)

    class Arguments:
        task_id = graphene.ID(required=True)
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        is_completed = graphene.Boolean(required=True)

    @login_required
    def mutate(self, info, task_id, title='', content='', is_completed=False):
        user = info.context.user
        user_obj = models.User.objects.get(username__iexact=user)
        task = models.Task.objects.get(pk=task_id)
        
        if task.user_id == user_obj.id:
            task.title = title
            task.content = content
            task.is_completed = is_completed
            task.save()
        else:
            raise Exception('Task not for this user')
        
        return UpdateTask(task=task)


class UpdateTaskComplete(graphene.Mutation):
    task = graphene.Field(types.TaskType)

    class Arguments:
        task_id = graphene.ID(required=True)
        is_completed = graphene.Boolean(required=True)

    @login_required
    def mutate(self, info, task_id, is_completed):
        user = info.context.user
        user_obj = models.User.objects.get(username__iexact=user)
        task = models.Task.objects.get(pk=task_id)

        if task.user_id == user_obj.id:
            task.is_completed = is_completed
            task.save()
        else:
            raise Exception('Task not for this user')

        return UpdateTaskComplete(task=task)


class Mutation(graphene.ObjectType):
    # Tokens
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_user = CreateUser.Field()
    create_task = CreateTask.Field()

    update_task = UpdateTask.Field()
    update_task_complete = UpdateTaskComplete.Field()
