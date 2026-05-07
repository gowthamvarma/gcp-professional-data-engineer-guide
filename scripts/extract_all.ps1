# Batch process all PDFs in the sample-questions folder
$inputDir = "docs/sample-questions/pdf"
$outputDir = "docs/sample-questions/extracted_text"

if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir
}

Write-Host "Starting batch extraction..." -ForegroundColor Cyan
python scripts/extract_pdf_text.py $inputDir -o $outputDir
Write-Host "Extraction complete. Files saved to $outputDir" -ForegroundColor Green
