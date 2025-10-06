import json
from pathlib import Path

questions = []

counter = 1

def add_question(categoria, subcategoria, dificultad, pregunta, opciones, respuesta_correcta, explicacion):
    global counter
    question = {
        "id": f"onco-{counter:03d}",
        "categoria": categoria,
        "subcategoria": subcategoria,
        "dificultad": dificultad,
        "pregunta": pregunta,
        "opciones": opciones,
        "respuestaCorrecta": respuesta_correcta,
        "explicacion": explicacion,
    }
    questions.append(question)
    counter += 1


# Tumores sólidos - Mama
add_question(
    "Tumores sólidos",
    "Mama",
    "Básico",
    "¿Qué receptor hormonal define el subtipo luminal A de cáncer de mama?",
    [
        "Receptor de estrógeno positivo y HER2 negativo",
        "Receptor de progesterona negativo",
        "HER2 positivo y Ki-67 alto",
        "Triple negativo",
    ],
    0,
    "El subtipo luminal A se caracteriza por receptores hormonales positivos (principalmente estrógeno) y ausencia de sobreexpresión de HER2, con baja proliferación.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Básico",
    "¿Qué prueba de imagen es la base del cribado poblacional del cáncer de mama?",
    [
        "Mamografía",
        "Resonancia magnética",
        "Ecografía",
        "Tomosíntesis contrastada",
    ],
    0,
    "La mamografía es la técnica estándar de cribado en población general femenina, al detectar microcalcificaciones y lesiones sospechosas en fases precoces.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Intermedio",
    "¿Qué fármaco anti-HER2 se asocia a cardiotoxicidad reversible y requiere monitorización de fracción de eyección?",
    [
        "Trastuzumab",
        "Pertuzumab",
        "Lapatinib",
        "Tucatinib",
    ],
    0,
    "El trastuzumab puede inducir disfunción ventricular reversible; por ello se monitoriza la fracción de eyección periódicamente durante el tratamiento.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Intermedio",
    "En cáncer de mama estadio inicial con receptores hormonales positivos, ¿qué tratamiento adyuvante disminuye el riesgo de recaída?",
    [
        "Terapia endocrina",
        "Quimioterapia con antraciclinas",
        "Inhibidores de PARP",
        "Inmunoterapia con anti-PD-1",
    ],
    0,
    "En tumores con receptores hormonales positivos, la terapia endocrina (tamoxifeno o inhibidores de aromatasa) es clave para reducir recurrencias tras la cirugía.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Intermedio",
    "¿Cuál es la indicación principal de la prueba multigénica (Oncotype DX u otras) en cáncer de mama?",
    [
        "Determinar el beneficio de quimioterapia adyuvante en tumores luminales",
        "Seleccionar candidatas a terapia anti-HER2",
        "Definir respuesta a radiofrecuencia",
        "Detectar mutaciones germinales de BRCA",
    ],
    0,
    "Las firmas genómicas ayudan a estimar riesgo de recaída en tumores luminales y decidir si la paciente se beneficia de añadir quimioterapia a la endocrina.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Avanzado",
    "En cáncer de mama metastásico triple negativo con expresión de PD-L1, ¿qué combinación ha mostrado beneficio en supervivencia global?",
    [
        "Atezolizumab + nab-paclitaxel",
        "Trastuzumab + paclitaxel",
        "Capecitabina + bevacizumab",
        "Talazoparib en monoterapia",
    ],
    0,
    "En tumores triple negativos PD-L1 positivos, la combinación de atezolizumab con nab-paclitaxel demostró mejora en supervivencia global frente a quimioterapia sola.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Avanzado",
    "¿Cuál es la principal toxicidad limitante del uso de inhibidores de CDK4/6 como palbociclib?",
    [
        "Neutropenia",
        "Cardiotoxicidad",
        "Retraso del crecimiento óseo",
        "Neurotoxicidad periférica",
    ],
    0,
    "Los inhibidores de CDK4/6 producen neutropenia reversible como efecto adverso más frecuente, por lo que se monitoriza hemograma regularmente.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Avanzado",
    "¿Qué mutación germinal condiciona el uso de inhibidores de PARP en cáncer de mama metastásico?",
    [
        "BRCA1 o BRCA2",
        "PIK3CA",
        "ESR1",
        "HER2",
    ],
    0,
    "Los pacientes con mutaciones germinales en BRCA1/2 se benefician de inhibidores de PARP como olaparib o talazoparib en enfermedad metastásica.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Básico",
    "¿Cuál es el margen quirúrgico considerado adecuado tras una tumorectomía con radioterapia adyuvante?",
    [
        "Margen negativo (no tinta en el tumor)",
        "Al menos 1 cm de margen",
        "Margen negativo y 5 mm libres",
        "Margen positivo aceptado si se aplica boost",
    ],
    0,
    "En cirugía conservadora de mama, la recomendación es no tinta en el tumor; márgenes negativos microscópicos son suficientes junto con radioterapia.",
)

add_question(
    "Tumores sólidos",
    "Mama",
    "Intermedio",
    "¿Qué hallazgo clínico obliga a descartar enfermedad inflamatoria de mama?",
    [
        "Eritema difuso y edema cutáneo en piel de naranja",
        "Nódulo móvil de 1 cm",
        "Secreción serosa intermitente",
        "Dolor cíclico",
    ],
    0,
    "El cáncer de mama inflamatorio se caracteriza por eritema difuso, calor y edema en piel de naranja; requiere diagnóstico y tratamiento sistémico urgente.",
)

# Tumores sólidos - Pulmón
add_question(
    "Tumores sólidos",
    "Pulmón",
    "Básico",
    "En el cribado de cáncer de pulmón en alto riesgo, ¿qué prueba se recomienda?",
    [
        "Tomografía computarizada de baja dosis",
        "Radiografía de tórax anual",
        "PET-TC",
        "Resonancia magnética",
    ],
    0,
    "Los programas de cribado en fumadores de alto riesgo utilizan TAC de baja dosis anual, que reduce mortalidad por cáncer de pulmón.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Básico",
    "¿Qué mutación driver es más frecuente en adenocarcinoma de pulmón en no fumadores?",
    [
        "Mutaciones activadoras de EGFR",
        "Reordenamientos de ALK",
        "Mutaciones de KRAS G12C",
        "Amplificaciones de MET",
    ],
    0,
    "Las mutaciones activadoras de EGFR son comunes en adenocarcinoma en no fumadores y permiten terapia dirigida con inhibidores de EGFR.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Intermedio",
    "En cáncer de pulmón no microcítico estadio IIIA irresecable, ¿cuál es el tratamiento estándar inicial?",
    [
        "Quimiorradioterapia concurrente",
        "Quimioterapia seguida de cirugía",
        "Resección quirúrgica primaria",
        "Inmunoterapia neoadyuvante",
    ],
    0,
    "La quimiorradioterapia concurrente es la estrategia estándar para enfermedad localmente avanzada irresecable, buscando control locorregional.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Intermedio",
    "¿Qué biomarcador define la indicación de pembrolizumab en monoterapia en primera línea de cáncer de pulmón no microcítico avanzado?",
    [
        "PD-L1 ≥50%",
        "Mutación EGFR",
        "Reordenamiento ALK",
        "Amplificación ERBB2",
    ],
    0,
    "Pembrolizumab puede emplearse en monoterapia si la expresión de PD-L1 mediante TPS es ≥50% y no hay dianas accionables.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Avanzado",
    "En pacientes con mutación EGFR y progresión tras osimertinib, ¿qué opción terapéutica exploratoria gana relevancia?",
    [
        "Combinaciones con amivantamab + lazertinib",
        "Quimioterapia con cisplatino-vinorelbina",
        "Radioterapia holocraneal profiláctica",
        "Ipilimumab en monoterapia",
    ],
    0,
    "Tras progresión a osimertinib, se investigan combinaciones como amivantamab (anti-EGFR/MET) con lazertinib para abordar mecanismos de resistencia.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Básico",
    "¿Qué síndrome paraneoplásico se asocia con más frecuencia al carcinoma microcítico de pulmón?",
    [
        "Secreción ectópica de ACTH",
        "Hipercalcemia",
        "Hipoglucemia",
        "Síndrome de Trousseau",
    ],
    0,
    "El carcinoma microcítico produce frecuentemente secreción ectópica de ACTH, generando síndrome de Cushing paraneoplásico.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Intermedio",
    "¿Cuál es la recomendación tras completar quimiorradioterapia en estadio III irresecable con PD-L1 ≥1%?",
    [
        "Consolidación con durvalumab por 12 meses",
        "Quimioterapia adicional con cisplatino",
        "Cirugía de rescate",
        "Radiofrecuencia pulmonar",
    ],
    0,
    "Durvalumab durante un año tras quimiorradioterapia mejora supervivencia libre de progresión y global en pacientes con PD-L1 ≥1%.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Avanzado",
    "En enfermedad oligometastásica inicial, ¿qué beneficio aporta la radioterapia estereotáxica sobre todas las lesiones?",
    [
        "Mejora la supervivencia libre de progresión en combinación con tratamiento sistémico",
        "Sustituye la enucleación metastásica",
        "Permite suspender la terapia sistémica",
        "No ofrece beneficio demostrado",
    ],
    0,
    "En estudios fase II, la radioterapia estereotáxica sobre todas las lesiones oligometastásicas junto a tratamiento sistémico prolonga la supervivencia libre de progresión.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Avanzado",
    "¿Qué toxicidad obliga a suspender inmunoterapia anti-PD-1/PD-L1 en cáncer de pulmón si aparece grado 3?",
    [
        "Neumonitis",
        "Hipotiroidismo",
        "Rash cutáneo leve",
        "Artralgias",
    ],
    0,
    "La neumonitis inmune grado 3 requiere suspensión de la inmunoterapia y tratamiento inmediato con corticoides a altas dosis.",
)

add_question(
    "Tumores sólidos",
    "Pulmón",
    "Intermedio",
    "¿Cuál es la principal causa de resistencia primaria a inhibidores de ALK?",
    [
        "Mutaciones de activación de EGFR",
        "MET amplificado",
        "Expresión de PD-L1",
        "Inactivación de STK11",
    ],
    0,
    "La activación de vías alternativas como EGFR puede conferir resistencia primaria a inhibidores de ALK; se estudian combinaciones para superarla.",
)

# Tumores sólidos - Digestivo
add_question(
    "Tumores sólidos",
    "Digestivo",
    "Básico",
    "¿Qué prueba de cribado reduce la mortalidad por cáncer colorrectal y permite resección de pólipos?",
    [
        "Colonoscopia",
        "TC abdominal",
        "Ecografía endoscópica",
        "Tránsito intestinal",
    ],
    0,
    "La colonoscopia permite detectar lesiones precursoras y extirpar pólipos, disminuyendo mortalidad por cáncer colorrectal.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Básico",
    "¿Qué marcador orienta al seguimiento en carcinoma hepatocelular?",
    [
        "Alfa-fetoproteína",
        "CEA",
        "CA 19-9",
        "Calcitonina",
    ],
    0,
    "La alfa-fetoproteína se utiliza junto a la imagen para diagnóstico y seguimiento de hepatocarcinoma, aunque no es exclusiva.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Intermedio",
    "En cáncer colorrectal metastásico RAS wild-type, ¿qué factor contraindica anti-EGFR como cetuximab?",
    [
        "Tumor primario en colon derecho",
        "Metástasis hepática",
        "Elevado CEA",
        "Cirrosis compensada",
    ],
    0,
    "Los tumores del colon derecho responden peor a anti-EGFR en primera línea, por lo que se prefieren combinaciones con bevacizumab.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Intermedio",
    "¿Qué esquema perioperatorio es estándar en adenocarcinoma gástrico resecable localmente avanzado?",
    [
        "FLOT (5-FU, leucovorina, oxaliplatino, docetaxel)",
        "Capecitabina adyuvante",
        "FOLFOX neoadyuvante",
        "Radioquimioterapia con cisplatino",
    ],
    0,
    "El esquema FLOT perioperatorio ha demostrado mejorar supervivencia frente a regímenes anteriores en adenocarcinoma gástrico resecable.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Avanzado",
    "En carcinoma hepatocelular avanzado, ¿qué combinación sistémica es estándar de primera línea?",
    [
        "Atezolizumab + bevacizumab",
        "Sorafenib",
        "Regorafenib",
        "Nivolumab",
    ],
    0,
    "Atezolizumab más bevacizumab mostró superioridad frente a sorafenib en supervivencia global y libre de progresión.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Básico",
    "¿Qué enfermedad inflamatoria intestinal incrementa el riesgo de cáncer colorrectal tras 8-10 años de evolución?",
    [
        "Colitis ulcerosa extensa",
        "Enfermedad celíaca",
        "Colitis microscópica",
        "Diverticulitis",
    ],
    0,
    "La colitis ulcerosa extensa aumenta riesgo de cáncer colorrectal tras años de actividad, requiriendo colonoscopias de vigilancia.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Intermedio",
    "En tumores neuroendocrinos pancreáticos G2, ¿qué fármaco dirigido bloquea mTOR?",
    [
        "Everolimus",
        "Sunitinib",
        "Lenvatinib",
        "Pazopanib",
    ],
    0,
    "Everolimus inhibe mTOR y controla el crecimiento de tumores neuroendocrinos bien diferenciados pancreáticos.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Avanzado",
    "¿Qué alteración justifica el uso de pembrolizumab en cáncer colorrectal metastásico refractario?",
    [
        "Inestabilidad de microsatélites alta (MSI-H)",
        "Mutación KRAS",
        "Sobreexpresión HER2",
        "Amplificación FGFR2",
    ],
    0,
    "Los tumores MSI-H o dMMR responden a inmunoterapia con pembrolizumab o nivolumab incluso tras líneas previas.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Intermedio",
    "¿Qué técnica complementa la ecoendoscopia para estadificar cáncer de páncreas?",
    [
        "Tomografía con contraste trifásico",
        "PET-TC",
        "Resonancia cerebral",
        "Gammagrafía ósea",
    ],
    0,
    "La TAC con contraste arterial y portal permite valorar resecabilidad vascular en cáncer de páncreas.",
)

add_question(
    "Tumores sólidos",
    "Digestivo",
    "Avanzado",
    "En carcinoma colorrectal metastásico con mutación BRAF V600E, ¿qué combinación dirigida mejora la supervivencia?",
    [
        "Encorafenib + cetuximab",
        "Trametinib + bevacizumab",
        "Cobimetinib + pembrolizumab",
        "Vemurafenib + panitumumab + irinotecán",
    ],
    0,
    "La combinación encorafenib + cetuximab demostró beneficio en supervivencia tras progresión a quimioterapia.",
)

# Tumores sólidos - Ginecológico
add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Básico",
    "¿Cuál es la principal prueba de cribado para cáncer de cérvix?",
    [
        "Test de VPH y citología",
        "Resonancia magnética",
        "Ecografía transvaginal",
        "CA-125 sérico",
    ],
    0,
    "El cribado se basa en test de VPH de alto riesgo y/o citología para detectar lesiones precancerosas cervicales.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Básico",
    "¿Cuál es el tratamiento estándar para cáncer de endometrio estadio inicial de bajo riesgo?",
    [
        "Histerectomía total con salpingooforectomía bilateral",
        "Quimioterapia con carboplatino",
        "Radioterapia externa",
        "Inmunoterapia",
    ],
    0,
    "La cirugía, generalmente por vía mínimamente invasiva, es curativa en estadios iniciales de bajo riesgo.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Intermedio",
    "En cáncer de ovario epitelial avanzado, ¿qué terapia de mantenimiento se recomienda tras respuesta a platinos en pacientes BRCA mutadas?",
    [
        "Olaparib",
        "Bevacizumab",
        "Paclitaxel semanal",
        "Pembrolizumab",
    ],
    0,
    "Olaparib en mantenimiento prolonga la supervivencia libre de progresión en pacientes con mutación BRCA tras respuesta a platinos.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Intermedio",
    "¿Qué estadio FIGO de cáncer de cérvix se trata con radioquimioterapia definitiva?",
    [
        "IIB",
        "IA1",
        "IB1",
        "IIA1",
    ],
    0,
    "La afectación parametrial (estadio IIB) impide la cirugía radical primaria y se maneja con radioquimioterapia concurrente.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Avanzado",
    "¿Qué terapia dirigida se emplea en cáncer de endometrio avanzado con inestabilidad de microsatélites?",
    [
        "Pembrolizumab",
        "Bevacizumab",
        "Rucaparib",
        "Pazopanib",
    ],
    0,
    "Los tumores MSI-H responden a inhibidores de PD-1 como pembrolizumab tras quimioterapia.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Básico",
    "¿Qué factor incrementa el riesgo de cáncer de endometrio tipo I?",
    [
        "Obesidad y anovulación crónica",
        "Uso prolongado de anticonceptivos combinados",
        "Historia de embarazos múltiples",
        "Tabaquismo",
    ],
    0,
    "La exposición prolongada a estrógenos sin oposición (como en obesidad o síndrome de ovario poliquístico) eleva el riesgo de cáncer endometrioide.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Intermedio",
    "¿Qué rol tiene la cirugía de citorreducción secundaria en cáncer de ovario sensible a platinos?",
    [
        "Mejora la supervivencia si se logra resección completa",
        "Solo palia síntomas",
        "Se contraindica en recaída",
        "Sustituye a la quimioterapia",
    ],
    0,
    "En pacientes seleccionadas con recaída platino-sensible, la citorreducción secundaria completa mejora supervivencia global.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Avanzado",
    "¿Qué combinación se usa en cáncer de ovario platino-resistente con sobreexpresión de FRα?",
    [
        "Mirvetuximab soravtansine + bevacizumab",
        "Trabectedina + doxorrubicina",
        "Pazopanib + gemcitabina",
        "Ipilimumab + nivolumab",
    ],
    0,
    "Mirvetuximab, un conjugado anti-FRα, combinado con bevacizumab mejora respuestas en tumores con alta expresión del receptor folato α.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Avanzado",
    "En cáncer de cuello uterino metastásico PD-L1 positivo, ¿qué añade pembrolizumab al tratamiento estándar?",
    [
        "Incrementa supervivencia global combinado con quimioterapia ± bevacizumab",
        "Sustituye totalmente la quimioterapia",
        "Solo reduce toxicidad",
        "Evita la radioterapia",
    ],
    0,
    "El estudio KEYNOTE-826 mostró beneficio en supervivencia global al añadir pembrolizumab a quimioterapia con o sin bevacizumab.",
)

add_question(
    "Tumores sólidos",
    "Ginecológico",
    "Intermedio",
    "¿Qué prueba genética se recomienda en cáncer de ovario epitelial de alto grado?",
    [
        "Estudio germinal y somático de BRCA1/2",
        "Panel de genes cardiacos",
        "Estudio de RET",
        "Análisis KRAS",
    ],
    0,
    "Se aconseja realizar estudio germinal y somático de BRCA porque condiciona terapia con inhibidores de PARP y asesoramiento familiar.",
)

# Tumores sólidos - Urológico
add_question(
    "Tumores sólidos",
    "Urológico",
    "Básico",
    "¿Qué marcador tumoral es útil para seguimiento de cáncer de próstata?",
    [
        "PSA",
        "CA 19-9",
        "Calcitonina",
        "CA 125",
    ],
    0,
    "El PSA se emplea en cribado, diagnóstico y seguimiento del cáncer de próstata, aunque no es específico.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Básico",
    "En cáncer de vejiga músculo invasivo, ¿cuál es el tratamiento estándar?",
    [
        "Cistectomía radical con quimioterapia neoadyuvante",
        "Cistoscopia cada 3 meses",
        "Radioterapia exclusiva",
        "Inmunoterapia en monoterapia",
    ],
    0,
    "La cistectomía radical precedida de quimioterapia basada en platinos es el tratamiento estándar para enfermedad músculo invasiva.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Intermedio",
    "¿Qué terapia sistémica se recomienda en carcinoma renal metastásico de riesgo intermedio/alto?",
    [
        "Combinaciones de inmunoterapia (nivolumab + ipilimumab)",
        "Interferón alfa",
        "Quimioterapia con gemcitabina",
        "Hormonoterapia",
    ],
    0,
    "Las combinaciones de inmunoterapia (nivolumab + ipilimumab) son estándar en riesgo intermedio/alto según IMDC.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Intermedio",
    "¿Qué tipo histológico de testículo requiere bleomicina-etopósido-cisplatino (BEP) como estándar?",
    [
        "Tumores de células germinales",
        "Tumores de Sertoli",
        "Carcinoma epidermoide",
        "Sarcoma paratesticular",
    ],
    0,
    "Los tumores germinales testiculares metastásicos se tratan con esquemas BEP, logrando altas tasas de curación.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Avanzado",
    "En cáncer de próstata resistente a castración con metástasis óseas, ¿qué agente radiofármaco mejora supervivencia?",
    [
        "Radium-223",
        "Estroncio-89",
        "Ytrio-90",
        "Iodo-131",
    ],
    0,
    "El radio-223 prolonga supervivencia y reduce eventos óseos en pacientes con metástasis óseas sintomáticas sin enfermedad visceral extensa.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Básico",
    "¿Qué factor de riesgo se asocia al carcinoma urotelial?",
    [
        "Tabaquismo",
        "Consumo moderado de alcohol",
        "Dieta rica en fibra",
        "Osteoporosis",
    ],
    0,
    "El tabaquismo es el principal factor de riesgo modificable para cáncer urotelial de vejiga.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Intermedio",
    "¿Cuál es la indicación de tratamiento focal con terapia focal (HIFU, cryo) en próstata?",
    [
        "En tumores localizados de bajo riesgo seleccionados",
        "En enfermedad metastásica",
        "En recidiva bioquímica",
        "En tumores de alto riesgo",
    ],
    0,
    "Las terapias focales se reservan para pacientes muy seleccionados con enfermedad localizada de bajo riesgo dentro de protocolos.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Avanzado",
    "¿Qué marcador molecular define tratamiento con inhibidores de PARP en cáncer de próstata metastásico?",
    [
        "Alteraciones en genes de reparación como BRCA1/2",
        "PTEN positivo",
        "Amplificación de EGFR",
        "Mutación ESR1",
    ],
    0,
    "Las alteraciones en genes de recombinación homóloga (BRCA1/2, ATM) identifican candidatos a inhibidores de PARP.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Intermedio",
    "¿Qué esquema neoadyuvante se emplea en cistectomía radical?",
    [
        "Cisplatino + gemcitabina",
        "Paclitaxel + carboplatino",
        "FOLFOX",
        "Docetaxel + prednisona",
    ],
    0,
    "Los regímenes basados en cisplatino (MVAC o cisplatino-gemcitabina) mejoran supervivencia en cistectomía radical.",
)

