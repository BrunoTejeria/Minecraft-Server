# Guarda la configuración
Get-NetFirewallRule | Export-Clixml -Path "$PSScriptRoot\firewall\firewall-with-rules.xml"


# Define el nombre de las reglas que deseas eliminar
$ruleNamesToDelete = @("AllowSSHFrom192.168.1.1", "AllowSSHFrom10.0.0.1", "DenyAllSSH")

# Elimina las reglas especificadas
foreach ($ruleName in $ruleNamesToDelete) {
    Remove-NetFirewallRule -DisplayName $ruleName
}

