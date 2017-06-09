import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models import (
    Department as DepartmentModel,
    Employee as EmployeeModel,
    Pokemon as PokemonModel,
    Role as RoleModel,
)


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node,)


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node,)


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node,)


class Pokemon(SQLAlchemyObjectType):
    class Meta:
        model = PokemonModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee)
    all_roles = SQLAlchemyConnectionField(Role)
    all_departments = SQLAlchemyConnectionField(Department)
    all_pokemon = SQLAlchemyConnectionField(Pokemon)
    role = graphene.Field(Role)

schema = graphene.Schema(query=Query, types=[Department, Employee, Role])
