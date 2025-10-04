# ISOTools Daily News System

Sistema automatizado para la generación diaria de noticias ISO para uso en sitios web.

## 🚀 Características

- **Generación automática diaria**: GitHub Actions ejecuta el script cada día a las 12:00 UTC
- **Selección inteligente**: 3 artículos diferentes cada día usando algoritmo basado en fecha
- **Multiple formatos**: Soporte para JSON con metadatos completos
- **API RESTful**: Acceso directo via GitHub RAW URLs

## 📡 URL de Consumo

```
https://raw.githubusercontent.com/thenext90/manu2/isotools-news-only/isotools-daily-news.json
```

## 🗂️ Estructura del Proyecto

```
├── isotools-daily-news.json          # Archivo principal (se actualiza diariamente)
├── isotools-summaries-standalone/    # Sistema completo
│   ├── generate-daily-3-news.py     # Script principal de generación
│   ├── isotools-final-data.json     # Base de datos de artículos
│   └── isotools-daily-news.json     # Copia local
├── data/
│   └── isotools-scraping.json       # Datos de scraping
└── .github/workflows/
    └── daily-news-update.yml        # Automatización GitHub Actions
```

## 🔧 Ejecución Manual

Para generar noticias manualmente:

```bash
# Usando Python (recomendado)
python isotools-summaries-standalone/generate-daily-3-news.py

# Usando PowerShell (prueba local)
.\test-workflow.ps1
```

## 📊 Formato del JSON

```json
{
  "metadata": {
    "title": "ISOTools - Noticias Diarias",
    "generated_date": "2025-10-04",
    "total_articles": 3,
    "source": "ISOTools Corporate Blog"
  },
  "daily_news": [
    {
      "news_priority": 1,
      "id": "art_123",
      "title": "Título del artículo",
      "summary": "Resumen del artículo...",
      "category": "ISO_Category",
      "url": "https://isotools.us/article-url",
      "featured_image": "image_url"
    }
  ]
}
```

## ⚙️ Configuración del Workflow

El sistema se ejecuta automáticamente:
- **Horario**: Todos los días a las 12:00 UTC
- **Trigger manual**: Disponible en GitHub Actions
- **Rama**: `isotools-news-only`

## 🔄 Estado del Sistema

- ✅ **Python Script**: Funcional
- ✅ **GitHub Actions**: Configurado y funcional  
- ✅ **Auto-commit**: Configurado
- ✅ **RAW URL**: Disponible públicamente

## 📝 Logs y Debugging

Para revisar ejecuciones:
1. Ve a GitHub Actions en el repositorio
2. Busca el workflow "Daily News Update"
3. Revisa los logs de la última ejecución

## 🛠️ Mantenimiento

El sistema es completamente autónomo. Los artículos se seleccionan automáticamente de la base de datos `isotools-final-data.json` usando un algoritmo que garantiza rotación diaria.

---

**Última actualización**: Octubre 4, 2025  
**Versión**: 1.0.0  
**Estado**: ✅ Operacional