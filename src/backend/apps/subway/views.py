from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import SubwayLine
from exceptions import StatusUpdateError
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample


import logging

logger = logging.getLogger(__name__)


@extend_schema(
    description="Get subway line statuses",
    parameters=[
        OpenApiParameter(name="line", description="Comma-separated line names", type=str),
        OpenApiParameter(name="status", description="Filter by status (normal,delayed)", type=str),
    ],
    responses={200: list, 404: dict, 503: dict},
    examples=[
        OpenApiExample(
            "Success Response",
            value=[{"line": "1", "status": "normal"}, {"line": "2", "status": "delayed"}],
            response_only=True,
            status_codes=["200"],
        ),
        OpenApiExample(
            "Not Found Error",
            value={"error": "No matching subway lines found"},
            response_only=True,
            status_codes=["404"],
        ),
        OpenApiExample(
            "Service Unavailable Error",
            value={"error": "Failed to update statuses: Connection error"},
            response_only=True,
            status_codes=["503"],
        ),
    ],
)
@api_view(["GET"])
@permission_classes([AllowAny])
def get_status(request):
    """Fetch the status of subway lines with optional filters for line and status."""
    line_names = request.GET.get("line", "").split(",")
    line_statuses = request.GET.get("status", "").split(",")

    try:
        SubwayLine.update_statuses()

        # Apply filters
        lines = SubwayLine.objects.all()
        if line_names and line_names != [""]:
            name_filter = Q()
            for name in line_names:
                name_filter |= Q(name__iexact=name.strip())
            lines = lines.filter(name_filter)

        if line_statuses and line_statuses != [""]:
            status_filter = Q()
            for line_status in line_statuses:
                status_filter |= Q(status__iexact=line_status.strip())
            lines = lines.filter(status_filter)

        if not lines.exists():
            logger.error(f"No matching subway lines found for line={line_names} and status={line_statuses}")
            return Response({"error": "No matching subway lines found"}, status=status.HTTP_404_NOT_FOUND)

        lines = lines.order_by("name")
        response_data = [line.to_dict() for line in lines]
        return Response(response_data, status=status.HTTP_200_OK)

    except StatusUpdateError as e:
        logger.error(f"Failed to update statuses: {e}")
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        logger.error(f"Unexpected error during status fetch: {e}")
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    description="Get subway line uptime metrics",
    parameters=[OpenApiParameter(name="line", description="Comma-separated line names", type=str)],
    responses={200: list, 404: dict, 503: dict},
    examples=[
        OpenApiExample(
            "Success Response",
            value=[{"line": "1", "uptime": 0.855}, {"line": "2", "uptime": 0.588}],
            response_only=True,
            status_codes=["200"],
        ),
        OpenApiExample(
            "Not Found Error",
            value={"error": "No matching subway lines found"},
            response_only=True,
            status_codes=["404"],
        ),
        OpenApiExample(
            "Service Unavailable Error",
            value={"error": "Failed to update statuses: Connection error"},
            response_only=True,
            status_codes=["503"],
        ),
    ],
)
@api_view(["GET"])
@permission_classes([AllowAny])
def get_uptime(request):
    """Get uptime for all lines or filtered by line name."""
    line_names = request.GET.get("line", "").split(",")

    try:
        # Get lines and apply filter
        lines = SubwayLine.objects.all()
        if line_names and line_names != [""]:
            lines = lines.filter(name__iexact__in=[name.strip() for name in line_names])

        if not lines.exists():
            return Response({"error": "No matching subway lines found"}, status=status.HTTP_404_NOT_FOUND)

        lines = lines.order_by("name")
        return Response(
            [
                {
                    "line": line.name,
                    "uptime": round(line.uptime_ratio, 3) if line.uptime_ratio != -1.0 else None,
                }
                for line in lines
            ]
        )

    except StatusUpdateError as e:
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
