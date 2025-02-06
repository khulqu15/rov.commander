import socket
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_tcp_ip_list(request):
    ip_list = []
    host_name = socket.gethostname()
    for ip in socket.getaddrinfo(host_name, None):
        ip_list.append(ip[4][0])
    return Response({"tcpIpList": list(set(ip_list))})