add_question(
    "Tumores sólidos",
    "Urológico",
    "Avanzado",
    "¿Qué acción tiene el lutecio-177-PSMA en cáncer de próstata metastásico?",
    [
        "Entrega radiación dirigida a células PSMA positivas",
        "Inhibe AR directamente",
        "Bloquea VEGF",
        "Estimula linfocitos T",
    ],
    0,
    "El radiofármaco lutecio-177-PSMA se une a PSMA en células tumorales y emite radiación beta para destruirlas.",
)

# Tumores sólidos - Cabeza y cuello
add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Básico",
    "¿Qué virus se asocia a carcinomas orofaríngeos positivos para p16?",
    [
        "Virus del papiloma humano",
        "Virus de Epstein-Barr",
        "Virus de la hepatitis B",
        "Citomegalovirus",
    ],
    0,
    "Los carcinomas orofaríngeos relacionados con VPH suelen ser p16 positivos y tienen mejor pronóstico.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Básico",
    "¿Cuál es el tratamiento estándar del carcinoma glótico temprano T1-T2?",
    [
        "Radioterapia o cirugía conservadora",
        "Quimioterapia exclusiva",
        "Laringectomía total",
        "Inmunoterapia",
    ],
    0,
    "En estadios tempranos, radioterapia o microcirugía endoscópica ofrecen tasas de curación elevadas preservando la función laríngea.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Intermedio",
    "¿Qué terapia sistémica se añade a la radioterapia en carcinoma de nasofaringe localmente avanzado?",
    [
        "Quimioterapia basada en platinos",
        "Cetuximab",
        "Imatinib",
        "Bevacizumab",
    ],
    0,
    "La radioquimioterapia con platinos es estándar en nasofaringe localmente avanzado debido a radiosensibilidad tumoral.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Intermedio",
    "En carcinoma de cavidad oral T3-T4 resecable, ¿qué estrategia es preferente?",
    [
        "Cirugía seguida de radio o radioquimioterapia adyuvante",
        "Radioterapia definitiva",
        "Quimioterapia neoadyuvante exclusiva",
        "Quimio-inmunoterapia",
    ],
    0,
    "La cirugía con márgenes adecuados seguida de terapia adyuvante según factores de riesgo es el estándar en tumores resecables avanzados.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Avanzado",
    "¿Qué combinación inmunoterápica se usa en recaída/metástasis tras platino?",
    [
        "Nivolumab o pembrolizumab",
        "Durvalumab + tremelimumab",
        "Ipilimumab + nivolumab",
        "Atezolizumab + bevacizumab",
    ],
    0,
    "Nivolumab o pembrolizumab están aprobados tras progresión a platino al mejorar supervivencia global.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Básico",
    "¿Qué hábito es el principal factor de riesgo para cáncer de cavidad oral?",
    [
        "Tabaquismo y consumo de alcohol",
        "Dieta rica en frutas",
        "Ejercicio regular",
        "Uso de protectores bucales",
    ],
    0,
    "La combinación de tabaco y alcohol multiplica el riesgo de carcinomas escamosos en cavidad oral.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Intermedio",
    "¿Qué complicación tardía es frecuente tras radioterapia de cabeza y cuello?",
    [
        "Xerostomía",
        "Hipertensión",
        "Retinopatía",
        "Polineuropatía",
    ],
    0,
    "La radioterapia sobre glándulas salivales produce xerostomía, que deteriora calidad de vida y favorece caries.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Avanzado",
    "En carcinoma orofaríngeo VPH positivo con buena respuesta inicial, ¿qué estrategia se investiga para reducir toxicidad?",
    [
        "De-escalada de tratamiento (dosis menores o menos quimioterapia)",
        "Aumentar dosis de radioterapia",
        "Suspender la cirugía",
        "Añadir quimioterapia intensiva",
    ],
    0,
    "Se exploran esquemas de de-escalada para reducir secuelas manteniendo control tumoral en pacientes con pronóstico favorable.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Intermedio",
    "¿Cuál es el estándar para carcinoma de laringe avanzado no resecable buscando preservación de órgano?",
    [
        "Quimiorradioterapia concurrente",
        "Laringectomía total",
        "Radioterapia exclusiva",
        "Quimioterapia adyuvante",
    ],
    0,
    "La quimiorradioterapia concurrente logra control tumoral y puede preservar la laringe en enfermedad avanzada no resecable.",
)

add_question(
    "Tumores sólidos",
    "Cabeza y cuello",
    "Avanzado",
    "¿Qué síntoma obliga a descartar osteorradionecrosis mandibular postradioterapia?",
    [
        "Exposición ósea dolorosa persistente",
        "Rinitis",
        "Disfonía transitoria",
        "Hipo",
    ],
    0,
    "La exposición ósea mandibular con dolor tras radioterapia sugiere osteorradionecrosis y requiere manejo multidisciplinar.",
)

# Tumores sólidos - Melanoma
add_question(
    "Tumores sólidos",
    "Melanoma",
    "Básico",
    "¿Qué mutación driver es más frecuente en melanoma cutáneo?",
    [
        "BRAF V600",
        "EGFR",
        "ALK",
        "RET",
    ],
    0,
    "Aproximadamente la mitad de los melanomas cutáneos presentan mutación BRAF V600, útil para terapia dirigida con BRAF/MEK.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Básico",
    "¿Cuál es el factor pronóstico más relevante en melanoma localizado?",
    [
        "Espesor de Breslow",
        "Color de la lesión",
        "Localización",
        "Edad del paciente",
    ],
    0,
    "El espesor de Breslow determina el riesgo de metástasis y la indicación de biopsia del ganglio centinela.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Intermedio",
    "¿Qué tratamiento adyuvante se recomienda en melanoma estadio III BRAF mutado tras cirugía?",
    [
        "Dabrafenib + trametinib",
        "Interferón alfa",
        "Quimioterapia con dacarbazina",
        "Imiquimod tópico",
    ],
    0,
    "La combinación de inhibidores BRAF/MEK reduce recaídas en pacientes con mutación BRAF y alto riesgo.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Intermedio",
    "¿Qué combinación inmunoterápica se usa en melanoma metastásico de alto volumen tumoral?",
    [
        "Nivolumab + ipilimumab",
        "Pembrolizumab + bevacizumab",
        "Atezolizumab + cetuximab",
        "Durvalumab + trastuzumab",
    ],
    0,
    "Nivolumab más ipilimumab aumenta la tasa de respuesta profunda en enfermedad de alto volumen, aunque con mayor toxicidad.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Avanzado",
    "En pacientes con metástasis cerebrales asintomáticas y mutación BRAF, ¿qué estrategia obtiene respuestas rápidas?",
    [
        "Inhibidores BRAF/MEK",
        "Radioterapia holocraneal",
        "Quimioterapia con temozolomida",
        "Interferón intratecal",
    ],
    0,
    "Los inhibidores BRAF/MEK proporcionan respuestas rápidas intracraneales en metastásis cerebrales de melanoma BRAF mutado.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Básico",
    "¿Qué técnica diagnóstica se utiliza para evaluar ganglio centinela en melanoma?",
    [
        "Biopsia ganglionar selectiva con linfogammagrafía previa",
        "Punción aspirativa",
        "PET-TC",
        "Ecografía Doppler",
    ],
    0,
    "La biopsia del ganglio centinela guiada por linfogammagrafía y colorante identifica micrometástasis ganglionares.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Intermedio",
    "¿Qué efecto adverso inmunomediado es frecuente con anti-PD-1?",
    [
        "Hipotiroidismo",
        "Anemia hemolítica",
        "Neuropatía desmielinizante",
        "Ceguera súbita",
    ],
    0,
    "El hipotiroidismo por tiroiditis autoinmune es frecuente con inhibidores de PD-1 y suele manejarse con levotiroxina.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Avanzado",
    "¿Qué factor predice respuesta a terapia dirigida con BRAF/MEK?",
    [
        "Mutación BRAF V600",
        "Expresión PD-L1",
        "Alteración KIT",
        "Amplificación HER2",
    ],
    0,
    "La presencia de mutación BRAF V600 es requisito para usar inhibidores de BRAF y MEK.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Básico",
    "¿Cuál es la recomendación para lesiones melanocíticas sospechosas?",
    [
        "Escisión completa con márgenes estrechos",
        "Biopsia incisional",
        "Crioterapia",
        "Láser CO2",
    ],
    0,
    "La excisión completa permite evaluar espesor y márgenes; se evita biopsia parcial para no subestimar.",
)

add_question(
    "Tumores sólidos",
    "Melanoma",
    "Avanzado",
    "¿Qué estrategia se evalúa tras respuesta completa mantenida con inmunoterapia?",
    [
        "Suspender tratamiento tras 2 años",
        "Continuar indefinidamente",
        "Cambiar a terapia dirigida",
        "Añadir radioterapia profiláctica",
    ],
    0,
    "Muchos ensayos permiten suspender inmunoterapia tras 2 años de respuesta mantenida, vigilando recaídas.",
)

# Tumores sólidos - Sarcomas
add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Básico",
    "¿Cuál es el tratamiento principal del sarcoma de partes blandas localizado de extremidades?",
    [
        "Cirugía con márgenes amplios",
        "Quimioterapia exclusiva",
        "Radioterapia exclusiva",
        "Embolización",
    ],
    0,
    "La cirugía con márgenes adecuados es fundamental para el control local en sarcomas de extremidades.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Básico",
    "¿Qué prueba de imagen es esencial para estadificar sarcomas profundos de extremidad?",
    [
        "Resonancia magnética",
        "Ecografía",
        "Radiografía simple",
        "PET de cuerpo completo",
    ],
    0,
    "La resonancia magnética define extensión local y relación con estructuras neurovasculares.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Intermedio",
    "¿Qué fármaco es estándar en primera línea de sarcoma avanzado?",
    [
        "Doxorrubicina",
        "Imatinib",
        "Pazopanib",
        "Gemcitabina",
    ],
    0,
    "La doxorrubicina en monoterapia o combinada es el estándar inicial para la mayoría de sarcomas avanzados.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Intermedio",
    "¿Qué terapia dirigida es clave en tumores GIST con mutación KIT?",
    [
        "Imatinib",
        "Sorafenib",
        "Sunitinib",
        "Cediranib",
    ],
    0,
    "Imatinib bloquea KIT y es estándar en GIST avanzado o en adyuvancia en tumores de alto riesgo con mutación sensible.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Avanzado",
    "En GIST resistente a imatinib y sunitinib, ¿qué opción continúa la secuencia?",
    [
        "Regorafenib",
        "Pazopanib",
        "Lenvatinib",
        "Everolimus",
    ],
    0,
    "Regorafenib es el inhibidor multiquinasa aprobado tras fracaso de imatinib y sunitinib en GIST.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Básico",
    "¿Qué subtipo de sarcoma es radiosensible y se beneficia de radioterapia adyuvante?",
    [
        "Sarcoma mixoide de tejidos blandos",
        "Liposarcoma bien diferenciado",
        "Sarcoma epitelioide",
        "Fibrosarcoma",
    ],
    0,
    "El sarcoma mixoide responde bien a radioterapia, utilizada junto a cirugía para mejorar control local.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Intermedio",
    "En sarcoma sinovial, ¿qué fusión génica característica puede detectarse?",
    [
        "SS18-SSX",
        "EWSR1-FLI1",
        "ETV6-NTRK3",
        "ALK-EML4",
    ],
    0,
    "La fusión SS18-SSX es patognomónica de sarcoma sinovial y apoya el diagnóstico.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Avanzado",
    "¿Qué agente se emplea en liposarcoma mixoide metastásico tras antraciclinas?",
    [
        "Trabectedina",
        "Gemcitabina",
        "Temozolomida",
        "Capecitabina",
    ],
    0,
    "Trabectedina muestra actividad notable en liposarcoma mixoide y leiomiosarcoma tras antraciclinas.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Intermedio",
    "¿Qué síndrome familiar se asocia a leiomiosarcomas uterinos?",
    [
        "Síndrome de Lynch",
        "Neurofibromatosis tipo 1",
        "Von Hippel-Lindau",
        "MEN2",
    ],
    0,
    "El síndrome de Lynch incrementa riesgo de cánceres uterinos incluyendo leiomiosarcomas.",
)

add_question(
    "Tumores sólidos",
    "Sarcomas",
    "Avanzado",
    "¿Cuál es la principal vía de metástasis de osteosarcoma?",
    [
        "Pulmones",
        "Hígado",
        "Cerebro",
        "Huesos largos contralaterales",
    ],
    0,
    "El osteosarcoma metastatiza principalmente al pulmón, lo que condiciona el seguimiento con TAC torácico.",
)

# Hemato-oncología - Leucemias
add_question(
    "Hemato-oncología",
    "Leucemias",
    "Básico",
    "¿Qué alteración genética define la leucemia mieloide crónica?",
    [
        "Traslocación t(9;22) BCR-ABL",
        "Mutación JAK2 V617F",
        "Deleción 13q",
        "FLT3-ITD",
    ],
    0,
    "La presencia del cromosoma Filadelfia y la proteína de fusión BCR-ABL caracterizan la LMC.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Básico",
    "¿Qué tratamiento inicial se utiliza en leucemia linfática crónica sintomática con del17p?",
    [
        "Inhibidores de BTK (ibrutinib) o venetoclax",
        "Quimioinmunoterapia FCR",
        "Clorambucilo",
        "Interferón alfa",
    ],
    0,
    "Las deleciones 17p confieren resistencia a quimioterapia; se prefieren terapias dirigidas como ibrutinib o venetoclax.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Intermedio",
    "En leucemia aguda promielocítica, ¿qué combinación se emplea en primera línea?",
    [
        "Ácido transretinoico (ATRA) + trióxido de arsénico",
        "Antraciclinas + citarabina",
        "Imatinib",
        "Metotrexato",
    ],
    0,
    "ATRA junto con trióxido de arsénico ha reemplazado la quimioterapia intensiva en formas de riesgo bajo-intermedio.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Intermedio",
    "¿Qué mutación implica mal pronóstico en leucemia mieloide aguda normal cariotipo?",
    [
        "FLT3-ITD",
        "NPM1",
        "CEBPA bialélica",
        "IDH1",
    ],
    0,
    "La mutación FLT3-ITD confiere alto riesgo de recaída y se asocia a uso de inhibidores FLT3 y trasplante alogénico.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Avanzado",
    "¿Cuál es la indicación del trasplante alogénico en leucemia linfoblástica aguda del adulto?",
    [
        "Alto riesgo citogenético o respuesta subóptima",
        "Todos los pacientes en primera remisión",
        "Solo recaídas tardías",
        "Nunca se indica",
    ],
    0,
    "Los adultos con alto riesgo biológico o enfermedad residual mínima positiva suelen beneficiarse de trasplante alogénico en primera remisión.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Básico",
    "¿Qué signo clínico clásico sugiere leucemia aguda?",
    [
        "Pancitopenia con síndrome constitucional",
        "Hiperglucemia",
        "Hipertensión",
        "Aumento de ferritina",
    ],
    0,
    "La leucemia aguda suele debutar con pancitopenia, fiebre, infecciones y hemorragias por fallo de médula ósea.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Intermedio",
    "¿Qué terapia dirigida se usa en LMC resistente a imatinib con mutación T315I?",
    [
        "Ponatinib",
        "Nilotinib",
        "Dasatinib",
        "Bosutinib",
    ],
    0,
    "Ponatinib es activo frente a la mutación T315I, responsable de resistencia a otros ITK.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Avanzado",
    "¿Qué estrategia reduce síndrome de lisis tumoral al iniciar venetoclax?",
    [
        "Escalado gradual de dosis y profilaxis intensiva",
        "Inicio a dosis alta",
        "Suspender hidratación",
        "Añadir interleucina-2",
    ],
    0,
    "El escalado paulatino con hidratación y alopurinol previene síndrome de lisis tumoral con venetoclax.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Intermedio",
    "¿Qué marcador de enfermedad residual mínima se usa en LLA B?",
    [
        "Citometría de flujo multiparamétrica",
        "PCR de BCR-ABL",
        "Electroforesis de proteínas",
        "Test de Coombs",
    ],
    0,
    "La evaluación de enfermedad residual minima mediante citometría o PCR específica orienta el pronóstico y tratamiento en LLA.",
)

add_question(
    "Hemato-oncología",
    "Leucemias",
    "Avanzado",
    "¿Qué terapia celular se recomienda en LLA B refractaria?",
    [
        "CAR-T anti-CD19",
        "Trasplante autólogo",
        "Lenalidomida",
        "Bortezomib",
    ],
    0,
    "Las terapias CAR-T contra CD19 logran respuestas profundas en LLA B refractaria o en recaída.",
)

# Hemato-oncología - Linfomas
add_question(
    "Hemato-oncología",
    "Linfomas",
    "Básico",
    "¿Cuál es el esquema estándar de primera línea en linfoma difuso de células B grandes?",
    [
        "R-CHOP",
        "ABVD",
        "Bendamustina-rituximab",
        "HyperCVAD",
    ],
    0,
    "R-CHOP (rituximab, ciclofosfamida, doxorrubicina, vincristina y prednisona) es el tratamiento estándar inicial.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Básico",
    "¿Qué terapia se utiliza en linfoma de Hodgkin clásico en estadios avanzados?",
    [
        "ABVD",
        "BEACOPP",
        "CHOP",
        "ICE",
    ],
    0,
    "El esquema ABVD es estándar en estadios avanzados de linfoma de Hodgkin, con posible escalado según respuesta.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Intermedio",
    "¿Qué anticuerpo biespecífico se usa en linfoma B replanteado tras múltiples líneas?",
    [
        "Glofitamab",
        "Alemtuzumab",
        "Belantamab",
        "Daratumumab",
    ],
    0,
    "Glofitamab es un anticuerpo biespecífico CD20xCD3 aprobado para linfoma B en recaída refractaria.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Intermedio",
    "En linfoma folicular grado 1-2 sintomático, ¿qué combinación se emplea en primera línea?",
    [
        "Rituximab + bendamustina",
        "Lenalidomida",
        "Fludarabina",
        "Cladribina",
    ],
    0,
    "Rituximab con bendamustina ofrece altas tasas de respuesta y buena tolerancia en linfoma folicular.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Avanzado",
    "¿Qué papel tiene CAR-T en linfoma difuso B en segunda línea?",
    [
        "Indicado en recaída temprana tras R-CHOP",
        "Solo tercera línea",
        "Contraindicado",
        "Solo en recaídas tardías",
    ],
    0,
    "Tras recaída temprana o refractariedad a R-CHOP, CAR-T dirigidos a CD19 han demostrado superioridad frente a quimio-rescate.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Básico",
    "¿Qué marcador de proliferación se usa para diferenciar linfoma indolente de agresivo?",
    [
        "Ki-67",
        "CD30",
        "CD23",
        "Cyclin D1",
    ],
    0,
    "El índice Ki-67 elevado sugiere comportamiento agresivo y ayuda a categorizar linfomas.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Intermedio",
    "¿Qué factor pronóstico se incluye en el IPI?",
    [
        "Edad >60 años",
        "Nivel normal de LDH",
        "Sexo",
        "Antecedente familiar",
    ],
    0,
    "El International Prognostic Index valora edad, LDH, ECOG, estadio y número de sitios extranodales.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Avanzado",
    "En linfoma de Hodgkin refractario, ¿qué nuevo anticuerpo-drug conjugate se usa?",
    [
        "Brentuximab vedotina",
        "Trastuzumab deruxtecan",
        "Sacituzumab govitecan",
        "Belantamab mafodotin",
    ],
    0,
    "Brentuximab vedotina dirigido a CD30 es eficaz tras recaída post-trasplante autólogo o en segunda línea.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Intermedio",
    "¿Qué patología viral está ligada a linfoma de Burkitt endémico?",
    [
        "Virus de Epstein-Barr",
        "Virus de la hepatitis C",
        "HTLV-1",
        "VPH",
    ],
    0,
    "El linfoma de Burkitt endémico se asocia estrechamente con infección por EBV.",
)

add_question(
    "Hemato-oncología",
    "Linfomas",
    "Avanzado",
    "¿Qué terapia se considera en linfoma T periférico recaído?",
    [
        "Trasplante autólogo o alogénico",
        "Imatinib",
        "Lenalidomida",
        "Bevacizumab",
    ],
    0,
    "Los linfomas T periféricos tienen mal pronóstico y se candidatan a trasplante tras respuesta.",
)

# Hemato-oncología - Mieloma
add_question(
    "Hemato-oncología",
    "Mieloma",
    "Básico",
    "¿Qué criterio define mieloma múltiple sintomático?",
    [
        "Lesiones CRAB o biomarcadores específicos",
        "Proteinuria de Bence Jones aislada",
        "Presencia de MGUS",
        "Osteopenia leve",
    ],
    0,
    "El mieloma sintomático requiere daño orgánico (hipercalcemia, insuficiencia renal, anemia, lesiones óseas) o biomarcadores como ≥60% plasmocitos medulares.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Básico",
    "¿Cuál es el tratamiento de inducción estándar en pacientes candidatos a trasplante autólogo?",
    [
        "Bortezomib + lenalidomida + dexametasona (VRd)",
        "Melphalan oral",
        "Lenalidomida en monoterapia",
        "Clorambucilo",
    ],
    0,
    "VRd es la combinación más utilizada previa a la aféresis para trasplante autólogo.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Intermedio",
    "¿Qué estudio se realiza para evaluar citogenética de alto riesgo en mieloma?",
    [
        "FISH para t(4;14), t(14;16), del17p",
        "Cariotipo convencional",
        "Secuenciación de panel de exoma",
        "PCR cuantitativa",
    ],
    0,
    "Las alteraciones de alto riesgo se identifican mediante FISH en plasmocitos enriquecidos.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Intermedio",
    "¿Qué agente anti-CD38 se añade a regímenes de primera línea en pacientes no candidatos a trasplante?",
    [
        "Daratumumab",
        "Elotuzumab",
        "Belantamab",
        "Inotuzumab",
    ],
    0,
    "Daratumumab combinado con lenalidomida-dexametasona o VMP mejora la supervivencia en pacientes ineligibles a trasplante.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Avanzado",
    "¿Qué terapia celular emergente se usa en mieloma refractario triple clase?",
    [
        "CAR-T anti-BCMA",
        "Trasplante autólogo repetido",
        "Interferón",
        "Lenalidomida",
    ],
    0,
    "Las terapias CAR-T dirigidas a BCMA han mostrado respuestas profundas en mieloma refractario a múltiples líneas.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Básico",
    "¿Qué prueba de imagen se recomienda inicial para detectar lesiones óseas?",
    [
        "Tomografía de cuerpo entero de baja dosis",
        "Radiografía simple",
        "PET-FDG",
        "Gammagrafía ósea",
    ],
    0,
    "Las guías recomiendan TAC de cuerpo entero de baja dosis o PET-TC para detectar lesiones líticas con mayor sensibilidad.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Intermedio",
    "¿Qué profilaxis se debe administrar en pacientes tratados con lenalidomida?",
    [
        "Tromboprofilaxis (aspirina o anticoagulación)",
        "Vacuna antineumocócica",
        "Calcio y vitamina D",
        "Fluconazol",
    ],
    0,
    "Lenalidomida aumenta riesgo trombótico; se requiere profilaxis según factores de riesgo.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Avanzado",
    "¿Qué combina teclistamab en mieloma refractario?",
    [
        "Anticuerpo biespecífico BCMAxCD3",
        "Inhibidor de proteasoma",
        "Agente alquilante",
        "Radiofármaco",
    ],
    0,
    "Teclistamab es un anticuerpo biespecífico que acerca linfocitos T a células plasmáticas expresando BCMA.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Intermedio",
    "¿Qué define la respuesta completa estricta según IMWG?",
    [
        "Inmunofijación negativa y <5% plasmocitos",
        "Desaparición de síntomas",
        "Reducción de M-proteína 50%",
        "Hemoglobina normal",
    ],
    0,
    "La respuesta completa estricta exige inmunofijación negativa en suero/orina, <5% plasmocitos y cadenas ligeras libres normalizadas.",
)

