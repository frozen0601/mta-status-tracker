from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import SubwayLine
from .mta_data_fetcher import StatusUpdateError
from subway.tasks import update_subway_statuses


@api_view(["GET"])
@permission_classes([AllowAny])
def get_status(request):
    update_subway_statuses()
    line_name = request.GET.get("line")
    try:
        latest_line_info = SubwayLine.update_statuses(line_name)
        if line_name:
            if line_name not in latest_line_info:
                return Response({"error": "Line not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(latest_line_info[line_name].to_dict())
        return Response([line.to_dict() for line in latest_line_info.values()])
    except StatusUpdateError as e:
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(["GET"])
def get_uptime(request):
    line_name = request.GET.get("line")
    if not line_name:
        return Response({"error": "line parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        line = SubwayLine.objects.get(name=line_name)
        uptime = line.get_uptime()
        return Response({"line": line_name, "uptime": uptime})
    except SubwayLine.DoesNotExist:
        return Response({"error": "Line not found"}, status=status.HTTP_404_NOT_FOUND)
