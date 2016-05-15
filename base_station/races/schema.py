import graphene
from graphene import relay, resolve_only_args
from graphene.contrib.django import DjangoNode, DjangoObjectType
from graphene.contrib.django.debug import DjangoDebugPlugin
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.core.types.custom_scalars import DateTime

from . import models
from base_station.pilots.schema import Pilot
from base_station.utils.interfaces import TimeStampedInterface, SyncModelInterface


class RaceGroup(SyncModelInterface, TimeStampedInterface, DjangoNode):

    class Meta:
        model = models.RaceGroup


class Race(SyncModelInterface, TimeStampedInterface, DjangoNode):

    groups = DjangoFilterConnectionField(RaceGroup, description='All Pilot Groups')

    class Meta:
        model = models.Race


class GroupPilot(SyncModelInterface, TimeStampedInterface, DjangoNode):

    pilot = relay.NodeField(Pilot)

    class Meta:
        model = models.GroupPilot


class HeatEvent(SyncModelInterface, TimeStampedInterface, DjangoNode):

    trigger = graphene.Int()
    trigger_label = graphene.String()
    trigger_verbose_label = graphene.String()

    class Meta:
        model = models.HeatEvent

        filter_fields = {
            'trigger': ('exact',)
        }

    def resolve_trigger_label(self, data, info):
        return models.HeatEvent.TRIGGERS(self.trigger).serializer_label

    def resolve_trigger_verbose_label(self, data, info):
        return models.HeatEvent.TRIGGERS(self.trigger).label


class RaceHeat(SyncModelInterface, TimeStampedInterface, DjangoNode):

    number = graphene.Int().NonNull
    goal_start_time = DateTime()
    goal_end_time = DateTime()
    started_time = DateTime()
    ended_time = DateTime()
    active = graphene.Boolean()
    started = graphene.Boolean()
    ended = graphene.Boolean()
    event_template = graphene.String()

    events = DjangoFilterConnectionField(HeatEvent, description='Heat Race Events')

    class Meta:
        model = models.RaceHeat

    # May not be needed?
    @classmethod
    def get_node(cls, _id, info):
        return RaceHeat(models.RaceHeat.objects.get(_id))


class RaceQuery(graphene.ObjectType):
    race = relay.NodeField(Race)
    all_races = DjangoFilterConnectionField(Race, description='All Races')

    heat = relay.NodeField(RaceHeat)
    all_heats = DjangoFilterConnectionField(RaceHeat, description='All Race Heats')

    event = relay.NodeField(HeatEvent)
    all_events = DjangoFilterConnectionField(HeatEvent, description='All Race Events')

    node = relay.NodeField()
    viewer = graphene.Field('self')

    num_heats = graphene.Int()

    def resolve_viewer(self, *args, **kwargs):
        # Currently we aren't filtering to only viewer specific data,
        # this is a stub to do that in the future.
        return self

    def resolve_num_heats(self, *args, **kwargs):
        return models.RaceHeat.objects.all().count()

    def resolve_num_heats(self, *args, **kwargs):
        return models.RaceHeat.objects.filter(ended_time__isnull=True).count()


schema = graphene.Schema(
    query=RaceQuery,
    name='Race details',
    # Currently causing issues
    # plugins=[DjangoDebugPlugin()]
)