add_question(
    "Hemato-oncología",
    "Mieloma",
    "Avanzado",
    "¿Qué agente reduce riesgo de eventos óseos en mieloma?",
    [
        "Ácido zoledrónico",
        "Prednisona",
        "Carfilzomib",
        "G-CSF",
    ],
    0,
    "Los bisfosfonatos como ácido zoledrónico disminuyen eventos óseos y dolor en mieloma.",
)

# Cuidados de soporte - Antiemesis
add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Básico",
    "¿Qué esquema se recomienda en quimioterapia altamente emetógena como cisplatino?",
    [
        "Antagonista 5-HT3 + dexametasona + antagonista NK1",
        "Metoclopramida",
        "Ondansetrón solo",
        "Lorazepam en monoterapia",
    ],
    0,
    "Las pautas de alto riesgo requieren triple terapia combinando antagonista 5-HT3, dexametasona y antagonista NK1.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Básico",
    "¿Qué antiemético se añade para prevenir náuseas anticipatorias?",
    [
        "Benzodiacepinas",
        "Haloperidol",
        "Octreótido",
        "Escopolamina",
    ],
    0,
    "Las benzodiacepinas como lorazepam ayudan a reducir las náuseas anticipatorias asociadas a quimioterapia.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Intermedio",
    "¿Qué fármaco se incluye para prevenir emesis tardía en cisplatino?",
    [
        "Antagonista NK1",
        "Metoclopramida",
        "Dimenhidrinato",
        "Difenhidramina",
    ],
    0,
    "Los antagonistas de NK1 (aprepitant, fosaprepitant) reducen náuseas tardías inducidas por quimioterapia altamente emetógena.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Intermedio",
    "¿Qué diferencia existe entre ondasetrón y palonosetrón?",
    [
        "Palonosetrón tiene vida media más larga y cubre fase tardía",
        "Ondasetrón cruza mejor barrera hematoencefálica",
        "Palonosetrón solo bloquea NK1",
        "No hay diferencias",
    ],
    0,
    "Palonosetrón presenta mayor afinidad y vida media prolongada, útil para fase aguda y tardía de emesis.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Avanzado",
    "En pacientes con doble profilaxis estándar que siguen con náuseas, ¿qué fármaco puede añadirse?",
    [
        "Olanzapina",
        "Hioscina",
        "Domperidona",
        "Naproxeno",
    ],
    0,
    "Olanzapina se asocia a reducción adicional de náuseas refractarias cuando se añade a esquemas estándar.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Básico",
    "¿Qué profilaxis se usa en quimioterapia de bajo riesgo emético?",
    [
        "Dexametasona u ondansetrón según sea necesario",
        "Triple terapia",
        "Aprepitant",
        "Ningún tratamiento",
    ],
    0,
    "En bajo riesgo se emplea un solo agente, generalmente dexametasona o un antagonista 5-HT3 previo.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Intermedio",
    "¿Qué antiemesis se recomienda en quimioterapia oral moderadamente emetógena?",
    [
        "Profilaxis diaria con antagonista 5-HT3",
        "Ondasetrón IV",
        "Metoclopramida cada 8 horas",
        "No precisa profilaxis",
    ],
    0,
    "Las guías sugieren antagonista 5-HT3 oral diario durante el período de administración para quimioterapia oral emetógena moderada.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Avanzado",
    "¿Qué estrategia se utiliza en pacientes con retraso de la motilidad gástrica?",
    [
        "Añadir proquinéticos como metoclopramida",
        "Suspender antieméticos",
        "Utilizar corticoides en solitario",
        "Administrar antiácidos",
    ],
    0,
    "Los proquinéticos mejoran el vaciamiento gástrico y se combinan con antieméticos estándar en pacientes con gastroparesia.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Intermedio",
    "¿Qué diferencia hay entre emesis aguda y tardía?",
    [
        "La aguda ocurre <24h y la tardía >24h postquimioterapia",
        "La aguda ocurre a los 3 días",
        "La tardía es previa al tratamiento",
        "No existe diferencia",
    ],
    0,
    "La emesis aguda se presenta dentro de las primeras 24 horas, mientras que la tardía aparece posteriormente.",
)

add_question(
    "Cuidados de soporte",
    "Antiemesis",
    "Avanzado",
    "¿Cómo se manejan las náuseas en quimioterapia multiday altamente emetógena?",
    [
        "Antagonista 5-HT3 diario + dexametasona + NK1",
        "Ondasetrón único el día 1",
        "Metoclopramida eventual",
        "Solo benzodiacepinas",
    ],
    0,
    "Se extrapolan esquemas de alto riesgo ajustando dosis diarias de antagonista 5-HT3 y dexametasona con NK1 durante el ciclo.",
)

# Cuidados de soporte - Infecciones
add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Básico",
    "¿Qué profilaxis antimicrobiana se recomienda en neutropenia febril de alto riesgo?",
    [
        "Antibióticos de amplio espectro empíricos",
        "Penicilina oral",
        "Antivirales",
        "Ninguna",
    ],
    0,
    "La neutropenia febril de alto riesgo requiere iniciar antibióticos de amplio espectro dentro de la primera hora.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Básico",
    "¿Qué medida previene neumonía por Pneumocystis jirovecii en tumores sólidos con altas dosis de corticoides?",
    [
        "Profilaxis con trimetoprim-sulfametoxazol",
        "Profilaxis con azitromicina",
        "Vacuna antigripal",
        "Uso de probióticos",
    ],
    0,
    "La profilaxis con cotrimoxazol previene neumonía por Pneumocystis en pacientes inmunosuprimidos.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Intermedio",
    "¿Cuándo administrar G-CSF profiláctico primario?",
    [
        "Cuando el riesgo de neutropenia febril es ≥20%",
        "En todo ciclo",
        "Solo en neutropenia crónica",
        "Nunca en tumores sólidos",
    ],
    0,
    "Las guías recomiendan G-CSF primario si la quimioterapia conlleva riesgo ≥20% o hay factores adicionales.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Intermedio",
    "¿Qué vacunación anual se aconseja en pacientes oncológicos?",
    [
        "Vacuna antigripal inactivada",
        "BCG",
        "Varicela viva",
        "Fiebre amarilla",
    ],
    0,
    "Se recomienda vacunación antigripal con preparado inactivado cada temporada para reducir complicaciones.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Avanzado",
    "¿Qué pauta antiviral se utiliza en trasplante autólogo para prevenir reactivación de herpes?",
    [
        "Aciclovir",
        "Oseltamivir",
        "Ribavirina",
        "Remdesivir",
    ],
    0,
    "La profilaxis con aciclovir o valaciclovir previene reactivaciones herpéticas tras trasplante autólogo.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Básico",
    "¿Qué definición describe la sepsis en neutropenia febril?",
    [
        "Disfunción orgánica con infección probable",
        "Temperatura >39ºC",
        "Bacteriemia",
        "Neutrófilos >500",
    ],
    0,
    "La sepsis implica infección sospechada con disfunción orgánica; requiere manejo urgente siguiendo criterios SOFA/qSOFA.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Intermedio",
    "¿Qué prueba se realiza ante fiebre persistente en neutropenia pese a antibióticos?",
    [
        "TAC de tórax y senos paranasales",
        "Radiografía simple",
        "Colonoscopia",
        "Eco abdominal",
    ],
    0,
    "Un TAC de tórax y senos ayuda a detectar infecciones fúngicas o sinusales ocultas en neutropenia prolongada.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Avanzado",
    "¿Qué marcador orienta a infección fúngica invasora en neutropenia prolongada?",
    [
        "Galactomanano sérico",
        "Procalcitonina",
        "Ferritina",
        "Lactato",
    ],
    0,
    "El galactomanano es útil para detectar aspergilosis invasora, especialmente en pacientes con neutropenia prolongada.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Intermedio",
    "¿Qué medida reduce el riesgo de infección en pacientes con catéter venoso central?",
    [
        "Curar con técnica estéril y cambiar apósitos regularmente",
        "Uso rutinario de antibióticos",
        "Lavado con agua",
        "No tocar el catéter",
    ],
    0,
    "La asepsia estricta y el cuidado adecuado del catéter disminuyen la incidencia de infecciones relacionadas.",
)

add_question(
    "Cuidados de soporte",
    "Infecciones",
    "Avanzado",
    "¿Cuándo suspender profilaxis con fluoroquinolonas en neutropenia?",
    [
        "Tras recuperación de neutrófilos >500/µL sostenida",
        "Al cuarta dosis",
        "Si la fiebre persiste",
        "Nunca",
    ],
    0,
    "La profilaxis se mantiene hasta recuperar neutrófilos >500/µL de forma sostenida o finalizar el episodio de riesgo.",
)

# Cuidados paliativos - Dolor
add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Básico",
    "Según la escalera analgésica de la OMS, ¿qué se recomienda tras fracaso de opioides débiles?",
    [
        "Escalar a opioides mayores",
        "Añadir benzodiacepinas",
        "Suspender analgesia",
        "Usar AINE exclusivamente",
    ],
    0,
    "La escalera analgésica propone escalar a opioides potentes cuando los débiles no controlan el dolor moderado-severo.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Básico",
    "¿Qué adyuvante es útil en dolor neuropático oncológico?",
    [
        "Gabapentinoides",
        "Ibuprofeno",
        "Clorpromazina",
        "Antibióticos",
    ],
    0,
    "Los gabapentinoides (gabapentina, pregabalina) son eficaces en dolor neuropático como adyuvantes de opioides.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Intermedio",
    "¿Qué opioide es preferente en insuficiencia renal avanzada?",
    [
        "Fentanilo transdérmico",
        "Morfina",
        "Codeína",
        "Tramadol",
    ],
    0,
    "Fentanilo y buprenorfina tienen menos metabolitos activos renales y son preferibles en insuficiencia renal.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Intermedio",
    "¿Qué recomendación se hace al iniciar opioides de liberación prolongada?",
    [
        "Mantener rescates con opioide de acción rápida",
        "Suspender laxantes",
        "Evitar rescates",
        "Administrar solo por la noche",
    ],
    0,
    "Se deben mantener rescates para dolor irruptivo y ajustar la dosis diaria según consumo adicional.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Avanzado",
    "¿Qué técnica intervencionista se usa en dolor refractario por cáncer pancreático?",
    [
        "Bloqueo del plexo celíaco",
        "Radiofrecuencia facetaria",
        "Infiltración subacromial",
        "Electroestimulación medular",
    ],
    0,
    "El bloqueo del plexo celíaco con alcohol o fenol reduce el dolor visceral del cáncer pancreático avanzado.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Básico",
    "¿Qué efecto adverso es frecuente con opioides y precisa profilaxis?",
    [
        "Estreñimiento",
        "Hipertensión",
        "Dermatitis",
        "Hiperglucemia",
    ],
    0,
    "El estreñimiento es común y debe prevenirse con laxantes estimulantes/osmóticos desde el inicio.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Intermedio",
    "¿Cómo se calcula la dosis de rescate de opioide?",
    [
        "10-15% de la dosis total diaria",
        "50% de la dosis diaria",
        "Igual a dosis basal",
        "No se calcula",
    ],
    0,
    "Se recomienda rescate equivalente al 10-15% de la dosis diaria total de opioides.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Avanzado",
    "¿Qué manejo se recomienda ante hiperalgesia inducida por opioides?",
    [
        "Rotación de opioides y reducción de dosis",
        "Aumentar la dosis",
        "Suspender analgésicos",
        "Añadir benzodiacepinas",
    ],
    0,
    "La rotación hacia un opioide distinto y ajustar dosis ayuda a revertir la hiperalgesia inducida.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Intermedio",
    "¿Qué escala evalúa dolor irruptivo?",
    [
        "Escala BPI (Brief Pain Inventory)",
        "ECOG",
        "NPI",
        "Charlson",
    ],
    0,
    "El Brief Pain Inventory permite valorar intensidad, duración y repercusión del dolor irruptivo.",
)

add_question(
    "Cuidados paliativos",
    "Control del dolor",
    "Avanzado",
    "¿Qué tratamiento se usa en dolor óseo metastásico focal?",
    [
        "Radioterapia paliativa",
        "Quimioterapia",
        "Gabapentina",
        "Hipnosis",
    ],
    0,
    "La radioterapia paliativa proporciona alivio rápido y duradero del dolor óseo localizado.",
)

# Cuidados paliativos - Síntomas respiratorios
add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Básico",
    "¿Cuál es el fármaco de elección para disnea refractaria en cáncer avanzado?",
    [
        "Morfina",
        "Bromuro de ipratropio",
        "Diazepam",
        "Prednisona",
    ],
    0,
    "Los opioides sistémicos como morfina reducen la sensación de disnea en situaciones refractarias.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Básico",
    "¿Qué medida ambiental ayuda a aliviar disnea?",
    [
        "Ventilador dirigido al rostro",
        "Habitación caliente",
        "Silencio absoluto",
        "Luz intensa",
    ],
    0,
    "El flujo de aire en la cara mediante ventilador produce sensación de alivio en algunos pacientes.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Intermedio",
    "¿Qué manejo se recomienda en congestión bronquial terminal?",
    [
        "Anticolinérgicos como butilbromuro de hioscina",
        "Antibióticos IV",
        "Broncodilatadores",
        "Heparina",
    ],
    0,
    "Los anticolinérgicos reducen secreciones y el ruido respiratorio terminal.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Intermedio",
    "¿Qué intervención no farmacológica mejora ansiedad asociada a disnea?",
    [
        "Técnicas de respiración y relajación",
        "Restricción hídrica",
        "Sedación inmediata",
        "Aumento de oxígeno al máximo",
    ],
    0,
    "Entrenar respiración diafragmática, relajación y apoyo psicológico reduce la ansiedad ligada a disnea.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Avanzado",
    "¿Cuándo está indicada la sedación paliativa por disnea?",
    [
        "Cuando persiste disnea refractaria pese a tratamientos óptimos",
        "Al inicio del síntoma",
        "Solo con hipoxemia",
        "Nunca",
    ],
    0,
    "La sedación paliativa se considera en disnea refractaria que no responde a intervenciones farmacológicas y no farmacológicas.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Básico",
    "¿Qué papel tiene el oxígeno en disnea sin hipoxemia?",
    [
        "Beneficio limitado; se reserva para hipoxemia documentada",
        "Es imprescindible",
        "Está contraindicado",
        "Sustituye a opioides",
    ],
    0,
    "El oxígeno solo se recomienda cuando hay hipoxemia; en normoxemia puede no aportar mejora.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Intermedio",
    "¿Qué combinación farmacológica se usa en crisis de disnea con ansiedad intensa?",
    [
        "Opioide + benzodiacepina",
        "Corticoide + antibiótico",
        "Diurético + betabloqueante",
        "Anticolinérgico + heparina",
    ],
    0,
    "La asociación de opioide para disnea y benzodiacepina para ansiedad es eficaz en crisis agudas.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Avanzado",
    "¿Qué considerar en derrame pleural masivo sintomático en paciente paliativo?",
    [
        "Drenaje paliativo o pleurodesis",
        "Suspender opioides",
        "Solo diuréticos",
        "Reposo absoluto",
    ],
    0,
    "El drenaje mediante toracocentesis o catéter de túnel alivia disnea por derrame pleural maligno.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Intermedio",
    "¿Qué define disnea refractaria?",
    [
        "Persistencia del síntoma pese a terapia óptima",
        "Disnea nocturna",
        "Disnea al esfuerzo leve",
        "Sensación subjetiva de falta de aire",
    ],
    0,
    "Se considera refractaria cuando no responde a tratamientos dirigidos causa y medidas sintomáticas aceptables.",
)

add_question(
    "Cuidados paliativos",
    "Síntomas respiratorios",
    "Avanzado",
    "¿Qué evaluación se utiliza para monitorizar disnea?",
    [
        "Escala numérica 0-10",
        "Escala de Karnofsky",
        "Mini-Mental",
        "APGAR",
    ],
    0,
    "Las escalas numéricas permiten cuantificar intensidad y evaluar respuesta terapéutica en disnea.",
)

# Oncología radioterápica - Planeación
add_question(
    "Oncología radioterápica",
    "Planeación",
    "Básico",
    "¿Qué significa IMRT en radioterapia moderna?",
    [
        "Radioterapia de intensidad modulada",
        "Radioterapia intraoperatoria",
        "Radioterapia metabólica",
        "Radioterapia microfocal",
    ],
    0,
    "IMRT permite modular la intensidad de los haces para conformar la dosis al volumen tumoral y reducir toxicidad.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Básico",
    "¿Qué prueba de imagen es esencial para la planificación de radioterapia externa?",
    [
        "Tomografía computarizada de simulación",
        "Radiografía de tórax",
        "Resonancia cardíaca",
        "Ecografía",
    ],
    0,
    "La TAC de simulación permite definir contornos anatómicos y asignar densidades electrónicas para la planificación.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Intermedio",
    "¿Qué volumen incluye márgenes para el movimiento del tumor causado por la respiración?",
    [
        "ITV (Internal Target Volume)",
        "GTV",
        "CTV",
        "PTV",
    ],
    0,
    "El ITV incorpora el movimiento interno del tumor, especialmente en órganos móviles como pulmón o hígado.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Intermedio",
    "¿Qué técnica reduce el volumen pulmonar irradiado en cáncer de mama izquierdo?",
    [
        "Inspiración profunda mantenida",
        "Prono",
        "Aumento de energía",
        "Uso de bolus",
    ],
    0,
    "La inspiración profunda mantenida separa corazón y pulmón del campo y reduce dosis en mama izquierda.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Avanzado",
    "¿Qué tecnología permite administrar dosis ablativas en lesiones pequeñas?",
    [
        "Radioterapia estereotáxica (SBRT/SRS)",
        "Radioterapia 2D",
        "Brachiterapia",
        "Radioterapia de haz de electrones",
    ],
    0,
    "La radioterapia estereotáxica entrega altas dosis con gran precisión en pocos fraccionamientos.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Básico",
    "¿Qué parámetro dosimétrico se usa para evaluar cobertura del PTV?",
    [
        "D95 (dosis al 95% del volumen)",
        "SUV",
        "LDH",
        "PSA",
    ],
    0,
    "D95 indica la dosis recibida por el 95% del PTV, asegurando cobertura suficiente.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Intermedio",
    "¿Qué herramienta se usa para verificación diaria de posición?",
    [
        "Imagen guiada (IGRT) con cone-beam CT",
        "Tomografía PET",
        "Gammagrafía",
        "Fluoroscopia digestiva",
    ],
    0,
    "La IGRT mediante cone-beam CT permite ajustar la posición del paciente antes de cada sesión.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Avanzado",
    "¿Qué concepto describe la dosis media restringida en órganos de riesgo?",
    [
        "Constraint dosimétrico",
        "Boost",
        "Fraccionamiento",
        "Bolus",
    ],
    0,
    "Los constraints dosimétricos fijan límites de dosis en órganos críticos para evitar toxicidades.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Intermedio",
    "¿Qué ventaja aporta la protonterapia?",
    [
        "Depósito de dosis con pico de Bragg y menor salida",
        "Mayor dispersión",
        "Menor coste",
        "No requiere planificación",
    ],
    0,
    "La protonterapia aprovecha el pico de Bragg para reducir dosis a tejidos distales, útil en pediatría y tumores cercanos a órganos críticos.",
)

add_question(
    "Oncología radioterápica",
    "Planeación",
    "Avanzado",
    "¿Qué algoritmo de planificación es preferible en SBRT pulmonar?",
    [
        "Acuñamiento anisotrópico (AAA) o Monte Carlo",
        "Pencil beam sencillo",
        "Algoritmo 2D",
        "Ray tracing básico",
    ],
    0,
    "Algoritmos avanzados como Monte Carlo modelan heterogeneidades pulmonares con precisión en SBRT.",
)

