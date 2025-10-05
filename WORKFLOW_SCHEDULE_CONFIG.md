# ⏰ Configuración del Horario de Workflow Actualizada

## 📅 **Nuevo Horario Configurado**

### 🕰️ **Horario de Ejecución:**
- **Días**: Lunes a Viernes (días laborables únicamente)
- **Hora**: 7:00 AM UTC
- **Cron**: `0 7 * * 1-5`

### 🌍 **Equivalencias de Horario:**

| Zona Horaria | Hora Local |
|--------------|------------|
| UTC | 7:00 AM |
| España (CET/CEST) | 8:00 AM / 9:00 AM |
| México (CST) | 1:00 AM |
| Argentina (ART) | 4:00 AM |
| Colombia (COT) | 2:00 AM |

### 📊 **Beneficios del Nuevo Horario:**

1. **✅ Solo días laborables**: No se ejecuta fines de semana
2. **✅ Horario matutino**: Contenido fresco para el día laboral
3. **✅ Consistencia**: Mismo horario todos los días hábiles
4. **✅ Menor carga**: Reduce ejecuciones innecesarias en weekend

### 🔧 **Configuración Técnica:**

```yaml
on:
  schedule:
    - cron: '0 7 * * 1-5'  # Lunes a Viernes a las 7:00 AM UTC
```

**Significado del cron:**
- `0` = Minuto 0
- `7` = Hora 7 (UTC)
- `*` = Cualquier día del mes
- `*` = Cualquier mes
- `1-5` = Días de la semana (1=Lunes, 5=Viernes)

### 📈 **Próximas Ejecuciones:**

El workflow se ejecutará automáticamente:
- **Lunes**: 7:00 AM UTC
- **Martes**: 7:00 AM UTC  
- **Miércoles**: 7:00 AM UTC
- **Jueves**: 7:00 AM UTC
- **Viernes**: 7:00 AM UTC

**No se ejecutará:** Sábados y Domingos

### 🌐 **URL de Resultados:**
```
https://raw.githubusercontent.com/thenext90/manu2/isotools-news-only/isotools-daily-news.json
```

### 🎯 **Características Mantenidas:**
- ✅ Solo resúmenes únicos de IA
- ✅ 3 artículos por actualización
- ✅ Filtrado de resúmenes genéricos
- ✅ Ejecución exclusiva en rama `isotools-news-only`
- ✅ Ejecución manual disponible cuando sea necesario

---

**✅ Configuración Aplicada**: Lunes a Viernes a las 7:00 AM UTC  
**📅 Fecha de Configuración**: 2025-10-04  
**🔐 Estado**: Activo y Funcional