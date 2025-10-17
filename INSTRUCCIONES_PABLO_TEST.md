# Instrucciones para configurar el Test de Pablo 17/10/25

## ✅ Cambios Realizados

Se ha creado un nuevo test especial llamado "Test de Pablo 17/10/25" con las siguientes características:

### 🎯 Características del Test

- **15 preguntas** tipo test seleccionadas aleatoriamente de OPE de Farmacia Hospitalaria
- **Temporizador de 20 minutos** con visualización en tiempo real
- **Sistema de puntuación**: +1 por correcta, -0.25 por incorrecta
- **Revisión completa** de todas las preguntas con explicaciones
- **Historial de intentos** guardado en Supabase
- **Accesible SIN autenticación** - cualquiera puede hacer el test

### 📁 Archivos Creados/Modificados

1. **`src/components/PabloTest17Oct.jsx`** - Componente principal del test
2. **`src/utils/pabloTestStorage.js`** - Funciones para guardar/cargar datos
3. **`src/App.jsx`** - Modificado para incluir el botón de acceso
4. **`INSTRUCCIONES_PABLO_TEST.md`** - Este archivo

### 🗄️ Configuración de Supabase

**IMPORTANTE**: Debes ejecutar el siguiente SQL en tu panel de Supabase para crear la tabla necesaria:

```sql
-- Crear tabla para almacenar los resultados del test de Pablo
CREATE TABLE IF NOT EXISTS pablo_test_results (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  fecha TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  tiempo_empleado INTEGER NOT NULL, -- en segundos
  correctas INTEGER NOT NULL,
  incorrectas INTEGER NOT NULL,
  en_blanco INTEGER NOT NULL,
  nota_final DECIMAL(5,2) NOT NULL,
  porcentaje DECIMAL(5,2) NOT NULL,
  preguntas JSONB NOT NULL, -- array de preguntas con respuestas
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Crear índice por fecha para consultas rápidas
CREATE INDEX idx_pablo_test_fecha ON pablo_test_results(fecha DESC);

-- Habilitar Row Level Security
ALTER TABLE pablo_test_results ENABLE ROW LEVEL SECURITY;

-- Política para permitir INSERT a todos (sin autenticación)
CREATE POLICY "Permitir insertar resultados a todos"
  ON pablo_test_results
  FOR INSERT
  WITH CHECK (true);

-- Política para permitir SELECT a todos (sin autenticación)
CREATE POLICY "Permitir leer resultados a todos"
  ON pablo_test_results
  FOR SELECT
  USING (true);

-- Comentarios para documentación
COMMENT ON TABLE pablo_test_results IS 'Almacena los resultados del Test de Pablo 17/10/25 sin requerir autenticación';
COMMENT ON COLUMN pablo_test_results.tiempo_empleado IS 'Tiempo empleado en segundos';
COMMENT ON COLUMN pablo_test_results.preguntas IS 'Array JSON con las preguntas y respuestas del intento';
```

### 📝 Pasos para Configurar

1. **Ir a Supabase Dashboard**
   - Abre tu proyecto en https://supabase.com
   - Ve a la sección "SQL Editor"

2. **Ejecutar el SQL**
   - Copia el SQL de arriba
   - Pégalo en el editor SQL
   - Haz clic en "Run" para ejecutarlo

3. **Verificar la tabla**
   - Ve a "Table Editor"
   - Deberías ver la tabla `pablo_test_results` creada
   - Verifica que tenga las políticas RLS habilitadas

### 🚀 Uso del Test

#### Para usuarios SIN login:
- En la pantalla de login, verás un botón **"🎯 Test de Pablo 17/10/25 (Sin Login)"**
- Haz clic para acceder directamente al test

#### Para usuarios CON login:
- En la pantalla principal, encontrarás el botón **"🎯 Test de Pablo 17/10/25"**
- También disponible en el hero section junto a "Comenzar simulacro"

### 📊 Funcionalidades del Test

1. **Pantalla de Inicio**
   - Descripción del test
   - Botones para iniciar o ver historial

2. **Durante el Test**
   - Temporizador visible en todo momento
   - Barra de progreso
   - 15 preguntas con 4 opciones cada una
   - Finalización automática al acabar el tiempo

3. **Pantalla de Resultados**
   - Estadísticas completas: correctas, incorrectas, en blanco
   - Nota final con descuento por fallo
   - Revisión detallada de cada pregunta
   - Explicaciones de las respuestas correctas

4. **Historial**
   - Todos los intentos guardados en Supabase
   - Ordenados por fecha (más reciente primero)
   - Estadísticas resumidas de cada intento

### 🔒 Seguridad y Privacidad

- Los resultados se guardan de forma **anónima** (sin vincular a un usuario)
- Cualquiera puede ver todos los intentos en el historial
- Las políticas RLS permiten acceso público total a esta tabla específica
- No se requiere autenticación para ninguna funcionalidad del test

### 🎨 Diseño Visual

- Gradientes morados y azules característicos
- Interfaz moderna y responsive
- Animaciones suaves en transiciones
- Temporizador que se vuelve rojo cuando quedan menos de 5 minutos
- Iconos y colores para identificar respuestas correctas/incorrectas

### 🐛 Solución de Problemas

Si el test no guarda los resultados:
1. Verifica que la tabla esté creada en Supabase
2. Comprueba que las políticas RLS estén configuradas correctamente
3. Revisa la consola del navegador para ver errores
4. Asegúrate de que las variables de entorno de Supabase estén configuradas

Si no aparece el botón:
1. Verifica que `src/components/PabloTest17Oct.jsx` exista
2. Comprueba que el import esté en `App.jsx`
3. Revisa que no haya errores de compilación

### 📈 Próximas Mejoras Posibles

- [ ] Exportar resultados a PDF
- [ ] Gráficos de evolución
- [ ] Comparativa con otros intentos
- [ ] Modo de repaso de preguntas falladas
- [ ] Filtros por categoría/dificultad en el historial

---

**Creado el:** 17 de octubre de 2025  
**Versión:** 1.0  
**Autor:** Asistente IA
