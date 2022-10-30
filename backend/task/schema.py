import graphene
from task import queries, mutations


schema = graphene.Schema(query=queries.Query, mutation=mutations.Mutation)
