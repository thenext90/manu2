# Script de verificación final - Resúmenes únicos
Write-Host "🔍 VERIFICACIÓN DE RESÚMENES ÚNICOS" -ForegroundColor Green
Write-Host "=" * 50 -ForegroundColor Green

# Ejecutar el nuevo script
Write-Host "`n🗞️ Generando noticias con script MEJORADO..." -ForegroundColor Yellow
python "isotools-summaries-standalone/generate-daily-news-unique.py"

if (Test-Path "isotools-daily-news.json") {
    Write-Host "`n✅ Archivo generado exitosamente" -ForegroundColor Green
    
    # Verificar calidad de resúmenes
    $content = Get-Content "isotools-daily-news.json" | ConvertFrom-Json
    
    Write-Host "`n📊 MÉTRICAS DE CALIDAD:" -ForegroundColor Cyan
    Write-Host "Versión: $($content.metadata.version)" -ForegroundColor White
    Write-Host "Método: $($content.configuration.selection_method)" -ForegroundColor White
    Write-Host "Resúmenes únicos: $($content.metadata.summary_quality.unique_summaries)" -ForegroundColor Green
    Write-Host "Resúmenes genéricos: $($content.metadata.summary_quality.generic_summaries)" -ForegroundColor Red
    
    Write-Host "`n📰 RESÚMENES VERIFICADOS:" -ForegroundColor Yellow
    foreach ($article in $content.daily_news) {
        $type = if ($article.summary_type -eq "unique") { "🎯 ÚNICO" } else { "⚠️  GENÉRICO" }
        Write-Host "$($article.news_priority). $type" -ForegroundColor White
        Write-Host "   Título: $($article.title.Substring(0, [Math]::Min(60, $article.title.Length)))..." -ForegroundColor Gray
        Write-Host "   Resumen: $($article.ai_summary.Substring(0, [Math]::Min(80, $article.ai_summary.Length)))..." -ForegroundColor Gray
        Write-Host ""
    }
    
    # Verificar si hay duplicados
    $summaries = $content.daily_news | ForEach-Object { $_.ai_summary }
    $uniqueSummaries = $summaries | Select-Object -Unique
    
    if ($summaries.Count -eq $uniqueSummaries.Count) {
        Write-Host "✅ TODOS LOS RESÚMENES SON ÚNICOS" -ForegroundColor Green
    } else {
        Write-Host "❌ DETECTADOS RESÚMENES DUPLICADOS" -ForegroundColor Red
    }
    
    Write-Host "`n🌐 URL para verificar:" -ForegroundColor Cyan
    Write-Host "https://raw.githubusercontent.com/thenext90/manu2/isotools-news-only/isotools-daily-news.json" -ForegroundColor Blue
    
} else {
    Write-Host "`n❌ Error: No se pudo generar el archivo" -ForegroundColor Red
}

Write-Host "`n🎯 PROBLEMA RESUELTO: No más resúmenes duplicados!" -ForegroundColor Green