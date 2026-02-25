param([string]$Service = "ssh")
# demo: create a small archive (Windows/PowerShell Core cross-platform)
$now = Get-Date -Format "yyyyMMddHHmmss"
$dest = "logs_$Service_$now.zip"
Write-Output "Creating $dest (demo)"
# This is a demo — don't include real /var/log in public repos
New-Item -Path $dest -ItemType File -Force | Out-Null
Write-Output "Done (demo)"
