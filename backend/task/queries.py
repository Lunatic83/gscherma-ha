import graphene
from task import models
from task import types
from graphql_jwt.decorators import login_required


import graphene
import graphql_jwt


# The Query class
class Query(graphene.ObjectType):
    all_tasks = graphene.List(types.TaskType)
    task_by_id = graphene.Field(types.TaskType, id=graphene.ID())

    current_user = graphene.Field(types.UserType, username=graphene.String())

    def resolve_current_user(self, info, username):
        return (
            models.User.objects.get(username__iexact=username)
        )
        
    @login_required
    def resolve_all_tasks(root, info):
        user = info.context.user
        user_obj = models.User.objects.get(username__iexact=user)
        return (
            models.Task.objects.filter(user_id=user_obj.id)
        )

    def resolve_task_by_id(root, info, id):
        return (
            models.Task.objects.get(pk=id)
        ) 