# Oncología radioterápica - Toxicidades
add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Básico",
    "¿Qué toxicidad aguda es típica en radioterapia de cabeza y cuello?",
    [
        "Mucositis",
        "Nefrotoxicidad",
        "Cardiotoxicidad",
        "Neuropatía óptica",
    ],
    0,
    "La mucositis orofaríngea es una toxicidad aguda frecuente y se maneja con cuidados de soporte intensivos.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Básico",
    "¿Qué órgano limita la radioterapia en cáncer de pulmón?",
    [
        "Pulmón sano (neumonitis rádica)",
        "Riñón",
        "Bazo",
        "Tiroides",
    ],
    0,
    "La neumonitis por radiación es un riesgo clave, se limita la dosis pulmonar media y V20.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Intermedio",
    "¿Qué medida previene xerostomía en radioterapia de cabeza y cuello?",
    [
        "Parotid sparing con IMRT",
        "Aumentar la dosis",
        "Usar electrones",
        "Deshidratar",
    ],
    0,
    "La IMRT permite limitar la dosis a las glándulas parótidas, reduciendo la xerostomía crónica.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Intermedio",
    "¿Qué toxicidad tardía preocupa en radioterapia mamaria izquierda?",
    [
        "Cardiotoxicidad",
        "Hipotiroidismo",
        "Neuropatía periférica",
        "Retinopatía",
    ],
    0,
    "La dosis al corazón se relaciona con riesgo de eventos cardiovasculares a largo plazo.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Avanzado",
    "¿Qué toxicidad se monitoriza tras irradiación hepática?",
    [
        "Enfermedad venooclusiva (síndrome de Budd-Chiari rádico)",
        "Osteorradionecrosis",
        "Mielosupresión severa",
        "Hipercalcemia",
    ],
    0,
    "La enfermedad venooclusiva hepática es una complicación potencial tras altas dosis al hígado.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Básico",
    "¿Qué grado de toxicidad cutánea corresponde a eritema leve?",
    [
        "Grado 1",
        "Grado 2",
        "Grado 3",
        "Grado 4",
    ],
    0,
    "El eritema leve sin descamación corresponde a toxicidad cutánea grado 1.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Intermedio",
    "¿Qué fármaco protege contra cistitis rádica en próstata?",
    [
        "Amifostina (uso limitado)",
        "Mesna",
        "Ondansetrón",
        "Dexametasona",
    ],
    0,
    "La amifostina se ha estudiado como radioprotector, aunque su uso es limitado por efectos secundarios.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Avanzado",
    "¿Qué complicación tardía aparece tras irradiación medular?",
    [
        "Mielopatía rádica",
        "Neuropatía óptica",
        "Síndrome nefrótico",
        "Hipertiroidismo",
    ],
    0,
    "Dosis elevadas a la médula espinal pueden producir mielopatía rádica irreversible; se limita la dosis máxima.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Intermedio",
    "¿Qué parámetros se controlan para evitar toxicidad intestinal en irradiación pélvica?",
    [
        "Volumen intestinal (V45/V50)",
        "Dosis al corazón",
        "SUV",
        "LDH",
    ],
    0,
    "Se limitan los volúmenes intestinales que reciben dosis >45-50 Gy para reducir enteritis crónica.",
)

add_question(
    "Oncología radioterápica",
    "Toxicidades",
    "Avanzado",
    "¿Qué tratamiento se emplea para osteorradionecrosis mandibular?",
    [
        "Oxígeno hiperbárico y cirugía",
        "Quimioterapia",
        "Anticoagulación",
        "Vitamina C",
    ],
    0,
    "El manejo combina medidas conservadoras, antibióticos, oxígeno hiperbárico y, si es necesario, resección quirúrgica.",
)

# Genética y biología tumoral - Biomarcadores
add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Básico",
    "¿Qué biomarcador se evalúa para indicar trastuzumab en cáncer de mama?",
    [
        "HER2 por inmunohistoquímica o FISH",
        "PD-L1",
        "EGFR",
        "KRAS",
    ],
    0,
    "La sobreexpresión o amplificación de HER2 determina la indicación de terapias anti-HER2.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Básico",
    "¿Qué biomarcador orienta el uso de inhibidores de PARP en ovario?",
    [
        "Mutaciones BRCA1/2",
        "KRAS",
        "ALK",
        "ROS1",
    ],
    0,
    "Las mutaciones BRCA y otras alteraciones de recombinación homóloga identifican candidatas a PARP.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Intermedio",
    "¿Qué prueba detecta inestabilidad de microsatélites?",
    [
        "PCR/MSI o inmunohistoquímica de MMR",
        "Secuenciación germinal",
        "Citometría",
        "FISH",
    ],
    0,
    "La MSI se evalúa mediante PCR de microsatélites o pérdida de expresión de proteínas MMR por inmunohistoquímica.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Intermedio",
    "¿Qué biomarcador define sensibilidad a EGFR-TKIs en cáncer de pulmón?",
    [
        "Mutaciones activadoras de EGFR",
        "Amplificación de MET",
        "PD-L1",
        "HER2",
    ],
    0,
    "Las mutaciones en exones 19 y 21 de EGFR predicen respuesta a inhibidores tirosina cinasa.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Avanzado",
    "¿Qué biomarcador tumoral se emplea para terapia tisotumab vedotina en cérvix?",
    [
        "Tissue factor",
        "HER2",
        "NTRK",
        "RET",
    ],
    0,
    "Tisotumab vedotina se dirige al factor tisular expresado en cáncer de cérvix recurrente.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Básico",
    "¿Qué determina candidatas a inmunoterapia en cáncer endometrial?",
    [
        "MSI-H/dMMR",
        "CA-125 elevado",
        "CEA",
        "PSA",
    ],
    0,
    "La inestabilidad de microsatélites o deficiencia MMR predicen respuesta a inhibidores de PD-1 en endometrio.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Intermedio",
    "¿Qué biomarcador indica terapia con entrectinib?",
    [
        "Fusiones NTRK",
        "KRAS G12C",
        "BRAF V600",
        "PD-L1",
    ],
    0,
    "Entrectinib está aprobado para tumores con fusiones NTRK independientemente del origen.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Avanzado",
    "¿Qué biomarcador se usa para seleccionar sotorasib?",
    [
        "KRAS G12C",
        "NRAS",
        "ALK",
        "PIK3CA",
    ],
    0,
    "Sotorasib bloquea KRAS G12C y está indicado en cáncer de pulmón con esta mutación.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Intermedio",
    "¿Qué análisis se emplea para alteraciones complejas (TMB, firmas)?",
    [
        "Secuenciación de nueva generación",
        "PCR convencional",
        "Sanger",
        "Citometría",
    ],
    0,
    "La NGS permite evaluar múltiples genes, carga mutacional tumoral (TMB) y firmas genómicas.",
)

add_question(
    "Genética y biología tumoral",
    "Biomarcadores",
    "Avanzado",
    "¿Qué biomarcador emergente predice respuesta a inmunoterapia en melanoma?",
    [
        "TMB elevada",
        "HER2",
        "IDH1",
        "VEGFA",
    ],
    0,
    "Una carga mutacional elevada se asocia a mayor probabilidad de respuesta a inhibidores de checkpoint.",
)

# Genética y biología tumoral - Terapias dirigidas
add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Básico",
    "¿Qué mecanismo de acción tiene imatinib en GIST?",
    [
        "Inhibidor de tirosina cinasa KIT/PDGFRA",
        "Anticuerpo anti-HER2",
        "Inhibidor de MEK",
        "Antagonista NK1",
    ],
    0,
    "Imatinib bloquea la activación de KIT y PDGFRA, controlando la proliferación en GIST con mutaciones sensibles.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Básico",
    "¿Qué terapia dirigida se usa en cáncer renal metastásico?",
    [
        "Inhibidores de VEGFR (sunitinib, pazopanib)",
        "Inhibidores EGFR",
        "Anti-CD20",
        "Aromatasa",
    ],
    0,
    "Los inhibidores de VEGFR bloquean angiogénesis y son estándar en carcinoma renal avanzado.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Intermedio",
    "¿Qué combinación se usa en cáncer colorrectal BRAF V600E?",
    [
        "Encorafenib + cetuximab",
        "Trametinib + pembrolizumab",
        "Osimertinib",
        "Lenvatinib + everolimus",
    ],
    0,
    "La combinación de inhibidores BRAF con anti-EGFR mejora supervivencia en CCR BRAF mutado.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Intermedio",
    "¿Qué terapia dirigida se usa en cáncer de mama con mutación PIK3CA?",
    [
        "Alpelisib + fulvestrant",
        "Everolimus",
        "Trastuzumab",
        "Tucatinib",
    ],
    0,
    "Alpelisib combinado con fulvestrant mejora resultados en tumores HR+ con mutación PIK3CA.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Avanzado",
    "¿Qué fármaco bloquea mutaciones RET en cáncer de tiroides y pulmón?",
    [
        "Selpercatinib",
        "Trastuzumab",
        "Larotrectinib",
        "Crizotinib",
    ],
    0,
    "Selpercatinib es un inhibidor altamente selectivo de RET aprobado en tumores con fusiones o mutaciones RET.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Básico",
    "¿Qué define la resistencia secundaria a EGFR-TKIs de primera generación?",
    [
        "Mutación T790M",
        "Amplificación HER2",
        "Pérdida de PTEN",
        "Mutación ALK",
    ],
    0,
    "La mutación T790M confiere resistencia a gefitinib/erlotinib y se trata con osimertinib.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Intermedio",
    "¿Qué terapia se usa en leucemia mieloide crónica resistente con T315I?",
    [
        "Ponatinib",
        "Nilotinib",
        "Bosutinib",
        "Dasatinib",
    ],
    0,
    "Ponatinib mantiene actividad frente a la mutación T315I y se emplea en LMC resistente.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Avanzado",
    "¿Qué terapia dirigida se usa en tumores con fusiones ROS1?",
    [
        "Crizotinib",
        "Lorlatinib",
        "Osimertinib",
        "Selpercatinib",
    ],
    0,
    "Crizotinib y otros inhibidores de ROS1 son eficaces en CPNM con esta fusión.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Intermedio",
    "¿Qué estrategia combate resistencia mediada por MET tras EGFR-TKI?",
    [
        "Combinar amivantamab con lazertinib",
        "Aumentar la dosis",
        "Cambiar a inmunoterapia",
        "Suspender tratamiento",
    ],
    0,
    "La combinación de anticuerpos biespecíficos anti-EGFR/MET con TKIs aborda mecanismos de resistencia MET-dpendientes.",
)

add_question(
    "Genética y biología tumoral",
    "Terapias dirigidas",
    "Avanzado",
    "¿Qué fármaco inhibe IDH1 mutado en leucemia?",
    [
        "Ivosidenib",
        "Enasidenib",
        "Midostaurina",
        "Venetoclax",
    ],
    0,
    "Ivosidenib se dirige a IDH1 mutado, mientras enasidenib actúa sobre IDH2.",
)

# Investigación clínica - Ensayos
add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Básico",
    "¿Qué fase de ensayo evalúa seguridad y dosis máxima tolerada?",
    [
        "Fase I",
        "Fase II",
        "Fase III",
        "Fase IV",
    ],
    0,
    "Los ensayos fase I se centran en seguridad, farmacocinética y determinación de dosis recomendada.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Básico",
    "¿Qué característica define un ensayo fase II?",
    [
        "Evalúa eficacia preliminar",
        "Compara con estándar en grandes poblaciones",
        "Se realiza tras la comercialización",
        "Incluye solo voluntarios sanos",
    ],
    0,
    "Los fase II exploran eficacia y amplían datos de seguridad en pacientes con la enfermedad objetivo.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Intermedio",
    "¿Qué paradigma sigue un ensayo controlado aleatorizado?",
    [
        "Comparación entre tratamiento nuevo y control asignado al azar",
        "Observación retrospectiva",
        "Serie de casos",
        "Estudio cruzado sin control",
    ],
    0,
    "Los ensayos aleatorizados minimizan sesgos asignando tratamientos al azar y comparando con un control.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Intermedio",
    "¿Qué es una variable primaria?",
    [
        "Resultado principal que determina el éxito del estudio",
        "Cualquier dato exploratorio",
        "Variable secundaria",
        "Un efecto adverso",
    ],
    0,
    "La variable primaria es el endpoint crítico sobre el cual se calcula el tamaño muestral y se evalúa la hipótesis principal.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Avanzado",
    "¿Qué ventaja tienen los ensayos adaptativos?",
    [
        "Permiten modificar aspectos del estudio basados en análisis interinos",
        "Eliminan el azar",
        "No requieren consentimiento",
        "No necesitan análisis estadístico",
    ],
    0,
    "Los diseños adaptativos introducen ajustes predefinidos (ej. tamaño muestral, brazos) según resultados interinos.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Básico",
    "¿Qué es un ensayo doble ciego?",
    [
        "Ni participantes ni investigadores conocen la asignación",
        "Solo el paciente desconoce el tratamiento",
        "Solo el investigador desconoce",
        "No existe control",
    ],
    0,
    "El doble ciego reduce sesgos de observador y placebo al ocultar la asignación a ambos.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Intermedio",
    "¿Qué finalidad tiene un análisis interino de seguridad?",
    [
        "Detectar toxicidades graves tempranas",
        "Cambiar la hipótesis",
        "Reducir el tamaño muestral",
        "Evitar el seguimiento",
    ],
    0,
    "Los Comités de Monitorización realizan análisis interinos para detectar señales de toxicidad y proteger a los participantes.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Avanzado",
    "¿Qué es un endpoint compuesto?",
    [
        "Combinación de varios eventos clínicos relevantes",
        "Un evento único",
        "Variable secundaria",
        "Medida exploratoria",
    ],
    0,
    "Los endpoints compuestos agrupan eventos (p. ej., progresión o muerte) para aumentar potencia estadística.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Intermedio",
    "¿Qué caracteriza un estudio crossover?",
    [
        "Cada participante recibe secuencialmente ambos tratamientos",
        "Los grupos se comparan simultáneamente",
        "Se realiza en paralelo",
        "No requiere lavado",
    ],
    0,
    "En los estudios cruzados los participantes actúan como su propio control, requiriendo período de lavado.",
)

add_question(
    "Investigación clínica",
    "Diseño de ensayos",
    "Avanzado",
    "¿Qué objetivo tiene un ensayo de no inferioridad?",
    [
        "Demostrar que el nuevo tratamiento no es peor que el control dentro de un margen predefinido",
        "Mostrar superioridad",
        "Confirmar equivalencia exacta",
        "Determinar toxicidad",
    ],
    0,
    "Los ensayos de no inferioridad buscan mantener eficacia comparable con potenciales ventajas en seguridad u otros aspectos.",
)

# Farmacología oncológica - Terapias avanzadas
add_question(
    "Farmacología oncológica",
    "Anticuerpos conjugados",
    "Avanzado",
    "¿Cuál es el mecanismo de acción principal de trastuzumab deruxtecán (T-DXd) en cáncer de mama HER2+?",
    [
        "Entrega un inhibidor de topoisomerasa I tras internalización mediada por HER2",
        "Bloquea el dominio extracelular HER2 impidiendo dimerización",
        "Inhibe la tirosina cinasa citoplasmática de HER2",
        "Activa linfocitos T mediante CD3",
    ],
    0,
    "Trastuzumab deruxtecán es un anticuerpo conjugado que internaliza y libera deruxtecán, inhibidor de topoisomerasa I, tras unirse a HER2.",
)

add_question(
    "Farmacología oncológica",
    "Anticuerpos conjugados",
    "Avanzado",
    "¿Qué toxicidad limitante obliga a monitorizar la función pulmonar con T-DXd?",
    [
        "Enfermedad pulmonar intersticial/neumonitis",
        "Hipertensión pulmonar",
        "Fibrosis pleural",
        "Hemorragia alveolar",
    ],
    0,
    "T-DXd se asocia a enfermedad pulmonar intersticial; la ficha técnica exige detectar síntomas tempranos para suspender el fármaco.",
)

add_question(
    "Farmacología oncológica",
    "Anticuerpos conjugados",
    "Avanzado",
    "¿Qué diana reconoce sacituzumab govitecán y qué citotóxico libera?",
    [
        "Trop-2 y SN-38",
        "FRα y DM4",
        "HER2 y MMAE",
        "CD30 y auristatina",
    ],
    0,
    "Sacituzumab govitecán se une a Trop-2 y libera SN-38, metabolito activo de irinotecán.",
)

add_question(
    "Farmacología oncológica",
    "Anticuerpos conjugados",
    "Avanzado",
    "¿Cuál es el efecto adverso ocular característico de belantamab mafodotin?",
    [
        "Queratepatía epitelial microcística",
        "Retinopatía serosa",
        "Atrofia óptica",
        "Glaucoma agudo",
    ],
    0,
    "Belantamab mafodotin induce queratepatía epitelial; requiere exploraciones oftalmológicas periódicas.",
)

add_question(
    "Farmacología oncológica",
    "Anticuerpos conjugados",
    "Avanzado",
    "¿Qué recomendación recoge la ficha técnica de enfortumab vedotina respecto a la microangiopatía trombótica (MAT)?",
    [
        "Suspender definitivamente ante MAT confirmada",
        "Reducir dosis y continuar",
        "Añadir anticoagulación profiláctica",
        "Administrar plasma fresco congelado",
    ],
    0,
    "La aparición de microangiopatía trombótica obliga a suspender definitivamente enfortumab vedotina.",
)

add_question(
    "Farmacología oncológica",
    "Inmunoterapia",
    "Avanzado",
    "¿Qué biomarcador condiciona la dosis de tarlatamab (anti-DLL3) en CP microcítico según ficha técnica?",
    [
        "No requiere biomarcador; se pauta escalado 10→100 mg",
        "Expresión DLL3 >50%",
        "PD-L1 ≥10%",
        "Mutación RB1",
    ],
    0,
    "Tarlatamab se administra con escalado inicial fijo sin biomarcador obligatorio; DLL3 se expresa en la mayoría de células del CPMC.",
)

add_question(
    "Farmacología oncológica",
    "Inmunoterapia",
    "Avanzado",
    "¿Cuál es el manejo recomendado para la hepatotoxicidad grado 3 inducida por ipilimumab según ficha técnica?",
    [
        "Suspender ipilimumab y administrar corticoides IV",
        "Reducir a la mitad la dosis",
        "Añadir infliximab",
        "Esperar resolución espontánea",
    ],
    0,
    "Toxicidad hepática grado ≥3 requiere suspensión y corticoides sistémicos de alta dosis según las guías y ficha técnica.",
)

add_question(
    "Farmacología oncológica",
    "Inmunoterapia",
    "Avanzado",
    "¿Qué toxicidad cardiaca obliga a monitorizar ECG y troponinas durante el inicio de pembrolizumab + lenvatinib?",
    [
        "Síndrome de QT prolongado",
        "Miocarditis hiperaguda",
        "Tamponade",
        "Bloqueo AV completo",
    ],
    0,
    "La combinación incrementa riesgo de prolongación QT; se aconseja monitorización electrocardiográfica y electrolitos.",
)

add_question(
    "Farmacología oncológica",
    "Inmunoterapia",
    "Avanzado",
    "¿Qué profilaxis recomienda la ficha técnica de teclistamab para el síndrome de liberación de citocinas (SLC)?",
    [
        "Premedicación con dexametasona, antihistamínico y antipirético",
        "Infusión continua de tocilizumab",
        "Plasmaféresis preventiva",
        "Profilaxis con anakinra",
    ],
    0,
    "La ficha técnica de teclistamab exige premedicar con dexametasona, H1 y antipirético para reducir el riesgo de SLC.",
)

add_question(
    "Farmacología oncológica",
    "Inmunoterapia",
    "Avanzado",
    "¿Qué tratamiento recoge la ficha técnica para hipogammaglobulinemia sintomática inducida por teclistamab?",
    [
        "Administrar inmunoglobulina intravenosa",
        "Suspender el fármaco permanentemente",
        "Añadir rituximab",
        "Iniciar filgastrim",
    ],
    0,
    "Teclistamab puede causar hipogammaglobulinemia; se recomienda reposición con inmunoglobulina IV según necesidad clínica.",
)

add_question(
    "Farmacología oncológica",
    "Inmunoterapia",
    "Avanzado",
    "¿Qué pauta de premedicación describe la ficha técnica de glofitamab (CD20xCD3) para prevenir SLC?",
    [
        "Dexametasona, antihistamínico y antipirético antes de cada dosis",
        "Rituximab 375 mg/m² semanal previo",
        "Metilprednisolona en perfusión continua",
        "Infliximab a dosis fija",
    ],
    0,
    "Antes de glofitamab se administra premedicación estándar (corticoide, antihistamínico y antipirético); además se usa dosis única de obinutuzumab para depleción B, contemplada en la ficha técnica.",
)

add_question(
    "Farmacología oncológica",
    "Inhibidores de tirosina cinasa",
    "Avanzado",
    "¿Qué tratamiento requiere ajustar la dosis de osimertinib ante prolongación QTc >500 ms?",
    [
        "Suspender temporalmente hasta QTc <481 ms y reanudar a 80→40 mg",
        "Reducir a 20 mg diarios",
        "Añadir beta-bloqueante",
        "Continuar igual y monitorizar semanalmente",
    ],
    0,
    "La ficha técnica indica suspender osimertinib hasta normalización y considerar reanudar a 40 mg si QTc >500 ms.",
)

add_question(
    "Farmacología oncológica",
    "Inhibidores de tirosina cinasa",
    "Avanzado",
    "¿Cuál es la principal interacción de gilteritinib (FLT3) mencionada en ficha técnica?",
    [
        "Inhibidores potentes de CYP3A4 elevan su exposición",
        "Inductores de UGT1A1 elevan el AUC",
        "Anticoagulantes directos reducen eficacia",
        "Metformina aumenta niveles",
    ],
    0,
    "Inhibidores potentes de CYP3A4 (ej. azoles) incrementan los niveles de gilteritinib; se recomienda evitar o monitorizar.",
)

add_question(
    "Farmacología oncológica",
    "Inhibidores de tirosina cinasa",
    "Avanzado",
    "¿Qué ajuste recomienda la ficha técnica de selpercatinib ante hipertensión arterial grado 3?",
    [
        "Interrumpir hasta control y reanudar con reducción de dosis",
        "Continuar con antihipertensivos",
        "Suspender definitivamente",
        "Administrar diurético IV",
    ],
    0,
    "Ante hipertensión grado 3 se interrumpe selpercatinib y se reanuda con una reducción si se controla.",
)

add_question(
    "Farmacología oncológica",
    "Inhibidores de tirosina cinasa",
    "Avanzado",
    "¿Qué pauta alimentaria indica la ficha técnica de tucatinib?",
    [
        "Puede administrarse con o sin alimentos",
        "Debe tomarse en ayunas",
        "Requiere comida rica en grasa",
        "Evitar fibra 4 h previas",
    ],
    0,
    "Tucatinib se administra independientemente de las comidas, simplificando su pauta.",
)

add_question(
    "Farmacología oncológica",
    "Inhibidores de tirosina cinasa",
    "Avanzado",
    "¿Cuál es el manejo recomendado para toxicidad cutánea grado 3 con encorafenib + binimetinib?",
    [
        "Suspender ambos y reanudar con reducción escalonada",
        "Reducir solo binimetinib",
        "Añadir antihistamínicos y continuar",
        "Suspender definitivamente",
    ],
    0,
    "Las reacciones cutáneas de alto grado requieren suspender temporalmente ambos fármacos y reintroducir con reducción.",
)

