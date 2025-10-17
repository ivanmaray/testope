// Preguntas fijas para el "Test de Pablo" del 17/10/2025
// Formato compatible con TestRunner y PabloTest17Oct
// Campos: id, categoria, subcategoria, dificultad, pregunta, opciones[], respuestaCorrecta (índice), explicacion

export const preguntasPablo171025 = [
  {
    id: 'PAB-171025-01',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Farmacocinética clínica',
    dificultad: 'Alta',
    pregunta:
      'En un paciente crítico con sepsis y aclaramiento renal aumentado (ARC), ¿qué ajuste es más apropiado para un beta-lactámico tiempo-dependiente (p. ej., piperacilina/tazobactam) con T>MIC objetivo ≥ 50%?',
    opciones: [
      'Aumentar dosis en bolo manteniendo intervalo',
      'Acortar el intervalo entre bolos sin cambiar la dosis',
      'Administración en perfusión prolongada/continua',
      'Reducir dosis para evitar toxicidad por acumulación',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'En ARC aumenta el aclaramiento y se reduce el tiempo por encima de la MIC con bolos convencionales. Los beta-lactámicos son tiempo-dependientes; la perfusión prolongada o continua optimiza T>MIC sin necesidad de picos elevados.',
  },
  {
    id: 'PAB-171025-02',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Ajuste dosis renal',
    dificultad: 'Alta',
    pregunta:
      'Para un fármaco hidrofílico, bajo volumen de distribución y eliminación predominantemente renal (p. ej., vancomicina), ¿qué cambio farmacocinético es más esperable en edema generalizado y fluidoterapia intensiva?',
    opciones: [
      'Disminución del volumen de distribución y aumento de Cmax',
      'Aumento del volumen de distribución y descenso de concentraciones iniciales',
      'Aumento de unión a proteínas plasmáticas y menor fracción libre',
      'Disminución del aclaramiento renal por hemodilución',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'El aumento del espacio extracelular en estados de sobrecarga hídrica incrementa el Vd de fármacos hidrofílicos, reduciendo concentraciones iniciales; puede requerir dosis de carga mayores para alcanzar objetivos.',
  },
  {
    id: 'PAB-171025-03',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Antimicrobianos · PK/PD',
    dificultad: 'Alta',
    pregunta:
      '¿Cuál es el mejor índice PK/PD predictor de eficacia para los aminoglucósidos en infecciones graves?',
    opciones: [
      'T>MIC',
      'AUC/MIC',
      'Cmax/MIC',
      'Tiempo hasta picosúrica',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'Los aminoglucósidos son concentración-dependientes; el cociente Cmax/MIC (idealmente ≥ 8-10) se asocia con mejor respuesta clínica.',
  },
  {
    id: 'PAB-171025-04',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Oncohematología · Seguridad',
    dificultad: 'Muy alta',
    pregunta:
      'Según buenas prácticas de manipulación de citotóxicos, ¿cuál es la medida más crítica para prevenir exposición del personal durante la desconexión de líneas tras una perfusión de quimioterapia?',
    opciones: [
      'Uso exclusivo de guantes dobles',
      'Purgado previo con suero y sistemas cerrados de transferencia',
      'Retirada rápida de la línea para minimizar goteo',
      'Colocar gasas absorbentes sin otros cambios',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Los sistemas cerrados de transferencia (CSTD) y el purgado con suero antes de la desconexión reducen la liberación de aerosoles y gotas contaminadas; es una barrera clave junto al EPI.',
  },
  {
    id: 'PAB-171025-05',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Nutrición Parenteral',
    dificultad: 'Alta',
    pregunta:
      'En una NPT, ¿qué combinación favorece con mayor probabilidad la precipitación de fosfato cálcico?',
    opciones: [
      'pH más bajo, aminoácidos elevados, fosfato orgánico',
      'pH más alto, calcio iónico elevado, fosfato inorgánico',
      'Osmolaridad elevada por dextrosa',
      'Lípidos al 20% en mezcla ternaria',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'El riesgo de precipitado Ca–P aumenta con pH más alto, altas concentraciones de calcio iónico y uso de fosfato inorgánico. Los AA y fosfatos orgánicos ayudan a reducirlo.',
  },
  {
    id: 'PAB-171025-06',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Infectología · Monitorización',
    dificultad: 'Alta',
    pregunta:
      'Objetivo terapéutico recomendado para vancomicina en neumonía por S. aureus sensible con MIC 1 mg/L (método fiable):',
    opciones: [
      'Cmin 15–20 mg/L sin considerar AUC',
      'AUC24/MIC 400–600 (monitorización por AUC)',
      'Cmax/MIC >10',
      'AUC24/MIC 200–300',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Las guías actuales recomiendan AUC24/MIC 400–600 (método bayesiano o dos puntos) para balancear eficacia y nefrotoxicidad; Cmin aislada es menos precisa.',
  },
  {
    id: 'PAB-171025-07',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Compatibilidades · Y-site',
    dificultad: 'Alta',
    pregunta:
      'Se precisa coadministrar por Y-site meropenem y una perfusión continua de norepinefrina en un acceso limitado. ¿Cuál es la recomendación más segura?',
    opciones: [
      'Compatibles en todo rango de concentraciones',
      'Incompatibles: usar lumen independiente o espaciar con lavado riguroso',
      'Solo compatibles si el pH final es > 7,5',
      'Intercambiar por imipenem para mejorar compatibilidad',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Numerosas referencias indican incompatibilidad o datos insuficientes para Y-site entre meropenem y catecolaminas; se recomienda lumen separado o separación temporal con lavados.',
  },
  {
    id: 'PAB-171025-08',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Farmacotecnia estéril',
    dificultad: 'Muy alta',
    pregunta:
      'En preparación aséptica de dosis unitarias, ¿qué indicador es más representativo del control ambiental operativo en cabina de flujo laminar Clase A?',
    opciones: [
      'Recuento de partículas por contador óptico únicamente',
      'Placas de sedimentación pasiva 2h/4h en superficies cercanas a zona crítica',
      'Muestreo activo de aire (volumen conocido) y hisopados de guantes pos-proceso',
      'Medición de presión diferencial entre salas una vez al mes',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'El control ambiental operativo incluye muestreo activo de aire (UFC/m3) y monitorización del operador (guantes/ropa) tras actividad; complementa partículas y diferenciales de presión.',
  },
  {
    id: 'PAB-171025-09',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Legislación y gestión',
    dificultad: 'Alta',
    pregunta:
      'En el marco español, ¿qué aspecto describe mejor la liberación de una fórmula magistral estéril de alto riesgo?',
    opciones: [
      'Solo requiere revisión documental y etiquetado',
      'Debe incluir control microbiológico o de esterilidad según riesgo y validación de proceso',
      'No precisa trazabilidad por ser uso individualizado',
      'Se libera por el médico prescriptor sin intervención farmacéutica',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Las preparaciones estériles de alto riesgo requieren validación de proceso y, cuando procede, controles de esterilidad. La trazabilidad y liberación farmacéutica son obligatorias.',
  },
  {
    id: 'PAB-171025-10',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Antifúngicos · PK/PD',
    dificultad: 'Alta',
    pregunta:
      'En aspergilosis invasiva tratada con voriconazol, ¿cuál es el rango de concentraciones valle objetivo más aceptado para maximizar eficacia y minimizar toxicidad?',
    opciones: [
      '0,5–1,0 mg/L',
      '1,0–2,0 mg/L',
      '2,0–5,5 mg/L',
      '5,5–8,0 mg/L',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'Las guías suelen recomendar Cmin de 2–5,5 mg/L para equilibrio eficacia/seguridad; >5,5 mg/L se asocia a mayor toxicidad neurológica/visual.',
  },
  {
    id: 'PAB-171025-11',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Seguridad del paciente',
    dificultad: 'Alta',
    pregunta:
      '¿Qué intervención del servicio de farmacia reduce más los errores de conciliación al ingreso hospitalario?',
    opciones: [
      'Formación anual a todo el personal médico',
      'Conciliación estructurada por farmacéuticos con múltiples fuentes de información',
      'Revisión de prescripciones 24-48 h después del ingreso',
      'Entrega de folleto informativo al paciente en urgencias',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'La conciliación realizada por farmacéuticos usando ≥2 fuentes (entrevista, receta electrónica, informe) y validación clínica reduce significativamente discrepancias no intencionadas.',
  },
  {
    id: 'PAB-171025-12',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Oncología · Dosificación',
    dificultad: 'Alta',
    pregunta:
      'En quimioterapia dosificada por AUC de carboplatino (fórmula Calvert), ¿qué estimación de función renal es la más apropiada para minimizar infra/sobredosificación?',
    opciones: [
      'Aclaramiento de creatinina por Cockcroft-Gault con peso actual siempre',
      'MDRD-4 sin ajuste',
      'CKD-EPI 2021 y, en extremos, medición directa o ajuste por peso ideal/corregido',
      'Ninguna estimación afecta de forma relevante a la AUC',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'La estimación precisa de FG impacta directamente en la AUC de carboplatino. CKD-EPI (2021) es preferible; considerar peso ideal/corregido o medición en casos especiales.',
  },
  {
    id: 'PAB-171025-13',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Estabilidad · Preparaciones',
    dificultad: 'Alta',
    pregunta:
      'Respecto a la estabilidad de soluciones intravenosas, señale la opción correcta:',
    opciones: [
      'La degradación por hidrólisis se minimiza aumentando el pH de forma general',
      'La fotodegradación de nitroprusiato se evita con envase opaco y filtros UV',
      'La oxidación no depende de la presencia de oxígeno disuelto',
      'La temperatura no afecta a la velocidad de degradación',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Nitroprusiato es fotosensible; requiere protección de la luz. La hidrólisis y oxidación dependen de pH y oxígeno; la temperatura acelera reacciones (Arrhenius).',
  },
  {
    id: 'PAB-171025-14',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Antimicrobianos · Dosis',
    dificultad: 'Muy alta',
    pregunta:
      'Paciente con IMC 42 kg/m² y función renal normal: respecto a daptomicina, señale lo más adecuado para dosificación y monitorización de seguridad:',
    opciones: [
      'Dosificar por peso ideal y controlar CK basal',
      'Dosificar por peso actual con tope absoluto fijo',
      'Considerar peso ajustado o actual según guía local y monitorizar CPK semanal',
      'No precisa ningún ajuste por obesidad',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'En obesidad puede usarse peso ajustado o actual según protocolos para evitar sobredosis; daptomicina requiere monitorizar CPK por riesgo de miopatía, especialmente con estatinas.',
  },
  {
    id: 'PAB-171025-15',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Farmacovigilancia',
    dificultad: 'Alta',
    pregunta:
      'Se detecta una sospecha de reacción adversa grave e inesperada en un uso fuera de ficha técnica. ¿Cuál es la mejor actuación del farmacéutico hospitalario?',
    opciones: [
      'Notificar al sistema nacional de farmacovigilancia y documentar en historia clínica',
      'Notificar solo al laboratorio titular del medicamento',
      'Esperar confirmación del médico prescriptor antes de actuar',
      'Registrar internamente sin notificar',
    ],
    respuestaCorrecta: 0,
    explicacion:
      'Las sospechas de RAM graves/inesperadas deben notificarse al Sistema Español de Farmacovigilancia y quedar documentadas; no es necesario esperar confirmación diagnóstica definitiva.',
  },
];
