import socket
import serial.tools.list_ports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse

@api_view(['GET'])
def get_tcp_ip_list(request):
    ip_list = []
    host_name = socket.gethostname()
    for ip in socket.getaddrinfo(host_name, None):
        ip_list.append(ip[4][0])
    return Response({"tcpIp": list(set(ip_list))})

def get_com_ports(request):
    ports = list(serial.tools.list_ports())
    com_ports = [{"device": port.device, "description": port.description} for port in ports]
    return Response({"comPorts": com_ports})

def get_network_info(request):
    ip_list = []
    host_name = socket.gethostname()
    for ip in socket.getaddrinfo(host_name, None):
        ip_list.append(ip[4][0])
    ports = list(serial.tools.list_ports.comports())
    com_ports = [{"device": port.device, "description": port.description} for port in ports]
    return render(request, "network_info.html", {
        "interfaces": interfaces,
        "selected_interface": selected_interface,
        "tcpIp": ip_list,
        "comPorts": com_ports
    })
