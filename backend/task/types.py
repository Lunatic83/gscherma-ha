import graphene
from graphene_django import DjangoObjectType
from task import models



class UserType(DjangoObjectType):
    class Meta:
        model = models.User


class TaskType(DjangoObjectType):
    class Meta:
        model = models.Task