add_question(
    "Farmacología oncológica",
    "Inhibidores de tirosina cinasa",
    "Avanzado",
    "¿Qué riesgo cardiovascular obliga a monitorizar lipasas con alpelisib?",
    [
        "Pancreatitis",
        "Cardiomiopatía dilatada",
        "Pericarditis constrictiva",
        "Arritmias ventriculares",
    ],
    0,
    "Alpelisib puede provocar pancreatitis; se recomienda monitorizar lipasa/amilasa y suspender si elevadas.",
)

add_question(
    "Farmacología oncológica",
    "Terapias dirigidas",
    "Avanzado",
    "¿Cuál es la toxicidad característica que obliga a monitorizar fósforo con infigratinib (FGFR2)?",
    [
        "Hiperfosfatemia",
        "Hipofosfatemia",
        "Hiponatremia",
        "Hipercalcemia",
    ],
    0,
    "Los FGFR inhibidores elevan fosfato; la ficha técnica recomienda restrictor dietético y quelantes si necesario.",
)

add_question(
    "Farmacología oncológica",
    "Terapias dirigidas",
    "Avanzado",
    "¿Qué combinación requiere profilaxis antiemética triple en la primera línea de cáncer gástrico HER2 negativo según ficha de zolbetuximab?",
    [
        "Zolbetuximab + mFOLFOX6",
        "Zolbetuximab + FLOT",
        "Zolbetuximab + paclitaxel",
        "Zolbetuximab en monoterapia",
    ],
    0,
    "Zolbetuximab se combina con mFOLFOX6, que requiere profilaxis antiemética estándar de alto riesgo.",
)

add_question(
    "Farmacología oncológica",
    "Terapias dirigidas",
    "Avanzado",
    "¿Qué mutación confiere resistencia primaria a larotrectinib según datos de ficha técnica?",
    [
        "Fusiones NTRK con mutaciones G623R",
        "KRAS G12C",
        "BRAF V600E",
        "METex14",
    ],
    0,
    "Mutaciones en el dominio quinasa de NTRK (ej. G623R) generan resistencia al larotrectinib.",
)

add_question(
    "Farmacología oncológica",
    "Terapias dirigidas",
    "Avanzado",
    "¿Qué precaución existe con abemaciclib respecto a la función hepática?",
    [
        "Obligatoria monitorización de transaminasas cada 2 semanas al inicio",
        "Contraindicado si AST/ALT >2x LSN",
        "No requiere control",
        "Solo si hay metástasis hepáticas",
    ],
    0,
    "Abemaciclib puede elevar transaminasas; se controla cada 2 semanas los dos primeros meses.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "Según la ficha técnica de la doxorrubicina liposomal, ¿cuál es la medida inicial recomendada ante extravasación?",
    [
        "Interrumpir la perfusión y aplicar compresas frías intermitentes sobre la zona",
        "Administrar dexrazoxano en las primeras 6 horas",
        "Aplicar calor local continuo",
        "Inyectar dimetilsulfóxido tópicamente",
    ],
    0,
    "Para la formulación liposomal, la ficha técnica indica detener la infusión, mantener la extremidad inmóvil y aplicar compresas frías intermitentes; no recomienda antídotos específicos como dexrazoxano.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "¿Qué soporte es obligatorio con altas dosis de methotrexato (>1 g/m²)?",
    [
        "Rescate con leucovorina y alcalinización urinaria",
        "Filgrastim desde el día 1",
        "Suplemento de ácido fólico",
        "Suero hipertónico",
    ],
    0,
    "Las dosis altas de MTX requieren rescate con leucovorina y alcalinización para prevenir nefrotoxicidad.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "¿Qué medida reduce el riesgo de neurotoxicidad aguda con oxaliplatino?",
    [
        "Evitar exposición al frío durante 48 h",
        "Administrar calcio-magnesio al inicio",
        "Mantener ayuno",
        "Hidratar con suero hipertónico",
    ],
    0,
    "La neuropatía aguda se exacerba con frío; se aconseja evitar bebidas frías y exposición a bajas temperaturas.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "¿Qué antiemesis refleja la ficha técnica de cisplatino a dosis >70 mg/m²?",
    [
        "Triple profilaxis (5-HT3, NK1, dexametasona)",
        "Ondansetrón monoterapia",
        "Metoclopramida continua",
        "Palonosetrón semanal",
    ],
    0,
    "Cisplatino es altamente emetógeno; se requiere triple terapia con antagonista 5-HT3, NK1 y dexametasona.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "¿Qué monitorización hematológica es obligatoria con temozolomida concurrente a radioterapia?",
    [
        "Hemograma semanal",
        "Biopsia medular mensual",
        "Ferritina semanal",
        "Dímero D",
    ],
    0,
    "La temozolomida debe acompañarse de hemograma semanal por riesgo de neutropenia y trombocitopenia.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "¿Qué condición obliga a usar factor estimulante de colonias primario con dosetaxel + carboplatino + trastuzumab + pertuzumab?",
    [
        "Riesgo de neutropenia febril ≥20%",
        "Edad <35 años",
        "Nivel de albúmina bajo",
        "ECOG 0",
    ],
    0,
    "Los regímenes con doble anti-HER2 y taxano se asocian a riesgo de neutropenia febril >20%, justificando G-CSF primario.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "¿Qué suplemento debe evitarse con capecitabina según ficha técnica por interacción farmacocinética?",
    [
        "Folínico",
        "Vitamina C",
        "Hierro oral",
        "Vitamina D",
    ],
    0,
    "El ácido folínico potencia la toxicidad de capecitabina y se evita su uso concomitante fuera de protocolos definidos.",
)

add_question(
    "Farmacología oncológica",
    "Quimioterapia clásica",
    "Avanzado",
    "¿Qué síndrome obliga a suspender definitivamente irinotecán?",
    [
        "Colitis neutropénica (typhlitis)",
        "Hepatitis",
        "Hipertensión",
        "Alopecia",
    ],
    0,
    "La colitis neutropénica es una complicación grave descrita que requiere suspensión definitiva del fármaco.",
)

add_question(
    "Farmacología oncológica",
    "Soporte y hormonoterapia",
    "Avanzado",
    "¿Qué precaución destaca la ficha técnica de degarelix respecto al síndrome de QT prolongado?",
    [
        "Vigilar ECG en pacientes con factores de riesgo o fármacos que prolonguen QT",
        "Administrar betabloqueantes",
        "Suplementar magnesio",
        "Nada, no prolonga QT",
    ],
    0,
    "Degarelix puede prolongar el QT; se debe evaluar ECG en pacientes con factores predisponentes o fármacos concomitantes.",
)

add_question(
    "Farmacología oncológica",
    "Soporte y hormonoterapia",
    "Avanzado",
    "¿Qué antídoto revierte las hemorragias por sobredosis de cabazitaxel?",
    [
        "No existe antídoto específico; se brinda soporte intensivo",
        "Vitamina K",
        "Ácido tranexámico",
        "Protamina",
    ],
    0,
    "Cabazitaxel no tiene antídoto; el manejo de sobredosis es soporte intensivo y G-CSF.",
)

add_question(
    "Farmacología oncológica",
    "Soporte y hormonoterapia",
    "Avanzado",
    "¿Qué efecto adverso grave obliga a monitorizar peso y presión arterial con abiraterona + prednisona?",
    [
        "Retención de líquidos y hipertensión",
        "Hiperglucemia",
        "Depresión",
        "Insuficiencia renal aguda",
    ],
    0,
    "La inhibición de CYP17 causa hiperaldosteronismo secundario con retención de líquidos e hipertensión.",
)

add_question(
    "Farmacología oncológica",
    "Soporte y hormonoterapia",
    "Avanzado",
    "¿Qué medicamento debe suspenderse 7 días antes de lenalidomida según ficha técnica en pacientes de riesgo trombótico?",
    [
        "Eritropoyetina",
        "Ácido acetilsalicílico",
        "Clopidogrel",
        "Metformina",
    ],
    0,
    "La lenalidomida aumenta el riesgo trombótico; la ficha técnica recomienda valorar suspender estimuladores eritropoyéticos 7 días antes en pacientes de riesgo.",
)

add_question(
    "Farmacología oncológica",
    "Soporte y hormonoterapia",
    "Avanzado",
    "¿Qué limitación renal impone la ficha técnica de zoledrónico en metástasis óseas?",
    [
        "Contraindicado si aclaramiento <30 mL/min",
        "Reducir al 50% si aclaramiento <60",
        "Usar cada 12 semanas",
        "No tiene limitación",
    ],
    0,
    "Zoledronato está contraindicado cuando el aclaramiento de creatinina es <30 mL/min por riesgo de deterioro renal.",
)

add_question(
    "Farmacología oncológica",
    "Soporte y hormonoterapia",
    "Avanzado",
    "¿Cuál es la interacción relevante entre apalutamida y anticonvulsivantes?",
    [
        "Apalutamida induce CYP3A4 y puede reducir niveles de anticonvulsivantes",
        "Apalutamida inhibe CYP2C9 aumentando niveles",
        "No existe interacción",
        "Disminuye absorción de valproato",
    ],
    0,
    "Apalutamida induce CYP3A4, 2C19 y 2C9, reduciendo concentraciones de fármacos como fenitoína o carbamazepina.",
)

add_question(
    "Farmacología oncológica",
    "Radioprotección",
    "Avanzado",
    "¿Qué indicación recoge amifostina en ficha técnica para prevenir xerostomía?",
    [
        "Radioterapia de cabeza y cuello con glándulas parótidas dentro del campo",
        "Radioterapia corporal total",
        "Radioterapia cerebral",
        "Radioterapia pélvica",
    ],
    0,
    "Amifostina se usa en radioterapia de cabeza y cuello para reducir xerostomía al proteger glándulas salivales.",
)

add_question(
    "Farmacología oncológica",
    "Radioprotección",
    "Avanzado",
    "¿Qué ajuste precisa Pluvicto (Lu-177 PSMA) según función renal?",
    [
        "No recomendado si aclaramiento <40 mL/min",
        "Reducir al 50% si aclaramiento <70",
        "Aumentar ingesta proteica",
        "Realizar hemodiálisis tras cada dosis",
    ],
    0,
    "Lu-177 PSMA no se recomienda en aclaramiento de creatinina <40 mL/min por falta de datos y riesgo de toxicidad.",
)

add_question(
    "Farmacología oncológica",
    "Radioprotección",
    "Avanzado",
    "¿Qué profilaxis antiemética requiere Pluvicto según ficha técnica?",
    [
        "Antiemético oral previo a cada infusión",
        "Triple terapia",
        "No precisa profilaxis",
        "Metoclopramida IV",
    ],
    0,
    "Pluvicto puede causar náuseas leves; se recomienda antiemético oral (ej. ondansetrón) antes de cada administración.",
)

add_question(
    "Farmacología oncológica",
    "Terapias celulares",
    "Avanzado",
    "¿Qué premedicación estándar exige la infusión de idecabtagene vicleucel (abecma) para reducir SLC?",
    [
        "Acetaminofén y antihistamínico H1 30-60 minutos antes",
        "Dexametasona 20 mg IV",
        "Profilaxis con tocilizumab",
        "Inmunoglobulina IV",
    ],
    0,
    "La ficha técnica de idecabtagene vicleucel indica administrar paracetamol y antihistamínico H1 antes de cada infusión para mitigar el síndrome de liberación de citocinas.",
)

add_question(
    "Farmacología oncológica",
    "Terapias celulares",
    "Avanzado",
    "¿Qué efecto adverso neurológico obliga a monitorización estrecha tras talquetamab (GPRC5D)?",
    [
        "Disgeusia severa y neurotoxicidad ICANS",
        "Neuropatía motora periférica",
        "Ataxia cerebelosa",
        "Ceguera cortical",
    ],
    0,
    "Talquetamab produce disgeusia intensa y riesgo de síndrome neurotóxico (ICANS); la ficha técnica aconseja monitorización neurológica.",
)

# Oncology Diagnosis and Testing -----------------------------------------------------------------

# 1A Oncology Diagnosis (14 preguntas)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Etiología y fisiopatología",
    "Avanzado",
    "¿Cuál de los siguientes factores provoca inestabilidad microsatelital de forma hereditaria y aumenta el riesgo de cáncer colorrectal?",
    [
        "Mutaciones germinales en MLH1 o MSH2",
        "Amplificación de HER2",
        "Pérdida heterocigota de RB1",
        "Translocación t(8;14)",
    ],
    0,
    "El síndrome de Lynch se debe a mutaciones germinales en genes reparadores de errores de apareamiento como MLH1/MSH2, originando inestabilidad microsatelital y un alto riesgo de tumores colorrectales y otros.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Etiología y fisiopatología",
    "Intermedio",
    "En el carcinoma hepatocelular asociado a hepatitis B, ¿qué mecanismo contribuye directamente a la carcinogénesis?",
    [
        "Integración del ADN viral en el genoma hepatocitario",
        "Hiperfosforilación de RB",
        "Inhibición de PARP",
        "Activación de ALK",
    ],
    0,
    "La infección crónica por VHB integra material genético viral en el genoma humano con expresión de proteínas oncogénicas (HBx) que promueven proliferación y resistencia a la apoptosis.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Etiología y fisiopatología",
    "Intermedio",
    "¿Qué vía metabólica alterada explica la dependencia de glutamina en muchos tumores sólidos?",
    [
        "Activación de MYC que induce glutaminólisis",
        "Pérdida de PTEN que inhibe mTOR",
        "Sobreactivación de SMAD",
        "Pérdida de APC",
    ],
    0,
    "La sobreexpresión de MYC potencia la glutaminólisis para sostener la síntesis de nucleótidos y energía en células tumorales altamente proliferativas.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Etiología y fisiopatología",
    "Avanzado",
    "El fenómeno de evasión inmune tumoral vinculado a la expresión de PD-L1 en la superficie celular se debe principalmente a",
    [
        "Inhibición de la señal de coestimulación T a través de PD-1",
        "Activación de la vía JAK/STAT en linfocitos",
        "Secreción de IL-2 por la célula tumoral",
        "Downregulation de CTLA-4",
    ],
    0,
    "Cuando PD-L1 tumoral se une a PD-1 se transmite una señal inhibitoria a los linfocitos T que reduce su proliferación y producción de citocinas, facilitando la evasión inmune.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Tipos de cáncer",
    "Intermedio",
    "¿Cuál es la histología más frecuente en cáncer de pulmón asociado a mutaciones activadoras de EGFR en no fumadores?",
    [
        "Adenocarcinoma",
        "Carcinoma escamoso",
        "Carcinoma neuroendocrino de células grandes",
        "Carcinoma adenoescamoso",
    ],
    0,
    "Las mutaciones en EGFR aparecen mayoritariamente en adenocarcinomas pulmonares, especialmente en pacientes nunca fumadores o con escasa exposición al tabaco.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Tipos de cáncer",
    "Avanzado",
    "En el linfoma de Hodgkin clásico, la presencia de células Reed-Sternberg se caracteriza inmunofenotípicamente por",
    [
        "CD30 y CD15 positivos con ausencia de CD45",
        "CD20 y CD3 coexpresados",
        "CD5 y cyclin D1 positivos",
        "CD10 y BCL6 negativos",
    ],
    0,
    "Las células Reed-Sternberg típicas expresan CD30 y CD15, carecen de antígenos panleucocitarios como CD45 y muestran expresión variable de PAX5.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Tipos de cáncer",
    "Intermedio",
    "¿Qué subtipo molecular de cáncer de mama tiene mayor relación con mutaciones germinales BRCA1?",
    [
        "Triple negativo basal-like",
        "Luminal A",
        "Luminal B HER2 negativo",
        "HER2 enriquecido",
    ],
    0,
    "Las pacientes portadoras de mutaciones BRCA1 suelen desarrollar tumores triple negativos con perfil basal-like y alta proliferación.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Tipos de cáncer",
    "Avanzado",
    "¿Cuál es la neoplasia maligna más relacionada con la exposición ocupacional a asbestos?",
    [
        "Mesotelioma pleural",
        "Carcinoma escamoso laríngeo",
        "Carcinoma epidermoide cutáneo",
        "Cáncer de tiroides medular",
    ],
    0,
    "La inhalación prolongada de fibras de asbesto se vincula estrechamente con mesotelioma pleural maligno, además de aumentar el riesgo de cáncer de pulmón.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biología molecular tumoral",
    "Avanzado",
    "¿Qué alteración define la dependencia oncogénica del GIST sensible a imatinib?",
    [
        "Mutaciones activadoras en KIT exón 11",
        "Fusión BCR-ABL",
        "Amplificación de MET",
        "Mutaciones en IDH1",
    ],
    0,
    "Los GIST clásicos muestran mutaciones activadoras en KIT, especialmente en el exón 11, que son sensibles a inhibidores de tirosina cinasa como imatinib.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biología molecular tumoral",
    "Intermedio",
    "Una mutación BRAFV600E confiere sensibilidad a qué clase de terapias dirigidas en melanoma metastásico?",
    [
        "Inhibidores de BRAF y MEK",
        "Inhibidores de ALK",
        "Inhibidores de CDK4/6",
        "Anticuerpos anti-HER2",
    ],
    0,
    "La sustitución V600E activa la vía MAPK y se trata con combinaciones dabrafenib/trametinib u otros inhibidores BRAF/MEK.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biología molecular tumoral",
    "Avanzado",
    "El fenotipo MSI-H (inestabilidad microsatelital alta) se asocia con",
    [
        "Mayor respuesta a inmunoterapia anti-PD-1",
        "Resistencia a fluoropirimidinas",
        "Menor carga mutacional tumoral",
        "Sobreexpresión de EGFR",
    ],
    0,
    "Los tumores MSI-H tienen alta carga mutacional y expresan neoantígenos que incrementan la eficacia de inhibidores de checkpoint como pembrolizumab.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Resistencia tumoral",
    "Avanzado",
    "La mutación T790M en EGFR representa",
    [
        "Un mecanismo de resistencia adquirida a inhibidores de EGFR de primera generación",
        "Una mutación germinal predisponente autosómica dominante",
        "Una deleción que confiere sensibilidad a gefitinib",
        "La pérdida de expresión de PD-L1",
    ],
    0,
    "El cambio T790M aumenta la afinidad de EGFR por ATP y confiere resistencia a gefitinib/erlotinib, siendo tratable con osimertinib.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Resistencia tumoral",
    "Intermedio",
    "La expresión de bombas de eflujo como P-glicoproteína (MDR1) causa",
    [
        "Resistencia a taxanos y antraciclinas",
        "Hipermutación",
        "Aumento del microambiente ácido",
        "Activación de mTOR",
    ],
    0,
    "La sobreexpresión de MDR1 favorece la expulsión de fármacos lipofílicos como taxanos, antraciclinas o vinca, reduciendo su eficacia.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Resistencia tumoral",
    "Avanzado",
    "¿Qué mecanismo permite a las células tumorales escapar de la terapia antiangiogénica con bevacizumab?",
    [
        "Activación de vías proangiogénicas alternativas como FGF",
        "Expresión de HER2",
        "Sobreproducción de IL-2",
        "Desactivación de MET",
    ],
    0,
    "La inhibición de VEGF puede inducir la señalización compensatoria de otros factores proangiogénicos (FGF, PDGF), manteniendo la neovascularización tumoral.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Resistencia tumoral",
    "Intermedio",
    "La paradoja de Warburg describe",
    [
        "Preferencia tumoral por glucólisis aeróbica incluso con oxígeno disponible",
        "Dependencia exclusiva de fosforilación oxidativa",
        "Producción de ácido láctico solo en hipoxia",
        "Uso de glutamina como único combustible",
    ],
    0,
    "La mayoría de tumores utilizan glucólisis aeróbica (efecto Warburg) generando lactato aun con oxígeno, favoreciendo ambiente ácido e intermediarios biosintéticos.",
)

