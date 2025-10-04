# Script para probar el workflow localmente
Write-Host "Probando workflow de GitHub Actions localmente..." -ForegroundColor Green

# Simular el paso de generacion
Write-Host "Generando noticias diarias..." -ForegroundColor Yellow
python "isotools-summaries-standalone/generate-daily-3-news.py"

if (Test-Path "isotools-daily-news.json") {
    Write-Host "Archivo generado exitosamente" -ForegroundColor Green
    
    # Mostrar tamaño del archivo
    $fileSize = (Get-Item "isotools-daily-news.json").Length
    Write-Host "Tamaño del archivo: $fileSize bytes" -ForegroundColor Cyan
    
    # Mostrar preview del contenido
    Write-Host "Preview del JSON generado:" -ForegroundColor Yellow
    $content = Get-Content "isotools-daily-news.json" | ConvertFrom-Json
    Write-Host "Titulo: $($content.metadata.title)" -ForegroundColor White
    Write-Host "Fecha generada: $($content.metadata.generated_date)" -ForegroundColor White
    Write-Host "Total articulos: $($content.daily_news.Count)" -ForegroundColor White
    
    Write-Host "Articulos seleccionados:" -ForegroundColor Yellow
    foreach ($article in $content.daily_news) {
        $title = $article.title.Substring(0, [Math]::Min(60, $article.title.Length))
        Write-Host "$($article.news_priority). $title..." -ForegroundColor White
    }
    
    Write-Host "URL RAW seria:" -ForegroundColor Cyan
    Write-Host "https://raw.githubusercontent.com/thenext90/manu2/isotools-news-only/isotools-daily-news.json" -ForegroundColor Blue
    
} else {
    Write-Host "Error: No se pudo generar el archivo" -ForegroundColor Red
    exit 1
}

Write-Host "Prueba del workflow completada!" -ForegroundColor Green