from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.utils import timezone
from .models import SubwayLine
from exceptions import StatusUpdateError

import logging

logger = logging.getLogger(__name__)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_status(request):
    """Fetch the status of subway lines with optional filters for line and status."""
    line_name = request.GET.get("line")
    status_filter = request.GET.get("status")

    try:
        latest_lines = SubwayLine.update_statuses()

        # Apply filters
        lines = SubwayLine.objects.filter(name__in=latest_lines.keys())
        if line_name:
            lines = lines.filter(name=line_name)
        if status_filter:
            lines = lines.filter(status=status_filter)

        if not lines.exists():
            raise ValidationError("No matching subway lines found.")

        # Convert lines to dictionary format
        response_data = [line.to_dict() for line in lines]
        return Response(response_data, status=status.HTTP_200_OK)

    except StatusUpdateError as e:
        logger.error(f"Failed to update statuses: {e}")
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        logger.error(f"Unexpected error during status fetch: {e}")
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_uptime(request):
    """Get uptime for all lines or filtered by line name."""
    line_name = request.GET.get("line")

    try:
        # Update all statuses first
        latest_lines = SubwayLine.update_statuses()

        # Get lines and apply filter
        lines = SubwayLine.objects.filter(name__in=latest_lines.keys())
        if line_name:
            lines = lines.filter(name=line_name)

        if not lines.exists():
            return Response({"error": "No matching subway lines found"}, status=status.HTTP_404_NOT_FOUND)
        sorted(lines, key=lambda line: line.name)
        return Response(
            [
                {
                    "line": line.name,
                    "uptime": line.get_uptime(),
                }
                for line in lines
            ]
        )

    except StatusUpdateError as e:
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
