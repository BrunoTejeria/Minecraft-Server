# Guarda la configuración
Get-NetFirewallRule | Export-Clixml -Path "$PSScriptRoot\firewall-default.xml"


# Define las direcciones IP permitidas (ajusta según sea necesario)
$allowedIPs = @("192.168.1.1", "10.0.0.1")

# Define el puerto SSH (por ejemplo, el puerto 64)
$sshPort = 64

# Configura el firewall de Windows para permitir conexiones solo desde direcciones IP específicas en el puerto SSH
foreach ($allowedIP in $allowedIPs) {
    New-NetFirewallRule -DisplayName "AllowSSHFrom$allowedIP" -Direction Inbound -Protocol TCP -LocalPort $sshPort -Action Allow -RemoteAddress $allowedIP
}

# Bloquea todas las demás conexiones SSH al puerto específico
New-NetFirewallRule -DisplayName "DenyAllSSH" -Direction Inbound -Protocol TCP -LocalPort $sshPort -Action Block