# 1B Oncology Testing (14 preguntas)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Genómica",
    "Avanzado",
    "¿Qué tipo de alteración detecta con mayor sensibilidad un ensayo de NGS dirigido (panel) frente a la secuenciación Sanger?",
    [
        "Mutaciones puntuales concurrentes en múltiples genes",
        "Translocaciones equilibradas",
        "Aneuploidías cromosómicas",
        "Amplificaciones de genes críticos",
    ],
    0,
    "Los paneles de NGS permiten detectar simultáneamente variantes puntuales y pequeñas inserciones/deleciones en numerosos genes con alta cobertura, superando la capacidad unigen de Sanger.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Genómica",
    "Intermedio",
    "¿Cuál de las siguientes alteraciones es un ejemplo de amplificación génica accionable en cáncer de mama?",
    [
        "HER2 (ERBB2)",
        "BRAF V600E",
        "IDH2 R140Q",
        "NPM1",
    ],
    0,
    "La amplificación de HER2 conduce a sobreexpresión proteica detectable por IHQ/FISH y se trata con terapias anti-HER2.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Genómica",
    "Avanzado",
    "Una deleción en exon 19 de EGFR en pulmón se clasifica como",
    [
        "Mutación activadora sensible a inhibidores de EGFR",
        "Mutación de resistencia primaria",
        "Polimorfismo germinal sin significado",
        "Reordenamiento cromosómico",
    ],
    0,
    "Las deleciones en el exón 19 son mutaciones activadoras clásicas que confieren sensibilidad a gefitinib, erlotinib y osimertinib.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Prognóstico y pruebas predictivas",
    "Intermedio",
    "El índice FLIPI en linfoma folicular incluye",
    [
        "Edad, LDH, estadio Ann Arbor, recuento de ganglios y hemoglobina",
        "Edad, ECOG, ferritina, beta-2 microglobulina",
        "Edad, LDH, mutación MYD88, recuento plaquetario",
        "Edad, PSA, Gleason, densidad prostática",
    ],
    0,
    "FLIPI considera edad >60, estadio III/IV, LDH elevado, hemoglobina <12 g/dL y >4 áreas ganglionares afectas para estratificar riesgo.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Prognóstico y pruebas predictivas",
    "Avanzado",
    "Oncotype DX proporciona preferentemente",
    [
        "Riesgo de recurrencia y beneficio esperado de quimioterapia en cáncer de mama HR+",
        "Probabilidad de respuesta a trastuzumab",
        "Clasificación molecular triple negativo",
        "Riesgo de metástasis óseas",
    ],
    0,
    "Oncotype DX estima la probabilidad de recurrencia a 10 años y el beneficio quimioterápico en tumores HR+/HER2- estadio temprano.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Prognóstico y pruebas predictivas",
    "Intermedio",
    "¿Qué factor del IPI modificado para linfoma difuso de células B grandes se asocia con peor pronóstico?",
    [
        "Edad >60 años",
        "Ser mujer",
        "PCR elevada",
        "Anemia",
    ],
    0,
    "El IPI incluye edad >60, LDH elevada, ECOG ≥2, estadio III/IV y compromiso extranodal >1 sitio como factores adversos.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "NGS",
    "Avanzado",
    "En un panel de NGS multitumoral, ¿qué parámetro garantiza la sensibilidad para detectar variantes de baja frecuencia al analizar biopsia líquida?",
    [
        "Alta profundidad de lectura (coverage)",
        "Uso de cebadores universales",
        "Lectura de extremo único",
        "Enriquecimiento por hibridación sin PCR",
    ],
    0,
    "La ctDNA suele estar en bajas fracciones alélicas. Coberturas muy altas y umbrales bioinformáticos específicos permiten detectarlas.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "NGS",
    "Intermedio",
    "¿Qué limitación tiene la biopsia líquida respecto a la biopsia tisular en cáncer de pulmón?",
    [
        "Menor sensibilidad en enfermedad localizada",
        "Imposibilidad de detectar mutaciones activadoras",
        "No identifica reordenamientos",
        "Mayor número de falsos positivos",
    ],
    0,
    "En estadios tempranos la carga de DNA tumoral circulante es baja, reduciendo la sensibilidad de la biopsia líquida respecto al tejido.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biomarcadores",
    "Intermedio",
    "¿Qué biomarcador se expresa como CPS (Combined Positive Score)?",
    [
        "PD-L1 en cáncer gástrico",
        "TMB en melanoma",
        "HER2 en mama",
        "ALK en pulmón",
    ],
    0,
    "El CPS para PD-L1 suma células tumorales y del microambiente positivas sobre el número total de células viables en determinadas indicaciones gástricas y de cabeza-cuello.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biomarcadores",
    "Avanzado",
    "La puntuación TPS (tumor proportion score) en pulmón mide",
    [
        "Porcentaje de células tumorales viables con PD-L1",
        "Número de mutaciones por megabase",
        "Porcentaje de linfocitos CD8",
        "Índice proliferativo Ki-67",
    ],
    0,
    "El TPS evalúa la proporción de células tumorales que expresan PD-L1 respecto al total de tumores viables en el tejido.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biomarcadores",
    "Intermedio",
    "¿Qué prueba se solicita para determinar elegibilidad a terapias anti-HER2 en cáncer gástrico?",
    [
        "Inmunohistoquímica con confirmación por FISH si 2+",
        "PCR cuantitativa",
        "Secuenciación Sanger",
        "ELISA sérico",
    ],
    0,
    "La sobreexpresión de HER2 se evalúa por IHQ (0-3+). Los casos 2+ requieren confirmación con hibridación in situ (FISH/DISH).",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biomarcadores",
    "Avanzado",
    "¿Cuál de los siguientes marcadores predice beneficio de PARP inhibidores en cáncer de ovario?",
    [
        "Deficiencia de recombinación homóloga",
        "Amplificación de CCND1",
        "Expresión elevada de TOP2A",
        "Mutación KRAS",
    ],
    0,
    "Los tumores con deficiencia de recombinación homóloga (BRCA1/2 o score HRD alto) son sensibles a PARP inhibidores como olaparib.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Biomarcadores",
    "Intermedio",
    "Un TMB ≥10 mut/Mb se ha utilizado para",
    [
        "Aprobar pembrolizumab en tumor de sitio desconocido (indicación tissue-agnostic)",
        "Seleccionar pacientes para bevacizumab",
        "Indicar crizotinib",
        "Sugerir terapia anti-EGFR",
    ],
    0,
    "La FDA aprobó pembrolizumab para tumores sólidos con TMB alto (≥10 mut/Mb) refractarios a líneas previas, independentemente del origen.",
)

# 1C Detección y prevención (8 preguntas)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Detección",
    "Intermedio",
    "¿Con qué frecuencia se recomienda la mamografía en mujeres de riesgo promedio (50-74 años) según la USPSTF?",
    [
        "Cada 2 años",
        "Anual",
        "Cada 5 años",
        "Solo a los 50 y 60",
    ],
    0,
    "La USPSTF sugiere cribado bianual (cada dos años) en mujeres de 50 a 74 años con riesgo medio.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Detección",
    "Intermedio",
    "¿Qué técnica de cribado reduce mortalidad por cáncer de pulmón en fumadores de alto riesgo?",
    [
        "TAC de baja dosis anual",
        "Radiografía de tórax bianual",
        "Citología de esputo",
        "PET-TC anual",
    ],
    0,
    "Los ensayos NLST y NELSON demostraron reducción de mortalidad con TAC de baja dosis anual en fumadores/ exfumadores de alto riesgo.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Detección",
    "Intermedio",
    "Una mujer portadora de BRCA1 debe iniciar resonancia magnética mamaria",
    [
        "A partir de los 25-30 años anual",
        "A los 40 años",
        "Solo tras la menopausia",
        "No indicada",
    ],
    0,
    "Las guías recomiendan RM anual desde los 25-30 años en portadoras de BRCA, además de mamografía cuando sea apropiado.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Prevención",
    "Intermedio",
    "La vacunación frente al VPH se recomienda idealmente a",
    [
        "Niños y niñas de 11-12 años",
        "Solo mujeres mayores de 21",
        "Varones mayores de 40",
        "Pacientes con cáncer metastásico",
    ],
    0,
    "El CDC recomienda vacunación rutinaria contra VPH a 11-12 años (puede iniciarse desde los 9) en ambos sexos para prevenir cánceres asociados.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Prevención",
    "Avanzado",
    "¿Qué intervención reduce de forma significativa el riesgo de cáncer colorrectal en pacientes con poliposis adenomatosa familiar?",
    [
        "Colectomía profiláctica",
        "Tamoxifeno",
        "Uso crónico de estatinas",
        "Vitamina E",
    ],
    0,
    "La colectomía profiláctica (sub-total o total) es la intervención de elección en FAP para prevenir carcinoma colorrectal.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Prevención",
    "Intermedio",
    "¿Cuál es la recomendación de quimioprevención con tamoxifeno?",
    [
        "Mujeres premenopáusicas de alto riesgo de cáncer de mama ER+",
        "Varones BRCA1",
        "Pacientes con HER2 positivo",
        "Mujeres con triple negativo",
    ],
    0,
    "Tamoxifeno se ofrece a mujeres pre o perimenopáusicas con elevado riesgo de cáncer de mama ER+, reduciendo la incidencia de enfermedad invasiva y DCIS.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Recursos",
    "Básico",
    "¿Cuál de las siguientes organizaciones provee guías para pacientes y cuidadores sobre manejo de cáncer?",
    [
        "American Cancer Society",
        "NIH Clinical Center",
        "EMA",
        "USPSTF",
    ],
    0,
    "La ACS ofrece material educativo, guías y recursos de apoyo para pacientes oncológicos y sus familias.",
)

add_question(
    "Diagnóstico y pruebas oncológicas",
    "Recursos",
    "Intermedio",
    "¿Qué herramienta ayuda a evaluar alfabetización sanitaria y adaptar la educación al paciente?",
    [
        "Teach-back method",
        "Índice ECOG",
        "Puntuación FLIPI",
        "Score MELD",
    ],
    0,
    "La técnica teach-back consiste en pedir al paciente que repita con sus palabras la información para confirmar comprensión y ajustar la educación.",
)

# 2 Therapeutics and Patient Management ----------------------------------------------------------

# 2A Treatment Planning (26 preguntas)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Avanzado",
    "¿Cuál es el esquema estándar adyuvante para cáncer de colon estadio III con riesgo bajo según NCCN?",
    [
        "CAPOX durante 3 meses",
        "FOLFOX durante 6 meses",
        "FOLFIRI durante 6 meses",
        "5-FU/leucovorina durante 12 meses",
    ],
    0,
    "En tumores T1-3 N1, CAPOX por 3 meses ofrece beneficio comparable con menor toxicidad comparado con 6 meses de terapia.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "En cáncer de pulmón no microcítico estadio IV con mutación ALK, la terapia de primera línea preferida es",
    [
        "Alectinib",
        "Carboplatino/pemetrexed",
        "Pembrolizumab en monoterapia",
        "Docetaxel",
    ],
    0,
    "Los inhibidores ALK de segunda generación como alectinib, brigatinib o lorlatinib son estándar inicial por superioridad en PFS.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "¿Cuál es la terapia sistémica recomendada para cáncer de mama metastásico HR+/HER2- con mutación ESR1 tras inhibidor de aromatasa?",
    [
        "Elacestrant",
        "Fulvestrant en monoterapia",
        "Capecitabina",
        "Pembrolizumab",
    ],
    0,
    "Elacestrant, degradador oral selectivo de receptores de estrógeno, mostró superioridad en ESR1 mutado tras terapia endocrina.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Avanzado",
    "En el tratamiento perioperatorio del cáncer gástrico localmente avanzado, el régimen preferido actualmente es",
    [
        "FLOT",
        "EP",
        "CAPOX",
        "FOLFIRI",
    ],
    0,
    "FLOT (5-FU, leucovorina, oxaliplatino y docetaxel) ha mostrado mejores resultados frente a ECF/ECX en supervivencia global.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "La terapia de consolidación tras quimiorradioterapia en NSCLC estadio III irresecable PD-L1 ≥1% es",
    [
        "Durvalumab durante 12 meses",
        "Pembrolizumab durante 6 meses",
        "Osimertinib",
        "Carboplatino semanal",
    ],
    0,
    "PACIFIC demostró beneficio significativo con durvalumab por un año tras finalizar quimiorradioterapia en estadio III irresecable.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Avanzado",
    "¿Cuál es la combinación estándar para carcinoma hepatocelular avanzado en primera línea con función hepática Child-Pugh A?",
    [
        "Atezolizumab + bevacizumab",
        "Sorafenib",
        "Lenvatinib + pembrolizumab",
        "Durvalumab en monoterapia",
    ],
    0,
    "IMbrave150 estableció atezolizumab + bevacizumab como estándar al mejorar SG y SLP frente a sorafenib.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "En melanoma irresecable con mutación BRAFV600, ¿qué terapia combinada reduce el riesgo de recurrencia tras resección?",
    [
        "Dabrafenib + trametinib",
        "Ipilimumab + nivolumab",
        "Pembrolizumab",
        "Imatinib",
    ],
    0,
    "La terapia adyuvante con dabrafenib + trametinib reduce significativamente el riesgo de recurrencia en pacientes BRAFV600 mutados.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "El esquema preferido para carcinoma cervical persistente/recidivante PD-L1 positivo incluye",
    [
        "Pembrolizumab + quimioterapia ± bevacizumab",
        "Bevacizumab + paclitaxel",
        "Cisplatino semanal",
        "Durvalumab",
    ],
    0,
    "KEYNOTE-826 mostró beneficio significativo con pembrolizumab añadido a quimioterapia ± bevacizumab en enfermedad avanzada PD-L1 positiva.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Avanzado",
    "En linfoma difuso de células B grandes recaído precoz tras R-CHOP, el estándar actual en segunda línea para candidatos es",
    [
        "Terapia CAR-T anti-CD19",
        "R-ICE seguido de autotrasplante",
        "Lenalidomida",
        "Brentuximab vedotina",
    ],
    0,
    "Ensayos ZUMA-7 y TRANSFORM demostraron superioridad de CAR-T frente a quimio-rescate+ASCT en recaídas tempranas.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "¿Cuál es la recomendación terapéutica en leucemia mieloide crónica con respuesta subóptima a imatinib y mutación T315I?",
    [
        "Ponatinib",
        "Nilotinib",
        "Dasatinib",
        "Bosutinib",
    ],
    0,
    "La mutación T315I confiere resistencia a la mayoría de ITK excepto ponatinib, que mantiene actividad contra esta variante.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "En cáncer de próstata metastásico hormonosensible de alto volumen, el tratamiento inicial debe incluir",
    [
        "ADT + docetaxel",
        "ADT en monoterapia",
        "Enzalutamida sin ADT",
        "Apalutamida sola",
    ],
    0,
    "Las guías recomiendan intensificación con docetaxel o antiandrógenos potentes combinados con supresión androgénica en enfermedad hormonosensible de alto volumen.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Avanzado",
    "La terapia adyuvante estándar tras resección completa de carcinoma urotelial músculo invasivo con PD-L1 ≥1% incluye",
    [
        "Nivolumab durante 1 año",
        "Pembrolizumab",
        "Cisplatino",
        "Durvalumab",
    ],
    0,
    "CheckMate-274 demostró beneficio de nivolumab adyuvante en pacientes de alto riesgo (incluye PD-L1 ≥1%) tras cistectomía.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "¿Cuál es la terapia de elección en linfoma de Hodgkin clásico en recaída temprana tras autotrasplante?",
    [
        "Brentuximab vedotina",
        "Lenalidomida",
        "Ibritumomab",
        "Ibrutinib",
    ],
    0,
    "Brentuximab vedotina está aprobado como consolidación tras autotrasplante o en recaída, mejorando la supervivencia libre de progresión.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento del cáncer",
    "Intermedio",
    "Para pacientes con cáncer de ovario avanzado con respuesta completa a quimioterapia platino-sensible y HRD positivo, la recomendación de mantenimiento es",
    [
        "Olaparib",
        "Bevacizumab solo",
        "Carboplatino semanal",
        "Trabectedina",
    ],
    0,
    "Los PARP inhibidores como olaparib prolongan notablemente la SLP en pacientes con HRD positivo tras respuesta a platinos.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento de trastornos hematológicos",
    "Intermedio",
    "¿Cuál es el tratamiento de primera línea recomendado en anemia aplásica severa en menores de 40 años con donante compatible?",
    [
        "Trasplante alogénico de progenitores hematopoyéticos",
        "Ciclosporina + ATG",
        "Eltrombopag",
        "Azacitidina",
    ],
    0,
    "El trasplante alogénico de un donante HLA idéntico es la terapia curativa de elección en pacientes jóvenes con anemia aplásica severa.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento de trastornos hematológicos",
    "Intermedio",
    "¿Qué terapia de rescate es estándar en PTI crónica refractaria tras corticoides e IVIG?",
    [
        "Agonistas del receptor de trombopoyetina",
        "Azatioprina",
        "Profilaxis antibiótica",
        "Micofenolato",
    ],
    0,
    "Eltrombopag o romiplostim (agonistas del receptor de TPO) son pilares en PTI crónica refractaria, aumentando la producción plaquetaria.",
)

add_question(
    "Planificación terapéutica",
    "Tratamiento de trastornos hematológicos",
    "Avanzado",
    "En anemia falciforme con crisis frecuentes y herencia homocigota, la terapia modificadora de enfermedad recomendada es",
    [
        "Hydroxiurea",
        "Eritropoyetina",
        "Transfusión simple mensual",
        "Metotrexato",
    ],
    0,
    "La hidroxiurea incrementa la hemoglobina fetal y reduce la tasa de crisis dolorosas y hospitalizaciones en anemia falciforme homocigota.",
)

add_question(
    "Planificación terapéutica",
    "Paliativos y soporte",
    "Intermedio",
    "¿Qué escalera analgésica recomienda la OMS para dolor oncológico moderado-severo persistente pese a opioides débiles?",
    [
        "Escalar a opioides potentes",
        "Añadir benzodiacepinas",
        "Mantener AINE",
        "Usar esteroides",
    ],
    0,
    "La OMS propone escalar del segundo al tercer peldaño con opioides mayores (morfina, oxicodona) cuando los débiles resultan insuficientes.",
)

add_question(
    "Planificación terapéutica",
    "Paliativos y soporte",
    "Avanzado",
    "¿Qué manejo farmacológico se considera de primera línea para disnea refractaria en paciente oncológico avanzado?",
    [
        "Opioides sistémicos",
        "Broncodilatadores",
        "Antibióticos",
        "Diuréticos",
    ],
    0,
    "Los opioides (morfina) son el tratamiento farmacológico más efectivo para disnea refractaria en cuidados paliativos.",
)

add_question(
    "Planificación terapéutica",
    "Paliativos y soporte",
    "Intermedio",
    "¿Qué suplemento nutricional está indicado en caquexia oncológica cuando la ingesta oral es inadecuada?",
    [
        "Alimentos hiperproteicos orales",
        "Parenteral total",
        "Suplementos de vitamina A",
        "Creatina",
    ],
    0,
    "Se prioriza optimizar la ingesta oral con suplementos hiperproteicos antes de considerar nutrición enteral/parenteral.",
)

add_question(
    "Planificación terapéutica",
    "Cuidados al final de la vida",
    "Intermedio",
    "En un paciente con dolor refractario y pronóstico de días, ¿qué intervención es apropiada?",
    [
        "Sedación paliativa proporcional",
        "Escalar quimioterapia",
        "Iniciar inmunoterapia",
        "Derivar a UCI",
    ],
    0,
    "La sedación paliativa proporcional permite aliviar síntomas refractarios como dolor o disnea en fases terminales, respetando principios éticos.",
)

add_question(
    "Planificación terapéutica",
    "Supervivencia",
    "Intermedio",
    "En el plan de supervivencia tras cáncer de mama, ¿qué vigilancia es esencial?",
    [
        "Mamografía anual del seno restante o reconstruido",
        "PET-TC anual",
        "Determinación mensual de marcadores tumorales",
        "Colonoscopia anual",
    ],
    0,
    "La vigilancia incluye mamografía anual del tejido mamario residual y asesoramiento de estilo de vida; pruebas avanzadas no se recomiendan rutinariamente.",
)

add_question(
    "Planificación terapéutica",
    "Supervivencia",
    "Intermedio",
    "¿Qué intervención reduce linfoedema en supervivientes de cáncer de mama?",
    [
        "Ejercicio supervisado y compresión temprana",
        "Restricción total de movimiento",
        "Furosemida",
        "Vitaminas antioxidantes",
    ],
    0,
    "El ejercicio controlado, terapia de compresión y educación sobre autocuidados disminuyen el riesgo y la severidad del linfoedema.",
)

add_question(
    "Planificación terapéutica",
    "Determinantes sociales",
    "Intermedio",
    "¿Qué estrategia aborda mejor barreras de alfabetización en pacientes oncológicos de baja escolaridad?",
    [
        "Material educativo visual y lenguaje sencillo",
        "Entrega de folletos técnicos",
        "Citas menos frecuentes",
        "Prescripción electrónica",
    ],
    0,
    "Adaptar la comunicación con lenguaje claro, apoyos visuales y confirmación de comprensión mejora adherencia y seguridad.",
)

add_question(
    "Planificación terapéutica",
    "Determinantes sociales",
    "Básico",
    "¿Cuál es un ejemplo de determinante social que puede modificar la adherencia a terapias orales oncológicas?",
    [
        "Inseguridad alimentaria o económica",
        "Color de los comprimidos",
        "Edad >70",
        "Sexo masculino",
    ],
    0,
    "Factores como inseguridad económica, transporte, apoyo familiar o cobertura sanitaria influyen directamente en la adherencia farmacológica.",
)

add_question(
    "Planificación terapéutica",
    "Guías clínicas",
    "Intermedio",
    "¿Qué recurso es referencia para guías de práctica clínica en oncología en EE. UU.?",
    [
        "NCCN",
        "GOLD",
        "ADA",
        "IDSA",
    ],
    0,
    "Las guías NCCN ofrecen recomendaciones basadas en evidencia para el manejo integral de cáncer y se actualizan regularmente.",
)

# 2B Therapeutic Implementation (27 preguntas)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Avanzado",
    "Para ajustar dosis de carboplatino en quimioterapia, la fórmula de Calvert utiliza",
    [
        "AUC objetivo y aclaramiento de creatinina",
        "Peso corporal ideal",
        "Superficie corporal",
        "Nivel plasmático de fármaco",
    ],
    0,
    "Calvert calcula dosis = AUC deseada × (ClCr + 25). Es la fórmula estándar para personalizar carboplatino.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Intermedio",
    "En pacientes con insuficiencia renal severa (ClCr <30 mL/min), ¿qué fármaco requiere evitarse por acumulación neurotóxica?",
    [
        "Pemetrexed",
        "Paclitaxel",
        "Doxorrubicina",
        "Cisplatino",
    ],
    0,
    "Pemetrexed está contraindicado en ClCr <45 (y especialmente <30) por riesgo elevado de toxicidad hematológica y GI.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Intermedio",
    "La compatibilidad Y-site de vincristina durante la administración de infusión continua de cisplatino es",
    [
        "Incompatible; se debe usar línea separada",
        "Compatible",
        "Solo compatible con filtro 0.2 µm",
        "Depende del disolvente",
    ],
    0,
    "Vincristina no debe mezclarse con cisplatino en Y-site porque precipita y aumenta riesgo de toxicidad; se recomienda línea separada.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Avanzado",
    "¿Qué ajuste posológico requiere la ifosfamida al sospechar neurotoxicidad encefalopática grado 3?",
    [
        "Suspensión inmediata y evitar dosis futuras",
        "Reducir al 50%",
        "Administrar azul de metileno y continuar",
        "Aumentar hidratación y continuar",
    ],
    0,
    "La encefalopatía grado ≥3 obliga a suspender ifosfamida definitivamente; el azul de metileno se usa profiláctico en algunos casos.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Intermedio",
    "En pacientes con ictericia y bilirrubina total >3 mg/dL, se debe evitar",
    [
        "Irinotecán",
        "Oxaliplatino",
        "Cyclofosfamida",
        "Gemcitabina",
    ],
    0,
    "Irinotecán requiere metabolismo hepático y su toxicidad se incrementa notablemente con bilirrubina >2 mg/dL; se contraindica >3.",
)

add_question(
    "Implementación terapéutica",
    "Modalidades no farmacológicas",
    "Intermedio",
    "La braquiterapia intersticial está indicada en",
    [
        "Carcinoma cervical IB2",
        "Cáncer de tiroides",
        "Mesotelioma",
        "Leucemia linfoblástica",
    ],
    0,
    "En carcinoma cervical localmente avanzado se combina radioterapia externa con braquiterapia intersticial para lograr dosis altas en el tumor.",
)

add_question(
    "Implementación terapéutica",
    "Modalidades no farmacológicas",
    "Intermedio",
    "La resección quirúrgica metastásica (metastasectomía) mejora supervivencia en",
    [
        "Metástasis hepáticas resecables de cáncer colorrectal",
        "Metástasis óseas múltiples",
        "Metástasis cerebrales múltiples",
        "Enfermedad leptomeníngea",
    ],
    0,
    "La resección de metástasis hepáticas en cáncer colorrectal selecto ofrece supervivencia prolongada y potencial curación.",
)

