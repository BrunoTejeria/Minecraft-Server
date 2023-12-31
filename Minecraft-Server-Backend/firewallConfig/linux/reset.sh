#!/bin/bash

# Obtener la ruta completa del directorio que contiene el script
script_directory="$(realpath "$(dirname "$0")")"

# Guardar configuración actual del firewall
iptables-save > "$script_directory/backup/firewall-with-rules.backup"

# Restaurar configuración del firewall desde el archivo XML
iptables-restore < "$script_directory/backup/firewall-default.backup"