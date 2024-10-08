# from rest_framework import viewsets
#
# class PersonView(viewsets.GenericViewSet):
#     @extend_schema(
#         parameters=[
#           QuerySerializer,  # serializer fields are converted to parameters
#           OpenApiParameter("nested", QuerySerializer),  # serializer object is converted to a parameter
#           OpenApiParameter("queryparam1", OpenApiTypes.UUID, OpenApiParameter.QUERY),
#           OpenApiParameter("pk", OpenApiTypes.UUID, OpenApiParameter.PATH), # path variable was overridden
#         ],
#         request=YourRequestSerializer,
#         responses=YourResponseSerializer,
#         # more customizations
#     )
#     def retrieve(self, request, pk, *args, **kwargs):
#         pass