add_question(
    "Implementación terapéutica",
    "Farmacogenómica",
    "Avanzado",
    "¿Qué alelo reduce drásticamente la actividad de dihidropirimidina deshidrogenasa y obliga a evitar fluoropirimidinas?",
    [
        "DPYD*2A",
        "UGT1A1*28",
        "TPMT*3A",
        "HLA-B*57:01",
    ],
    0,
    "DPYD*2A (mutación IVS14+1G>A) causa deficiencia de DPD y riesgo de toxicidad grave/lletal con 5-FU o capecitabina.",
)

add_question(
    "Implementación terapéutica",
    "Farmacogenómica",
    "Intermedio",
    "La dosis inicial de mercaptopurina debe reducirse en pacientes con",
    [
        "Deficiencia de TPMT o NUDT15",
        "Polimorfismo DPYD",
        "Mutación BRAF",
        "Alteración EGFR",
    ],
    0,
    "TPMT o NUDT15 reducidos disminuyen el metabolismo de tiopurinas; se requieren dosis reducidas o alternativas para evitar mielotoxicidad.",
)

add_question(
    "Implementación terapéutica",
    "Educación de pacientes",
    "Intermedio",
    "¿Qué consejo es clave para pacientes que inician terapia oral con lenalidomida?",
    [
        "Participar en el programa REMS con controles de embarazo",
        "Evitar alimentos grasos",
        "Tomar con antiácido",
        "Aumentar la ingesta de pomelo",
    ],
    0,
    "Lenalidomida requiere un programa REMS por teratogenicidad; mujeres en edad fértil necesitan test negativos y doble método anticonceptivo.",
)

add_question(
    "Implementación terapéutica",
    "Educación de pacientes",
    "Básico",
    "¿Qué técnica mejora adherencia en terapias orales complejas?",
    [
        "Pastilleros semanales y recordatorios electrónicos",
        "Indicaciones generales sin material",
        "Visitas trimestrales",
        "Evitar hablar de efectos adversos",
    ],
    0,
    "Organizadores físicos, recordatorios y educación personalizada facilitan adherencia a regímenes orales múltiples.",
)

add_question(
    "Implementación terapéutica",
    "Coordinación interdisciplinaria",
    "Intermedio",
    "¿Qué intervención previene errores al transicionar quimioterapia oral del hospital a la farmacia comunitaria?",
    [
        "Conciliación proactiva y comunicación con farmacéutico externo",
        "Entrega directa sin educación",
        "Suspender medicamentos concomitantes",
        "Uso de recetas en papel",
    ],
    0,
    "La coordinación con farmacia comunitaria mediante conciliación de medicación y comunicación sobre dosis y monitoreo reduce errores.",
)

add_question(
    "Implementación terapéutica",
    "Administración de fármacos",
    "Intermedio",
    "¿Qué vía de administración requiere filtro en línea de 0.22 µm para prevenir precipitados en taxanos?",
    [
        "Paclitaxel",
        "Docetaxel",
        "Nab-paclitaxel",
        "Vinorelbina",
    ],
    0,
    "Paclitaxel formulado en Cremophor requiere filtro 0.22 µm durante infusión para evitar partículas y reacciones.",
)

add_question(
    "Implementación terapéutica",
    "Administración de fármacos",
    "Avanzado",
    "Para prevenir extravasación de vesicantes, la administración debe realizarse preferentemente",
    [
        "A través de catéter venoso central",
        "Por acceso periférico en mano",
        "Subcutánea",
        "Intramuscular",
    ],
    0,
    "Vesicantes como antraciclinas deben administrarse por acceso central estable para minimizar riesgo de extravasación.",
)

add_question(
    "Implementación terapéutica",
    "Administración de fármacos",
    "Intermedio",
    "¿Cuál es el manejo recomendado si se retrasa la perfusión de rituximab por reacción grado 2?",
    [
        "Detener infusión, administrar medicación de soporte y reiniciar a velocidad reducida",
        "Suspender definitivamente",
        "Aumentar la velocidad",
        "Convertir a bolo IV",
    ],
    0,
    "Se detiene la infusión, se trata la reacción (antihistamínicos, esteroides) y tras resolución se reinicia lentamente.",
)

add_question(
    "Implementación terapéutica",
    "Administración de fármacos",
    "Básico",
    "¿Por qué se administra dexametasona previa a docetaxel?",
    [
        "Disminuir edema y reacciones de hipersensibilidad",
        "Mejorar absorción",
        "Aumentar metabolismo",
        "Potenciar efecto",
    ],
    0,
    "La dexametasona reduce el riesgo de reacciones de hipersensibilidad y retención de líquidos asociada a docetaxel.",
)

add_question(
    "Implementación terapéutica",
    "Terapias complementarias",
    "Intermedio",
    "¿Qué suplemento herbal puede interferir con imatinib al inducir CYP3A4?",
    [
        "Hierba de San Juan",
        "Ginseng",
        "Manzanilla",
        "Equinácea",
    ],
    0,
    "La hierba de San Juan induce CYP3A4/P-gp disminuyendo niveles plasmáticos de múltiples ITK como imatinib.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Avanzado",
    "En pacientes con QTc prolongado, ¿qué inhibidor de ALK tiene menor riesgo de arritmias?",
    [
        "Alectinib",
        "Crizotinib",
        "Lorlatinib",
        "Entrectinib",
    ],
    0,
    "Alectinib presenta menor incidencia de prolongación QT comparado con crizotinib o lorlatinib, siendo preferible en pacientes de riesgo.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Intermedio",
    "¿Cuál es la principal precaución al administrar vincristina en pediatría?",
    [
        "Nunca por vía intratecal",
        "Diluir en dextrosa",
        "Aumentar dosis según peso",
        "Administrar en bolo rápido",
    ],
    0,
    "La administración intratecal de vincristina es letal; deben existir medidas de seguridad estrictas para evitar errores de vía.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Intermedio",
    "¿Qué agente requiere profilaxis con ácido fólico y vitamina B12 para reducir toxicidad hematológica?",
    [
        "Pemetrexed",
        "Capecitabina",
        "Irinotecán",
        "Temozolomida",
    ],
    0,
    "Pemetrexed necesita suplementación con ácido fólico y B12 y premedicación con dexametasona para minimizar toxicidad hematológica y cutánea.",
)

add_question(
    "Implementación terapéutica",
    "Programas de asistencia",
    "Intermedio",
    "¿Qué recurso facilita acceso a fármacos orales costosos cuando no están cubiertos?",
    [
        "Programas de paciente de la industria",
        "Reposición automática",
        "Uso de medicamentos vencidos",
        "Compartir medicación",
    ],
    0,
    "Los programas de asistencia de fabricantes o fundaciones cubren parcialmente costos de terapias orales, cruciales en coordinación interdisciplinaria.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Avanzado",
    "¿Cuál es la estrategia de primera línea para minimizar síndrome mano-pie por capecitabina?",
    [
        "Ajuste de dosis y cuidado preventivo con cremas de urea",
        "Suspender definitivamente",
        "Añadir filgrastim",
        "Aumentar la dosis",
    ],
    0,
    "El síndrome mano-pie leve/moderado se maneja con emolientes, educación y reducción/interrupción temporal de capecitabina.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Intermedio",
    "¿Cuál es la recomendación al administrar olaratumab con doxorrubicina?",
    [
        "Control cardiaco base y acumulado",
        "Administrar por bolo",
        "Evitar antiemesis",
        "No usar dexrazoxano",
    ],
    0,
    "La doxorrubicina acumulada sigue siendo cardiotóxica; se requiere monitorizar función cardíaca y dosis acumulada incluso combinada con olaratumab.",
)

add_question(
    "Implementación terapéutica",
    "Farmacoterapia",
    "Avanzado",
    "Cuando se administra nivolumab + ipilimumab, ¿qué vigilancia es prioritaria en las primeras 12 semanas?",
    [
        "Control de toxicidad inmune (hepática, endocrina, dermatológica)",
        "Recuento neutrófilos diario",
        "Nivel plasmático de fármaco",
        "Calcio sérico",
    ],
    0,
    "Las combinaciones de checkpoint tienen alta incidencia de toxicidad inmune en las primeras semanas, requiriendo monitorización frecuente y educación.",
)

# 2C Cancer Outcomes and Treatment Monitoring (27 preguntas)

add_question(
    "Seguimiento y resultados",
    "Interacciones farmacológicas",
    "Intermedio",
    "¿Cuál de los siguientes antifúngicos incrementa de forma notable las concentraciones de tacrolimus al inhibir CYP3A4?",
    [
        "Voriconazol",
        "Fluconazol 100 mg",
        "Isavuconazol",
        "Caspofungina",
    ],
    0,
    "Voriconazol es un inhibidor potente de CYP3A4; al combinarlo con tacrolimus se requiere reducir sustancialmente la dosis y monitorizar niveles valle.",
)

add_question(
    "Seguimiento y resultados",
    "Interacciones farmacológicas",
    "Intermedio",
    "La ingesta habitual de jugo de pomelo debe evitarse con",
    [
        "Erlotinib",
        "Oxaliplatino",
        "Bevacizumab",
        "Lenalidomida",
    ],
    0,
    "El pomelo inhibe CYP3A4 intestinal elevando las concentraciones de ITK como erlotinib; esto incrementa riesgo de toxicidad cutánea y hepática.",
)

add_question(
    "Seguimiento y resultados",
    "Interacciones farmacológicas",
    "Intermedio",
    "Aprepitant reduce el INR de pacientes tratados con warfarina porque",
    [
        "Induce CYP2C9",
        "Inhibe CYP2C9",
        "Aumenta la síntesis de vitamina K",
        "Activa P-gp",
    ],
    0,
    "Aprepitant es un inductor moderado de CYP2C9; la administración concomitante disminuye el INR y obliga a monitorizar más de cerca.",
)

add_question(
    "Seguimiento y resultados",
    "Interacciones farmacológicas",
    "Avanzado",
    "Los inhibidores de bomba de protones disminuyen la exposición de cuál de los siguientes ITK por dependencia del pH gástrico?",
    [
        "Gefitinib",
        "Sorafenib",
        "Ponatinib",
        "Imatinib",
    ],
    0,
    "Gefitinib y otros ITK como erlotinib presentan absorción reducida con pH elevado. Se recomienda evitar IBP o espaciar su administración.",
)

add_question(
    "Seguimiento y resultados",
    "Mecanismos de resistencia",
    "Avanzado",
    "La mutación C797S en EGFR suele aparecer tras",
    [
        "Tratamiento con osimertinib",
        "Uso de gefitinib de primera línea",
        "Quimioterapia basada en platinos",
        "Inmunoterapia anti-PD-1",
    ],
    0,
    "C797S impide la unión covalente de osimertinib al receptor EGFR, generando resistencia adquirida tras su uso prolongado.",
)

add_question(
    "Seguimiento y resultados",
    "Mecanismos de resistencia",
    "Intermedio",
    "¿Qué mecanismo confiere resistencia adquirida a terapias dirigidas anti-BRAF en melanoma?",
    [
        "Activación de NRAS",
        "Pérdida de p53",
        "Amplificación de EGFR",
        "Mutación KIT",
    ],
    0,
    "La activación de NRAS reactiva la vía MAPK pese a la inhibición de BRAF, generando resistencia a dabrafenib/ trametinib.",
)

add_question(
    "Seguimiento y resultados",
    "Mecanismos de resistencia",
    "Intermedio",
    "El desarrollo de variantes del receptor androgénico (AR-V7) se asocia con resistencia primaria a",
    [
        "Enzalutamida y abiraterona",
        "Docetaxel",
        "Sipuleucel-T",
        "Mitoxantrona",
    ],
    0,
    "Las variantes AR-V7 carecen del dominio de unión a ligando, permanecen constitutivamente activas y confieren resistencia a antiandrógenos.",
)

add_question(
    "Seguimiento y resultados",
    "Mecanismos de resistencia",
    "Intermedio",
    "La mutación ALK G1202R confiere resistencia a",
    [
        "Inhibidores ALK de primera y segunda generación",
        "Lorlatinib",
        "Quimioterapia con pemetrexed",
        "Inhibidores de PD-1",
    ],
    0,
    "G1202R reduce la afinidad de crizotinib, alectinib y brigatinib; lorlatinib mantiene actividad frente a dicha mutación.",
)

add_question(
    "Seguimiento y resultados",
    "Prevención y manejo de toxicidad",
    "Intermedio",
    "¿Qué parámetro se monitoriza para detectar cardiotoxicidad por trastuzumab?",
    [
        "Fracción de eyección ventricular izquierda",
        "Troponina T diaria",
        "CK total",
        "LDH",
    ],
    0,
    "La FEVI se evalúa con ecocardiograma o MUGA cada 3 meses durante trastuzumab para detectar disfunción temprana.",
)

add_question(
    "Seguimiento y resultados",
    "Prevención y manejo de toxicidad",
    "Intermedio",
    "¿Cómo se previene el síndrome mano-pie asociado a sorafenib o regorafenib?",
    [
        "Uso regular de cremas con urea y educación sobre cuidados de manos/pies",
        "Aporte elevado de vitamina E",
        "Aumentar la dosis",
        "Profilaxis con filgrastim",
    ],
    0,
    "La hidratación cutánea intensiva, evitar fricciones y detectar síntomas tempranos reduce la severidad del síndrome mano-pie.",
)

add_question(
    "Seguimiento y resultados",
    "Prevención y manejo de toxicidad",
    "Avanzado",
    "¿Qué parámetro debe controlarse semanalmente al iniciar alpelisib?",
    [
        "Glucemia capilar",
        "Recuento plaquetario",
        "Creatinina",
        "Niveles de potasio",
    ],
    0,
    "Al inhibir PI3K-alfa, alpelisib produce hiperglucemia significativa; se monitoriza glucosa y se maneja con dieta o antidiabéticos.",
)

add_question(
    "Seguimiento y resultados",
    "Prevención y manejo de toxicidad",
    "Intermedio",
    "¿Qué agente se administra junto con ifosfamida para prevenir cistitis hemorrágica?",
    [
        "Mesna",
        "Palifermin",
        "Ondansetrón",
        "Darbepoetina",
    ],
    0,
    "Mesna se une a los metabolitos urotóxicos (acroleína) de ifosfamida evitando daño vesical.",
)

add_question(
    "Seguimiento y resultados",
    "Prevención y manejo de toxicidad",
    "Intermedio",
    "La monitorización de DLCO es útil para detectar a tiempo toxicidad pulmonar asociada a",
    [
        "Bleomicina",
        "Vincristina",
        "Cetuximab",
        "Oxaliplatino",
    ],
    0,
    "Bleomicina puede causar neumonitis intersticial temprana; el DLCO cada ciclo es sensible para detectar deterioro pulmonar.",
)

add_question(
    "Seguimiento y resultados",
    "Emergencias oncológicas",
    "Intermedio",
    "¿Cuál es la medida profiláctica fundamental en pacientes con alto riesgo de síndrome de lisis tumoral?",
    [
        "Hidratación vigorosa y alopurinol o rasburicasa",
        "Restricción hídrica",
        "Diuréticos de asa",
        "Calcitonina",
    ],
    0,
    "La hidratación y control del ácido úrico con alopurinol o rasburicasa previenen síndrome de lisis en tumores altamente proliferativos.",
)

add_question(
    "Seguimiento y resultados",
    "Emergencias oncológicas",
    "Intermedio",
    "El síndrome de vena cava superior requiere inicialmente",
    [
        "Elevar cabecera, oxígeno suplementario y esteroides",
        "Suspender líquidos",
        "Anticoagulación inmediata",
        "Quimioterapia en bolo",
    ],
    0,
    "Las medidas iniciales incluyen soporte respiratorio, elevación de la cabeza y, en algunos casos, esteroides. El tratamiento definitivo depende de la etiología (radioterapia, stent o quimioterapia).",
)

add_question(
    "Seguimiento y resultados",
    "Emergencias oncológicas",
    "Intermedio",
    "¿Qué agente es de elección en hipercalcemia maligna severa una vez corregida la volemia?",
    [
        "Ácido zoledrónico",
        "Calcio intravenoso",
        "Vitamina D",
        "Tamoxifeno",
    ],
    0,
    "Los bifosfonatos IV como zoledronato reducen la resorción ósea y son estándar en hipercalcemia maligna, junto a hidratación y calcitonina.",
)

add_question(
    "Seguimiento y resultados",
    "Emergencias oncológicas",
    "Intermedio",
    "En sospecha de compresión medular metastásica, el manejo inicial incluye",
    [
        "Corticoterapia de alta dosis y resonancia urgente",
        "Diuréticos",
        "Anticoagulación",
        "Observación expectante",
    ],
    0,
    "La dexametasona IV reduce el edema medular y la resonancia inmediata permite planificar radioterapia o descompresión quirúrgica.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones de terapia",
    "Intermedio",
    "¿Qué agente reduce la incidencia de mucositis oral severa en pacientes sometidos a quimioterapia de alta dosis antes de trasplante autólogo?",
    [
        "Palifermin",
        "Filgrastim",
        "Leucovorina",
        "Eritropoyetina",
    ],
    0,
    "Palifermin (factor de crecimiento de queratinocitos) disminuye la mucositis severa en pacientes sometidos a quimio de alta dosis previo a trasplante.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones de terapia",
    "Intermedio",
    "¿Qué intervención reduce el riesgo de neuropatía periférica por oxaliplatino?",
    [
        "Ajustar dosis ante síntomas persistentes y evitar exposición al frío",
        "Administrar vitamina B12",
        "Añadir taxanos",
        "Aumentar tasa de infusión",
    ],
    0,
    "La neuropatía se maneja reduciendo dosis o pausando tratamiento, y aconsejando evitar temperaturas frías que exacerban la sintomatología.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones de terapia",
    "Intermedio",
    "La tromboprofilaxis se recomienda en pacientes con cáncer ambulatorios cuando",
    [
        "Puntuación Khorana ≥2",
        "LDH elevada",
        "ECOG 0",
        "Edad <50",
    ],
    0,
    "Las guías ASCO/ASH sugieren tromboprofilaxis con DOAC o HBPM en pacientes ambulatorios con Khorana ≥2 sin contraindicaciones.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones de terapia",
    "Intermedio",
    "¿Cuál es la medida clave para prevenir osteonecrosis mandibular en pacientes que inician bifosfonatos?",
    [
        "Evaluación dental completa y resolución de focos infecciosos antes de la terapia",
        "Profilaxis antibiótica crónica",
        "Suplementación con vitamina D",
        "Uso de clorhexidina diaria",
    ],
    0,
    "La medida más efectiva es realizar evaluación odontológica y tratar problemas dentales antes de iniciar bifosfonatos o denosumab.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones de TPH/Celular",
    "Intermedio",
    "¿Cuál es la profilaxis estándar de enfermedad de injerto contra huésped en trasplante alogénico mieloablativo?",
    [
        "Inhibidor calcineurínico (ciclosporina/tacrolimus) + metotrexato",
        "Ciclosporina sola",
        "Rituximab",
        "Azacitidina",
    ],
    0,
    "La combinación de tacrolimus o ciclosporina con metotrexato en dosis bajas es el régimen profiláctico más utilizado para EICH aguda.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones de TPH/Celular",
    "Avanzado",
    "La enfermedad veno-oclusiva hepática post-trasplante se manifiesta con",
    [
        "Aumento de peso, hepatomegalia y bilirrubina elevada",
        "Hipotermia",
        "Hipoglucemia",
        "Hiponatremia",
    ],
    0,
    "La VOD cursa con retención hídrica >5%, hepatomegalia dolorosa y bilirrubina elevada; puede requerir defibrotide.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones de TPH/Celular",
    "Intermedio",
    "¿Cuál es el tratamiento de primera línea del síndrome de liberación de citocinas asociado a CAR-T grado ≥2?",
    [
        "Tocilizumab ± corticoides",
        "Infliximab",
        "Eculizumab",
        "Anakinra",
    ],
    0,
    "Tocilizumab (anti IL-6) es el tratamiento de elección para CRS moderado-severo; los corticoides se añaden si la respuesta es insuficiente.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones a largo plazo",
    "Intermedio",
    "¿Cuál es la complicación cardiovascular tardía más asociada con antraciclinas?",
    [
        "Cardiomiopatía dilatada",
        "Hipertensión",
        "Infarto agudo",
        "Arritmia supraventricular",
    ],
    0,
    "Las antraciclinas causan cardiomiopatía dilatada dependiente de la dosis acumulada; el riesgo persiste años después de la exposición.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones a largo plazo",
    "Intermedio",
    "En supervivientes de trasplante alogénico, la profilaxis de infecciones neumocócicas incluye",
    [
        "Vacunación secuencial con PCV13 seguida de PPSV23",
        "Profilaxis con penicilina de por vida",
        "Vacuna oral OPV",
        "Vacuna antigripal nasal",
    ],
    0,
    "Las guías recomiendan reinmunización con vacuna conjugada PCV13 y posteriormente PPSV23 aproximadamente 12 meses tras el trasplante.",
)

add_question(
    "Seguimiento y resultados",
    "Complicaciones a largo plazo",
    "Intermedio",
    "¿Qué estrategia ayuda a preservar la fertilidad en mujeres jóvenes sometidas a quimioterapia gonadotóxica?",
    [
        "Supresión ovárica con agonistas de GnRH",
        "Tamoxifeno",
        "Aspirina",
        "Calcio",
    ],
    0,
    "La administración de agonistas de GnRH durante la quimioterapia reduce el riesgo de insuficiencia ovárica prematura y preserva la fertilidad futura.",
)

# 3 Professional Practice -----------------------------------------------------------------------

# 3A Clinical Trials and Research (22 preguntas)

add_question(
    "Práctica profesional",
    "Métodos de investigación",
    "Intermedio",
    "¿Qué tipo de estudio utiliza asignación aleatoria pero no permite ciego de participantes por la naturaleza de la intervención?",
    [
        "Ensayo controlado aleatorizado abierto",
        "Estudio de cohorte prospectivo",
        "Serie de casos",
        "Ensayo cruzado",
    ],
    0,
    "Algunos ensayos clínicos deben ser abiertos (open-label) cuando el ciego es impracticable, pero mantienen la asignación aleatoria para minimizar sesgos.",
)

