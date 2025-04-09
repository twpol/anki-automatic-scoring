$date = Get-Date -Format "yyyy-MM-dd"
$file = ".\Anki Automatic Scoring $date.zip"

Remove-Item -ErrorAction SilentlyContinue $file
& 7za.exe a -r -tzip '-x!.*' $file .
