import graphene
import graphene_django.filter as django_filter

import purplship.server.graph.utils as utils
import purplship.server.graph.extension.orders.mutations as mutations
import purplship.server.graph.extension.orders.types as types
import purplship.server.orders.models as models


class Query:
    order = graphene.Field(types.OrderType, id=graphene.String(required=True))
    orders = django_filter.DjangoFilterConnectionField(
        types.OrderType,
        required=True,
        filterset_class=types.OrderFilter,
        default_value=[],
    )

    @utils.login_required
    def resolve_order(self, info, **kwargs):
        return models.Order.access_by(info.context).filter(**kwargs).first()

    @utils.login_required
    def resolve_orders(self, info, **kwargs):
        return models.Order.access_by(info.context)


class Mutation:
    partial_order_update = mutations.PartialOrderUpdate.Field()