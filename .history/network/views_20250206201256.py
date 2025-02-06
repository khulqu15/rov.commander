import socket
import serial.tools.list_ports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse

@api_view(['GET'])
def get_network_interfaces():
    interfaces = set()
    host_name = socket.gethostname()
    for ip in socket.getaddrinfo(host_name, None):
        interfaces.add(ip[4][0])
    return list(interfaces)

def get_network_info(request):
    interfaces = get_network_interfaces()
    selected_interface = request.GET.get("interface", None)
    ip_list = []
    com_ports = []

    if selected_interface:
        ip_list = [ip for ip in interfaces if ip == selected_interface]
        ports = list(serial.tools.list_ports.comports())
        com_ports = [{"device": port.device, "description": port.description} for port in ports]

    return render(request, "network_info.html", {
        "interfaces": interfaces,
        "selected_interface": selected_interface,
        "tcpIp": ip_list,
        "comPorts": com_ports
    })
    return render(request, "network_info.html", {
        "interfaces": interfaces,
        "selected_interface": selected_interface,
        "tcpIp": ip_list,
        "comPorts": com_ports
    })
