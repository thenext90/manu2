#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script MEJORADO para generar JSON diario de 3 artículos aleatorios
SOLO selecciona artículos con resúmenes únicos de IA
Evita resúmenes genéricos duplicados
"""

import json
import random
import os
from datetime import datetime, timedelta
from collections import Counter

def generate_daily_news():
    print("🗞️ GENERADOR DE NOTICIAS DIARIAS ISO (3 artículos ÚNICOS)")
    print("=" * 55)
    
    # Leer archivo principal
    try:
        with open('isotools-final-data.json', 'r', encoding='utf-8') as f:
            main_data = json.load(f)
        print(f"✅ Cargados {len(main_data['data'])} artículos")
    except FileNotFoundError:
        print("❌ No se encontró isotools-final-data.json")
        return
    
    all_articles = main_data['data']
    
    # Identificar el resumen genérico más común
    summaries = [article.get('ai_summary', '') for article in all_articles]
    summary_counts = Counter(summaries)
    most_common_summary = summary_counts.most_common(1)[0]
    generic_summary = most_common_summary[0]
    generic_count = most_common_summary[1]
    
    print(f"🔍 Detectado resumen genérico usado en {generic_count} artículos")
    print(f"📝 Resumen genérico: '{generic_summary[:80]}...'")
    
    # Filtrar artículos con resúmenes únicos
    unique_articles = []
    generic_articles = []
    
    for article in all_articles:
        if article.get('ai_summary', '') == generic_summary:
            generic_articles.append(article)
        else:
            unique_articles.append(article)
    
    print(f"✅ Encontrados {len(unique_articles)} artículos con resúmenes únicos")
    print(f"⚠️  Encontrados {len(generic_articles)} artículos con resúmenes genéricos")
    
    # Seleccionar 3 artículos priorizando únicos
    selected_articles = []
    
    if len(unique_articles) >= 3:
        # Suficientes artículos únicos
        selected_articles = random.sample(unique_articles, 3)
        print("🎯 Seleccionados 3 artículos con resúmenes únicos")
    elif len(unique_articles) > 0:
        # Algunos únicos, completar con genéricos pero diferentes títulos
        selected_articles = unique_articles.copy()
        remaining_needed = 3 - len(unique_articles)
        
        # Seleccionar los mejores genéricos (diferentes categorías si es posible)
        available_generic = random.sample(generic_articles, min(remaining_needed, len(generic_articles)))
        selected_articles.extend(available_generic)
        
        print(f"🔄 Seleccionados {len(unique_articles)} únicos + {len(available_generic)} genéricos")
    else:
        # Solo genéricos disponibles - seleccionar los mejores
        selected_articles = random.sample(generic_articles, 3)
        print("⚠️  Solo artículos genéricos disponibles")
    
    # Mezclar para orden aleatorio
    random.shuffle(selected_articles)
    
    # Agregar información de rotación
    for i, article in enumerate(selected_articles):
        article['news_priority'] = i + 1
        article['selected_date'] = datetime.now().isoformat()
        article['rotation_id'] = f"{datetime.now().strftime('%Y-%m-%d')}-{i+1}"
        
        # Marcar si es resumen único o genérico
        article['summary_type'] = 'unique' if article.get('ai_summary', '') != generic_summary else 'generic'
    
    # Crear JSON de noticias diarias
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    
    # Contar tipos de resumen seleccionados
    unique_selected = sum(1 for art in selected_articles if art.get('summary_type') == 'unique')
    generic_selected = sum(1 for art in selected_articles if art.get('summary_type') == 'generic')
    
    daily_news = {
        "metadata": {
            "title": "ISOTools - Noticias Diarias",
            "description": "Selección diaria de 3 artículos destacados sobre normas ISO",
            "source": "ISOTools Corporate Blog (isotools.us)",
            "generated_date": today.strftime("%Y-%m-%d"),
            "generated_at": today.isoformat(),
            "next_update": tomorrow.strftime("%Y-%m-%d"),
            "total_articles": 3,
            "rotation_type": "daily_random_selection_unique_summaries",
            "version": "2.0.0",
            "purpose": "Noticias diarias para sección web",
            "github_raw_example": "https://raw.githubusercontent.com/thenext90/manu2/isotools-news-only/isotools-daily-news.json",
            "parent_source": main_data['metadata']['source'],
            "language": "español",
            "summary_quality": {
                "unique_summaries": unique_selected,
                "generic_summaries": generic_selected,
                "total_available_unique": len(unique_articles)
            }
        },
        "configuration": {
            "daily_rotation": True,
            "articles_per_day": 3,
            "selection_method": "prioritize_unique_summaries",
            "auto_update": True,
            "github_action_enabled": True,
            "cache_duration_hours": 24,
            "rotation_on_each_execution": True,
            "quality_filter_enabled": True,
            "avoid_generic_summaries": True
        },
        "daily_news": selected_articles,
        "generation_info": {
            "selected_at": today.isoformat(),
            "next_rotation": tomorrow.isoformat(),
            "algorithm": "python_unique_summary_priority",
            "total_available_articles": len(all_articles),
            "unique_summaries_available": len(unique_articles),
            "generic_summaries_count": len(generic_articles),
            "rotation_guaranteed": True,
            "quality_metrics": {
                "unique_ratio": f"{unique_selected}/3",
                "generic_ratio": f"{generic_selected}/3"
            }
        }
    }
    
    # Guardar archivo en directorio actual
    with open('isotools-daily-news.json', 'w', encoding='utf-8') as f:
        json.dump(daily_news, f, indent=2, ensure_ascii=False)
    
    # También guardar en el directorio raíz del proyecto para GitHub Actions
    root_path = os.path.join('..', 'isotools-daily-news.json')
    with open(root_path, 'w', encoding='utf-8') as f:
        json.dump(daily_news, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generado isotools-daily-news.json con 3 artículos")
    print(f"✅ Copiado a directorio raíz para GitHub Actions")
    print(f"\n📊 Calidad de resúmenes:")
    print(f"   🎯 Únicos: {unique_selected}/3")
    print(f"   ⚠️  Genéricos: {generic_selected}/3")
    print("\n📋 Artículos seleccionados:")
    for i, article in enumerate(selected_articles, 1):
        summary_emoji = "🎯" if article.get('summary_type') == 'unique' else "⚠️ "
        print(f"{i}. {summary_emoji} {article['title'][:60]}...")
        print(f"   Categoría: {article['category']}")
        print(f"   Resumen: {article.get('ai_summary', '')[:80]}...")
    
    print(f"\n🚀 Archivo listo para consumo en GitHub!")
    print(f"🌐 URL: https://raw.githubusercontent.com/thenext90/manu2/isotools-news-only/isotools-daily-news.json")

if __name__ == "__main__":
    generate_daily_news()