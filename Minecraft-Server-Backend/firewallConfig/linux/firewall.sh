#!/bin/bash

# Obtener la ruta completa del directorio que contiene el script
script_directory="$(realpath "$(dirname "$0")")"

# Guardar configuración actual del firewall
iptables-save > "$script_directory/backup/firewall-default.backup"

# Definir las direcciones IP permitidas
allowedIPs=("192.168.1.1" "10.0.0.1")

# Definir el puerto SSH (por ejemplo, el puerto 64)
sshPort=64

# Limpiar reglas existentes
iptables -F

# Permitir conexiones SSH desde direcciones IP específicas
for allowedIP in "${allowedIPs[@]}"; do
    iptables -A INPUT -p tcp --dport $sshPort -s $allowedIP -j ACCEPT
done

# Bloquear todas las demás conexiones SSH al puerto específico
iptables -A INPUT -p tcp --dport $sshPort -j DROP

# Guardar configuración
iptables-save > "$script_directory/backup/firewall-with-rules.backup"

