$url = "http://127.0.0.1:64163/compute"
$concurrent = 20
$duration = 120

$startTime = Get-Date
$jobs = @()

while ((Get-Date).Subtract($startTime).TotalSeconds -lt $duration) {
    while ($jobs.Count -lt $concurrent) {
        $jobs += Start-Job -ScriptBlock {
            param($url)
            Invoke-WebRequest -Uri $url
        } -ArgumentList $url
    }
    
    $jobs = $jobs | Where-Object { $_.State -eq 'Running' }
    Start-Sleep -Milliseconds 100
}

$jobs | Remove-Job -Force
Write-Host "Test completed"