add_question(
    "Práctica profesional",
    "Métodos de investigación",
    "Intermedio",
    "¿Cuál es el propósito de un ensayo fase I en oncología?",
    [
        "Determinar dosis máxima tolerada y toxicidades",
        "Comparar eficacia con estándar",
        "Evaluar supervivencia global",
        "Analizar calidad de vida",
    ],
    0,
    "Los ensayos fase I se centran en evaluar seguridad, farmacocinética y dosis recomendada para estudios posteriores.",
)

add_question(
    "Práctica profesional",
    "Métodos de investigación",
    "Avanzado",
    "¿Qué diseño minimiza variabilidad interpaciente asignando cada sujeto a múltiples tratamientos en periodos distintos?",
    [
        "Ensayo cruzado (crossover)",
        "Ensayo adaptativo",
        "Cohorte retrospectiva",
        "Caso-control",
    ],
    0,
    "El diseño crossover asigna secuencialmente cada tratamiento al mismo participante, separando periodos por washout y reduciendo variabilidad interindividual.",
)

add_question(
    "Práctica profesional",
    "Métodos de investigación",
    "Intermedio",
    "¿Cuál es la característica principal de un ensayo pragmatico?",
    [
        "Evalúa efectividad en condiciones de práctica real",
        "Incluye solo pacientes muy seleccionados",
        "Carece de grupo control",
        "No requiere consentimiento",
    ],
    0,
    "Los ensayos pragmáticos buscan generalizar resultados a la práctica habitual incluyendo poblaciones amplias y procedimientos flexibles.",
)

add_question(
    "Práctica profesional",
    "Métodos de investigación",
    "Intermedio",
    "¿Qué elemento distingue un estudio caso-control de un estudio de cohorte?",
    [
        "La dirección temporal: caso-control es retrospectivo",
        "El uso de aleatorización",
        "El enfoque prospectivo obligatorio",
        "La inclusión de intervenciones",
    ],
    0,
    "Los estudios caso-control suelen ser retrospectivos, identifican sujetos con y sin evento y revisan exposiciones previas; las cohortes siguen sujetos en el tiempo.",
)

add_question(
    "Práctica profesional",
    "Estadística",
    "Intermedio",
    "El poder estadístico (1-β) representa",
    [
        "Probabilidad de detectar un efecto real",
        "Probabilidad de cometer error tipo I",
        "Probabilidad de aceptar la hipótesis nula",
        "Medida de tamaño de muestra",
    ],
    0,
    "El poder es la probabilidad de rechazar la hipótesis nula cuando es falsa; depende del tamaño de la muestra, la magnitud del efecto y el nivel alfa.",
)

add_question(
    "Práctica profesional",
    "Estadística",
    "Intermedio",
    "¿Qué estadístico se utiliza para comparar supervivencia entre dos grupos en un ensayo clínico?",
    [
        "Prueba de log-rank",
        "T de Student",
        "Chi cuadrado",
        "ANOVA",
    ],
    0,
    "La prueba de log-rank es la herramienta estándar para comparar curvas de Kaplan-Meier entre grupos de tratamiento.",
)

add_question(
    "Práctica profesional",
    "Estadística",
    "Intermedio",
    "El intervalo de confianza del 95% para hazard ratio de 0.70 (0.50-0.95) indica",
    [
        "Reducción significativa del riesgo",
        "No diferencia significativa",
        "Mayor riesgo en grupo experimental",
        "Error tipo II",
    ],
    0,
    "El IC del 95% no cruza 1, lo que sugiere reducción estadísticamente significativa del riesgo con el tratamiento experimental.",
)

add_question(
    "Práctica profesional",
    "Estadística",
    "Intermedio",
    "¿Qué medida resume el beneficio clínico necesario en términos de pacientes tratados para evitar un evento adicional?",
    [
        "Número necesario a tratar (NNT)",
        "Riesgo relativo",
        "Odds ratio",
        "Valor p",
    ],
    0,
    "El NNT indica cuántos pacientes deben tratarse para prevenir un evento adicional comparado con control; se calcula como 1/ARR.",
)

add_question(
    "Práctica profesional",
    "Resultados de investigación",
    "Intermedio",
    "Los desenlaces centrados en el paciente (patient-reported outcomes) evalúan",
    [
        "Percepción del paciente sobre síntomas y calidad de vida",
        "Respuesta tumoral radiológica",
        "Supervivencia libre de progresión",
        "Eventos adversos cardiacos",
    ],
    0,
    "Los PRO recogen la experiencia del paciente ante tratamientos, síntomas y calidad de vida sin intervención del clínico.",
)

add_question(
    "Práctica profesional",
    "Resultados de investigación",
    "Intermedio",
    "¿Cuál es un desenlace compuesto utilizado en ensayos oncológicos?",
    [
        "Supervivencia libre de fracaso",
        "Tasa de respuesta objetiva",
        "Tiempo hasta neutropenia",
        "Incidencia de diarrea",
    ],
    0,
    "La supervivencia libre de fracaso combina varios eventos (progresión, muerte, abandono por toxicidad) y es útil para reflejar fracaso del tratamiento.",
)

add_question(
    "Práctica profesional",
    "Resultados de investigación",
    "Intermedio",
    "Los estudios que evalúan utilidad de nuevas terapias incorporan análisis de",
    [
        "Medidas de beneficio clínico neto",
        "Costo directo únicamente",
        "Valor p exclusivamente",
        "Solo SG",
    ],
    0,
    "El beneficio clínico neto integra reducción de riesgo, supervivencia y toxicidad, ofreciendo una perspectiva equilibrada del impacto terapéutico.",
)

add_question(
    "Práctica profesional",
    "Ética e investigación",
    "Intermedio",
    "El principio de beneficencia en investigación clínica implica",
    [
        "Maximizar beneficios y minimizar riesgos",
        "Mantener confidencialidad absoluta",
        "Distribuir recursos equitativamente",
        "Obtener consentimiento verbal",
    ],
    0,
    "Beneficencia exige que los riesgos sean razonables en relación con los potenciales beneficios tanto para participantes como para la sociedad.",
)

add_question(
    "Práctica profesional",
    "Ética e investigación",
    "Intermedio",
    "¿Cuál de los siguientes elementos es obligatorio en un consentimiento informado válido?",
    [
        "Descripción de riesgos, beneficios y alternativas",
        "Compensación económica",
        "Firma del investigador únicamente",
        "Garantía de beneficio terapéutico",
    ],
    0,
    "El consentimiento debe describir finalidad, procedimientos, riesgos, beneficios, alternativas y derechos del participante, sin prometer beneficio seguro.",
)

add_question(
    "Práctica profesional",
    "Ética e investigación",
    "Intermedio",
    "La justicia en ensayos clínicos se refiere a",
    [
        "Selección equitativa de participantes",
        "Maximizar poder estadístico",
        "Minimizar costos",
        "Asegurar anonimato",
    ],
    0,
    "El principio de justicia implica una distribución equitativa de cargas y beneficios, evitando excluir o explotar poblaciones sin justificación científica.",
)

add_question(
    "Práctica profesional",
    "Diseño de ensayos",
    "Intermedio",
    "¿Qué fase de ensayo evalúa eficacia comparativa con el estándar de cuidado en grandes poblaciones?",
    [
        "Fase III",
        "Fase I",
        "Fase II",
        "Fase IV",
    ],
    0,
    "Los ensayos fase III comparan nuevas terapias con el estándar, evaluando eficacia, seguridad y potencial aprobación regulatoria.",
)

add_question(
    "Práctica profesional",
    "Diseño de ensayos",
    "Avanzado",
    "Los diseños adaptativos permiten",
    [
        "Modificar el ensayo basándose en análisis interinos preespecificados",
        "Cegar retrospectivamente a los investigadores",
        "Eliminar la aleatorización",
        "Evitar la necesidad de consentimiento",
    ],
    0,
    "Los ensayos adaptativos permiten ajustes (tamaño muestral, brazos) según datos interinos siempre que se planifique prospectivamente.",
)

add_question(
    "Práctica profesional",
    "Diseño de ensayos",
    "Intermedio",
    "Un endpoint compuesto usual en ensayos oncológicos incluye",
    [
        "Supervivencia libre de progresión",
        "Número de hospitalizaciones",
        "Tiempo hasta recuperación",
        "Carga viral",
    ],
    0,
    "La SLP combina progresión o muerte, reflejando el tiempo que un paciente permanece sin empeoramiento de la enfermedad.",
)

add_question(
    "Práctica profesional",
    "Diseño de ensayos",
    "Intermedio",
    "¿Qué fase suele evaluar intervenciones en población pediátrica tras establecer dosis en adultos?",
    [
        "Fase I/II pediátrica",
        "Fase III",
        "Fase IV",
        "Fase 0",
    ],
    0,
    "Una vez establecida dosis y seguridad en adultos, se realizan estudios fase I/II pediátricos para definir farmacocinética y eficacia preliminar.",
)

add_question(
    "Práctica profesional",
    "IRB/IEC",
    "Intermedio",
    "¿Cuál es la función principal de un Comité de Ética (IRB)?",
    [
        "Proteger los derechos y bienestar de los participantes",
        "Financiar estudios",
        "Reclutar pacientes",
        "Realizar análisis estadísticos",
    ],
    0,
    "El IRB revisa protocolos para garantizar que los riesgos sean razonables, el consentimiento informado adecuado y se protejan poblaciones vulnerables.",
)

add_question(
    "Práctica profesional",
    "Aprobación de fármacos",
    "Intermedio",
    "Un medicamento oncológico puede recibir aprobación acelerada de la FDA cuando",
    [
        "Muestra beneficio en un endpoint sustituto razonablemente probable",
        "Tiene menor costo",
        "No existen opciones de quimioterapia",
        "Se solicita por el fabricante",
    ],
    0,
    "La aprobación acelerada se basa en resultados sobre endpoints sustitutos (p. ej., respuesta) que predicen beneficio clínico en enfermedades graves sin opciones.",
)

add_question(
    "Práctica profesional",
    "Gestión de fármacos en investigación",
    "Intermedio",
    "¿Qué documento detalla almacenamiento, logística y devoluciones de un medicamento en investigación?",
    [
        "Manual del investigador",
        "Consentimiento informado",
        "Carta IRB",
        "Case report form",
    ],
    0,
    "El manual del investigador describe propiedades farmacológicas, condiciones de almacenamiento, manejo de devoluciones y seguridad del fármaco en investigación.",
)

# 3B Practice Management (22 preguntas)

add_question(
    "Gestión profesional",
    "Gestión de calidad",
    "Intermedio",
    "¿Cuál es el objetivo de un análisis causa-raíz tras un evento adverso?",
    [
        "Identificar causas sistémicas y proponer mejoras",
        "Asignar culpables",
        "Calcular costos",
        "Decidir sanciones",
    ],
    0,
    "El análisis causa-raíz busca entender procesos y barreras que llevaron al error para implementar acciones correctivas efectivas.",
)

add_question(
    "Gestión profesional",
    "Gestión de calidad",
    "Intermedio",
    "¿Qué indicador monitoriza la adecuación de protocolos de quimioterapia en farmacia oncológica?",
    [
        "Porcentaje de órdenes revisadas y verificadas por farmacéutico",
        "Número de pacientes atendidos",
        "Coste medio por ciclo",
        "Tiempo de espera",
    ],
    0,
    "El porcentaje de órdenes de quimioterapia verificadas por farmacéutico garantiza seguridad y adherencia a protocolos.",
)

add_question(
    "Gestión profesional",
    "Gestión de calidad",
    "Intermedio",
    "La metodología PDSA (Plan-Do-Study-Act) se utiliza para",
    [
        "Implementar mejoras continuas",
        "Validar medicamentos",
        "Auditorías regulatorias",
        "Capacitación",
    ],
    0,
    "PDSA es un ciclo iterativo que planifica, ejecuta, estudia resultados y ajusta procesos para la mejora continua.",
)

add_question(
    "Gestión profesional",
    "Gestión de inventario",
    "Intermedio",
    "¿Qué estrategia minimiza el desabasto de medicamentos oncológicos críticos?",
    [
        "Revisiones periódicas de niveles mínimos y acuerdos con múltiples proveedores",
        "Comprar grandes cantidades anualmente",
        "Compartir viales entre pacientes sin control",
        "Usar sustitutos no autorizados",
    ],
    0,
    "Mantener inventarios par, diversificar proveedores y monitorear demanda permite anticipar desabastos y establecer alternativas seguras.",
)

add_question(
    "Gestión profesional",
    "Gestión de inventario",
    "Intermedio",
    "El análisis ABC en inventario clasifica fármacos según",
    [
        "Valor económico y consumo",
        "Riesgo de toxicidad",
        "Requerimientos de refrigeración",
        "Fecha de caducidad",
    ],
    0,
    "La clasificación ABC prioriza recursos enfocándose en los productos de mayor valor o uso (clase A) para optimizar gestión y control.",
)

add_question(
    "Gestión profesional",
    "Gestión de inventario",
    "Intermedio",
    "¿Qué indicador evalúa la eficiencia en el uso de fármacos caros como CAR-T?",
    [
        "Tasa de utilización vs. caducidad",
        "Número de enfermeras",
        "Tiempo de infusión",
        "Nivel de glucosa",
    ],
    0,
    "Monitorear la proporción de dosis utilizadas frente a caducadas permite ajustar pedidos y minimizar pérdidas en terapias de alto costo.",
)

add_question(
    "Gestión profesional",
    "Manipulación y eliminación",
    "Intermedio",
    "La USP <800> establece estándares para",
    [
        "Manejo seguro de medicamentos peligrosos",
        "Regulación de ensayos clínicos",
        "Control de radiaciones",
        "Gestión de residuos biológicos",
    ],
    0,
    "La USP <800> proporciona lineamientos obligatorios sobre recepción, almacenamiento, preparación, administración y eliminación de fármacos peligrosos.",
)

add_question(
    "Gestión profesional",
    "Manipulación y eliminación",
    "Intermedio",
    "¿Cuál es la práctica correcta para desechar viales parcialmente usados de antraciclinas?",
    [
        "Eliminarlos como residuos peligrosos RCRA",
        "Vertirlos al desagüe",
        "Neutralizarlos con hipoclorito",
        "Refrigerarlos para uso posterior",
    ],
    0,
    "Las antraciclinas son residuos peligrosos listados por RCRA y deben descartarse en contenedores designados para incineración segura.",
)

add_question(
    "Gestión profesional",
    "Manipulación y eliminación",
    "Intermedio",
    "El uso de cabinas biológicas clase II en farmacias oncológicas permite",
    [
        "Mantener protección del trabajador y del producto durante la preparación",
        "Eliminar necesidad de guantes",
        "Almacenar viales",
        "Disminuir caducidades",
    ],
    0,
    "Las cabinas clase II BSC proporcionan flujo laminar y extracción filtrada que protegen tanto al personal como al medicamento estéril.",
)

add_question(
    "Gestión profesional",
    "Programas REMS",
    "Intermedio",
    "El programa REMS de lenalidomida requiere",
    [
        "Registro de prescriptores, farmacias y verificación de pruebas de embarazo",
        "Uso exclusivo hospitalario",
        "Receta en papel",
        "Monitorización de niveles plasmáticos",
    ],
    0,
    "El REMS de lenalidomida controla el riesgo teratogénico: prescriptores, farmacias y pacientes deben estar registrados y cumplir pruebas periódicas.",
)

add_question(
    "Gestión profesional",
    "Programas REMS",
    "Intermedio",
    "¿Cuál es un componente típico de un REMS para fármacos cardiotóxicos?",
    [
        "Monitorización periódica de ECG y reporte de eventos",
        "Aprobación de deriva",
        "Seguro obligatorio",
        "Hospitalización",
    ],
    0,
    "Los REMS pueden requerir monitorización de parámetros (p. ej., ECG, FEVI) y reporte, asegurando detección temprana de toxicidades graves.",
)

add_question(
    "Gestión profesional",
    "Programas REMS",
    "Intermedio",
    "El REMS de clozapina comparte con terapias oncológicas orales el requisito de",
    [
        "Notificar resultados de laboratorio antes de dispensar",
        "Entrega exclusivamente hospitalaria",
        "Uso de catéter central",
        "Consentimiento escrito",
    ],
    0,
    "Al igual que algunos fármacos oncológicos de alto riesgo, ciertos REMS exigen confirmación de laboratorio (ej. ANC) antes de cada dispensación.",
)

add_question(
    "Gestión profesional",
    "Uso compasivo",
    "Intermedio",
    "El acceso expandido (compasivo) a un fármaco en investigación requiere",
    [
        "Aprobación de la agencia regulatoria y consentimiento informado",
        "Aprobación automática del fabricante",
        "Entrega gratuita obligatoria",
        "Ensayo fase III activo",
    ],
    0,
    "Los programas de uso compasivo necesitan respaldo regulatorio (FDA/EMA), consentimiento informado y disponibilidad del fabricante.",
)

add_question(
    "Gestión profesional",
    "Uso compasivo",
    "Intermedio",
    "En EE. UU., el mecanismo \"Right-to-Try\" permite",
    [
        "Acceso a fármacos fase I aprobados para pacientes en situación crítica sin alternativas",
        "Uso de medicamentos genéricos",
        "Disminuir requisitos de REMS",
        "Evitar consentimiento informado",
    ],
    0,
    "La ley Right-to-Try posibilita que pacientes con enfermedades graves accedan a fármacos en investigación tras fase I, siempre que el fabricante acepte.",
)

add_question(
    "Gestión profesional",
    "Biosimilares",
    "Intermedio",
    "Un biosimilar se aprueba tras demostrar",
    [
        "Alta similitud en calidad, eficacia y seguridad con el biológico de referencia",
        "Precio más bajo",
        "Mayor potencia",
        "Fase III con miles de pacientes",
    ],
    0,
    "La aprobación se basa en un paquete analítico y clínico que demuestre ausencia de diferencias clínicamente significativas respecto al producto de referencia.",
)

add_question(
    "Gestión profesional",
    "Biosimilares",
    "Intermedio",
    "¿Qué concepto permite intercambiar un biosimilar por el producto original en farmacia sin contacto con el prescriptor (en EE. UU.)?",
    [
        "Designación de intercambiable",
        "Exención REMS",
        "Prior Authorization",
        "Off-label",
    ],
    0,
    "Solo los biosimilares con designación de \"interchangeable\" pueden sustituirse automáticamente según regulación estatal.",
)

add_question(
    "Gestión profesional",
    "Biosimilares",
    "Intermedio",
    "La farmacovigilancia de biosimilares requiere",
    [
        "Notificación con nombre comercial y número de lote",
        "Reporte solo por ingrediente activo",
        "No informar",
        "Usar códigos internos",
    ],
    0,
    "Para rastrear eventos adversos es imprescindible registrar nombre comercial y lote del biosimilar administrado.",
)

add_question(
    "Gestión profesional",
    "Estándares y regulaciones",
    "Intermedio",
    "¿Qué organización emite guías sobre seguridad en mezclas estériles antineoplásicas?",
    [
        "ASHP",
        "ADA",
        "GOLD",
        "AAFP",
    ],
    0,
    "La American Society of Health-System Pharmacists publica guías detalladas sobre preparación y seguridad de mezclas estériles oncológicas.",
)

add_question(
    "Gestión profesional",
    "Estándares y regulaciones",
    "Intermedio",
    "Las guías OSHA/NIOSH recomiendan",
    [
        "Uso de doble guante y protección ocular en manipulación de quimioterápicos",
        "Eliminar cabinas de seguridad",
        "Reutilizar jeringas",
        "Evitar controles anuales",
    ],
    0,
    "Para reducir exposición, las guías OSHA/NIOSH establecen EPP, cabinas apropiadas y procedimientos de derrames al manipular medicamentos peligrosos.",
)

add_question(
    "Gestión profesional",
    "Estándares y regulaciones",
    "Intermedio",
    "USP <797> aborda",
    [
        "Preparaciones estériles",
        "Manipulación de radiofármacos",
        "Control de calidad",
        "Bioequivalencia",
    ],
    0,
    "La USP <797> establece requisitos para preparación de productos estériles en farmacias, incluidos procedimientos, capacitación y monitoreo ambiental.",
)

add_question(
    "Gestión profesional",
    "Estándares y regulaciones",
    "Intermedio",
    "¿Qué norma regula la eliminación segura de residuos peligrosos farmacéuticos en EE. UU.?",
    [
        "RCRA",
        "HIPAA",
        "CLIA",
        "OSHA",
    ],
    0,
    "La Resource Conservation and Recovery Act (RCRA) regula el manejo y eliminación de residuos peligrosos, incluidos fármacos citotóxicos listados.",
)

add_question(
    "Gestión profesional",
    "Estándares y regulaciones",
    "Intermedio",
    "La documentación de medicamentos peligrosos administrados a cada paciente debe incluir",
    [
        "Fecha, lote y personal que preparó/administró",
        "Costo unitario",
        "Únicamente dosis",
        "Tiempo de viaje",
    ],
    0,
    "Un registro completo facilita trazabilidad ante eventos adversos y cumple con requisitos regulatorios y de calidad.",
)

add_question(
    "Gestión profesional",
    "Estándares y regulaciones",
    "Intermedio",
    "¿Qué medida reduce errores de prescripción en quimioterapia?",
    [
        "Uso de ordenes electrónicas normalizadas con doble verificación",
        "Recetas manuscritas",
        "Comunicación verbal",
        "Dosis en mg/kg sin superficie",
    ],
    0,
    "Las órdenes electrónicas estandarizadas, con calculadoras integradas y doble verificación, reducen errores de dosis y esquema en quimioterapia.",
)

add_question(
    "Gestión profesional",
    "Gestión de inventario",
    "Intermedio",
    "¿Qué indicador evalúa el desperdicio financiero asociado a medicamentos oncológicos multidosis?",
    [
        "Porcentaje de viales abiertos descartados",
        "Número de pacientes tratados",
        "Tiempo de infusión",
        "Salario del personal",
    ],
    0,
    "Calcular el porcentaje de viales descartados permite implementar estrategias como vial sharing estandarizado y programación eficiente para reducir costos.",
)

add_question(
    "Gestión profesional",
    "Programas REMS",
    "Intermedio",
    "Un programa REMS puede requerir materiales educativos obligatorios para",
    [
        "Garantizar que prescriptores y pacientes comprendan riesgos específicos",
        "Aumentar ventas",
        "Reducir costos",
        "Evitar controles regulatorios",
    ],
    0,
    "Algunos REMS incluyen guías educativas y comprobantes de conocimiento para asegurar que todos los implicados entiendan riesgos y medidas de mitigación.",
)
























Path("src/data/questions.json").write_text(
    json.dumps(questions, ensure_ascii=False, indent=2)
)
print(f"Total preguntas: {len(questions)}")
