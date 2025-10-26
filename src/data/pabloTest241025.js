// Preguntas fijas para el "Test de Pablo" del 24/10/2025
// Formato compatible con TestRunner y PabloTest17Oct
// Campos: id, categoria, subcategoria, dificultad, pregunta, opciones[], respuestaCorrecta (índice), explicacion

export const preguntasPablo241025 = [
  {
    id: 'PAB-241025-01',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Farmacocinética clínica',
    dificultad: 'Muy alta',
    pregunta:
      'En un paciente con insuficiencia renal crónica, ¿qué parámetro farmacocinético es más relevante para ajustar la dosificación de aminoglucósidos?',
    opciones: [
      'Volumen de distribución',
      'Aclaramiento renal',
      'Unión a proteínas plasmáticas',
      'Biodisponibilidad oral',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'El aclaramiento renal es el principal determinante de la eliminación de aminoglucósidos, por lo que es crucial para ajustar la dosificación en insuficiencia renal.',
  },
  {
    id: 'PAB-241025-02',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Farmacocinética clínica',
    dificultad: 'Muy alta',
    pregunta:
      'En un paciente con obesidad mórbida, ¿qué ajuste es necesario para calcular la dosis de fármacos hidrofílicos?',
    opciones: [
      'Usar el peso corporal total',
      'Usar el peso corporal ideal',
      'Usar el peso corporal ajustado',
      'No realizar ajustes',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'En pacientes con obesidad mórbida, el peso corporal ajustado se utiliza para evitar sobredosificación de fármacos hidrofílicos, ya que su distribución se limita al agua corporal.',
  },
  {
    id: 'PAB-241025-03',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Pediatría',
    dificultad: 'Muy alta',
    pregunta:
      'En neonatos, ¿qué factor farmacocinético afecta más la eliminación de medicamentos?',
    opciones: [
      'Aclaramiento hepático',
      'Aclaramiento renal',
      'Unión a proteínas',
      'Volumen de distribución',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'En neonatos, la inmadurez renal afecta significativamente la eliminación de medicamentos, especialmente aquellos excretados por vía renal.',
  },
  {
    id: 'PAB-241025-04',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Hematología',
    dificultad: 'Muy alta',
    pregunta:
      'En un paciente con anemia aplásica severa, ¿cuál es el tratamiento de primera línea?',
    opciones: [
      'Transfusión de glóbulos rojos',
      'Terapia inmunosupresora',
      'Trasplante de médula ósea',
      'Administración de eritropoyetina',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'El trasplante de médula ósea es el tratamiento de elección en pacientes jóvenes con anemia aplásica severa y un donante compatible.',
  },
  {
    id: 'PAB-241025-05',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Cardiovascular',
    dificultad: 'Muy alta',
    pregunta:
      'En un paciente con insuficiencia cardíaca, ¿qué fármaco mejora la supervivencia a largo plazo?',
    opciones: [
      'Digoxina',
      'Furosemida',
      'Eplerenona',
      'Ivabradina',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'Eplerenona, un antagonista de la aldosterona, ha demostrado mejorar la supervivencia en pacientes con insuficiencia cardíaca.',
  },
  {
    id: 'PAB-241025-06',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Parte general',
    dificultad: 'Alta',
    pregunta:
      'Según la legislación vigente, ¿cuál es el tiempo máximo para conservar registros de dispensación de medicamentos sujetos a receta médica?',
    opciones: [
      '1 año',
      '3 años',
      '5 años',
      '10 años',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'La normativa establece un periodo de conservación de 5 años para registros de dispensación, garantizando trazabilidad y cumplimiento legal.',
  },
  {
    id: 'PAB-241025-07',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Parte general',
    dificultad: 'Muy alta',
    pregunta:
      'En farmacovigilancia hospitalaria, ¿cuál es la definición de reacción adversa grave según la OMS?',
    opciones: [
      'Cualquier evento no deseado con sospecha de causalidad',
      'Evento que requiere hospitalización o prolonga ingreso',
      'Reacción alérgica leve sin secuelas',
      'Interacción farmacológica predecible',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Según la OMS, RAM grave incluye muerte, amenaza vital, hospitalización, discapacidad o anomalía congénita; requiere notificación inmediata.',
  },
  {
    id: 'PAB-241025-08',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Parte general',
    dificultad: 'Muy alta',
    pregunta:
      'En gestión de residuos citotóxicos, ¿qué medida reduce más la exposición ocupacional durante la desconexión de líneas?',
    opciones: [
      'Uso de guantes dobles estándar',
      'Purgado con suero y sistemas CSTD',
      'Desconexión rápida sin purgado',
      'Colocación de compresas absorbentes post-desconexión',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Los CSTD y purgado previo minimizan aerosoles y gotas; son barreras críticas para reducir exposición a residuos contaminados.',
  },
  {
    id: 'PAB-241025-09',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Ensayos clínicos',
    dificultad: 'Muy alta',
    pregunta:
      'En un ensayo clínico fase III con doble ciego, ¿qué sesgo es más probable si no se usa randomización estratificada por gravedad basal?',
    opciones: [
      'Sesgo de selección por diferencias en pronóstico',
      'Sesgo de recuerdo en cuestionarios retrospectivos',
      'Sesgo de Hawthorne por observación',
      'Sesgo de publicación positiva',
    ],
    respuestaCorrecta: 0,
    explicacion:
      'Sin estratificación, grupos pueden diferir en gravedad basal, llevando a sesgo de selección y conclusiones erróneas sobre eficacia.',
  },
  {
    id: 'PAB-241025-10',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'CIM',
    dificultad: 'Alta',
    pregunta:
      '¿Qué indicador es más útil para evaluar la calidad de un servicio de información de medicamentos?',
    opciones: [
      'Número de consultas atendidas',
      'Satisfacción del usuario',
      'Tiempo promedio de respuesta',
      'Precisión de la información proporcionada',
    ],
    respuestaCorrecta: 3,
    explicacion:
      'La precisión de la información es el indicador clave para evaluar la calidad y confiabilidad de un servicio de información de medicamentos.',
  },
  {
    id: 'PAB-241025-11',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'CIM',
    dificultad: 'Muy alta',
    pregunta:
      'En vigilancia epidemiológica CIM, ¿qué indicador es más sensible para detectar brotes de infección por catéter?',
    opciones: [
      'Incidencia global de bacteriemia',
      'Densidad de incidencia por días-catéter',
      'Prevalencia de colonización nasal',
      'Tasa de uso de antibióticos profilácticos',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'La densidad de incidencia (infecciones/1000 días-catéter) ajusta por exposición al riesgo, siendo más sensible para comparar unidades.',
  },
  {
    id: 'PAB-241025-12',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Cardiovascular',
    dificultad: 'Muy alta',
    pregunta:
      'En insuficiencia cardíaca descompensada, ¿qué ajuste de digoxina requiere monitorización de niveles plasmáticos?',
    opciones: [
      'Aumento por interacción con amiodarona',
      'Disminución por hipopotasemia inducida por diuréticos',
      'Aumento por insuficiencia renal concomitante',
      'Disminución por hipercalcemia',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Diuréticos deplecionan potasio, aumentando toxicidad de digoxina; requiere reducción de dosis y monitorización de niveles.',
  },
  {
    id: 'PAB-241025-13',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Reumatología',
    dificultad: 'Muy alta',
    pregunta:
      'En artritis reumatoide refractaria, ¿qué biológico requiere screening previo para tuberculosis latente?',
    opciones: [
      'Abatacept por mecanismo de coestimulación',
      'Tocilizumab por inhibición de IL-6',
      'Adalimumab por anti-TNF',
      'Rituximab por depleción de B células',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'Anti-TNF como adalimumab reactivan tuberculosis latente; requiere screening y profilaxis antes de iniciar tratamiento.',
  },
  {
    id: 'PAB-241025-14',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Infecciosas',
    dificultad: 'Muy alta',
    pregunta:
      'En neumonía por Pseudomonas aeruginosa multirresistente, ¿cuál es el régimen empírico más apropiado considerando sinergia?',
    opciones: [
      'Meropenem + amikacina por actividad antipseudomona',
      'Ceftazidima + ciprofloxacino por doble cobertura',
      'Piperacilina/tazobactam + colistina por resistencia extendida',
      'Imipenem + gentamicina por efecto postantibiótico',
    ],
    respuestaCorrecta: 2,
    explicacion:
      'En Pseudomonas MDR, piperacilina/tazobactam + colistina proporciona cobertura amplia; colistina es reserva para resistencias extendidas.',
  },
  {
    id: 'PAB-241025-16',
    categoria: 'Farmacia Hospitalaria',
    subcategoria: 'Farmacoeconomía',
    dificultad: 'Alta',
    pregunta:
      '¿Qué indicador se utiliza para evaluar la relación coste-efectividad de un medicamento?',
    opciones: [
      'Número necesario a tratar (NNT)',
      'Años de vida ajustados por calidad (AVAC)',
      'Tasa de eventos adversos prevenidos',
      'Incremento en la supervivencia global',
    ],
    respuestaCorrecta: 1,
    explicacion:
      'Los AVAC son una medida estándar en farmacoeconomía para evaluar la relación coste-efectividad, combinando cantidad y calidad de vida ganada.',
  },
];
