import graphene
from graphene_django import DjangoObjectType
from .models import Record

class RecordType(DjangoObjectType):
    class Meta:
        model = Record
        fields = ('id', 'name', 'date')

class Query(graphene.ObjectType):
    records = graphene.List(RecordType, id=graphene.Int())
    
    def resolve_records(self, info, id=None):
        if id:
            return Record.objects.filter(id=id)

        return Record.objects.all()
    
class CreateRecord(graphene.Mutation):
    record = graphene.Field(RecordType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        record = Record(name=name)
        record.save()
        return CreateRecord(record=record)

class UpdateRecord(graphene.Mutation):
    record = graphene.Field(RecordType)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()

    def mutate(self, info, id, name):
        record = Record.objects.get(id = id)
        if record:
            if name:
                record.name = name
                record.save()
                return UpdateRecord(record = record)
            
class DeleteRecord(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        record = Record.objects.get(id = id)
        record.delete()
        return DeleteRecord(message = f"ID {id} deleted")

class Mutation(graphene.ObjectType):
    create_record = CreateRecord.Field()
    update_record = UpdateRecord.Field()
    delete_record = DeleteRecord.Field()