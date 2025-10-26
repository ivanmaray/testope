import { useState, useEffect, useRef } from 'react';
import { guardarResultadoPabloTest, cargarResultadosPabloTest } from '../utils/pabloTestStorage.js';
import { preguntasPablo171025 } from '../data/pabloTest171025.js';
import { preguntasPablo241025 } from '../data/pabloTest241025.js';
import TestRunner from './TestRunner.jsx';
import Summary from './Summary.jsx';

const TIEMPO_TOTAL = 20 * 60; // 20 minutos en segundos

const PabloTest17Oct = ({ onVolver }) => {
  const [estado, setEstado] = useState('inicio'); // inicio, test, resultado, historial
  const [versionTest, setVersionTest] = useState('17'); // '17' o '24'
  const [preguntas, setPreguntas] = useState([]);
  const [respuestas, setRespuestas] = useState([]);
  const [indiceActual, setIndiceActual] = useState(0);
  const [tiempoRestante, setTiempoRestante] = useState(TIEMPO_TOTAL);
  const [iniciado, setIniciado] = useState(false);
  const [resultadoActual, setResultadoActual] = useState(null);
  const [historial, setHistorial] = useState([]);
  const finalizadoRef = useRef(false);
  const formatearTiempo = (segundos) => {
    const mins = Math.floor(segundos / 60);
    const secs = segundos % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };
  const historialStats = historial.length
    ? (() => {
        const totalIntentos = historial.length;
        const sumNota = historial.reduce((acc, intento) => acc + (parseFloat(intento.notaFinal) || 0), 0);
        const mejorNota = historial.reduce(
          (max, intento) => Math.max(max, parseFloat(intento.notaFinal) || 0),
          0,
        );
        const porcentajeMedio = historial.reduce(
          (acc, intento) => acc + (parseFloat(intento.porcentaje) || 0),
          0,
        );
        const tiempoMedioSegundos = Math.round(
          historial.reduce((acc, intento) => acc + (intento.tiempoEmpleado ?? 0), 0) / totalIntentos,
        );

        return {
          intentos: totalIntentos,
          notaMedia: (sumNota / totalIntentos).toFixed(2),
          mejorNota: mejorNota.toFixed(2),
          porcentajeMedio: (porcentajeMedio / totalIntentos).toFixed(1),
          tiempoMedio: formatearTiempo(Number.isFinite(tiempoMedioSegundos) ? tiempoMedioSegundos : 0),
        };
      })()
    : {
        intentos: 0,
        notaMedia: '--',
        mejorNota: '--',
        porcentajeMedio: '--',
        tiempoMedio: '--:--',
      };

  // Cargar 15 preguntas fijas del simulacro seleccionado (Farmacia Hospitalaria)
  const iniciarTest = () => {
    const preguntasDisponibles = versionTest === '17' ? preguntasPablo171025 : preguntasPablo241025;
    const seleccion = preguntasDisponibles.slice(0, 15);
    setPreguntas(seleccion);
    setRespuestas(Array(seleccion.length).fill(undefined));
    setIndiceActual(0);
    setTiempoRestante(TIEMPO_TOTAL);
    setIniciado(true);
    finalizadoRef.current = false;
    setEstado('test');
  };

  // Temporizador
  useEffect(() => {
    if (!iniciado || estado !== 'test') return;
    
    const intervalo = setInterval(() => {
      setTiempoRestante(prev => {
        if (prev <= 1) {
          finalizarTest();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    
    return () => clearInterval(intervalo);
  }, [iniciado, estado]);

  const seleccionarRespuesta = (indiceRespuesta) => {
    setRespuestas((prev) => {
      const actualizadas = [...prev];
      actualizadas[indiceActual] = indiceRespuesta;
      return actualizadas;
    });
  };

  const irSiguiente = () => {
    setIndiceActual((prev) => Math.min(prev + 1, preguntas.length - 1));
  };

  const irAnterior = () => {
    setIndiceActual((prev) => Math.max(prev - 1, 0));
  };

  const finalizarTest = async () => {
    if (estado !== 'test' || finalizadoRef.current) {
      return;
    }
    finalizadoRef.current = true;
    setIniciado(false);
    
    // Calcular resultado
    let correctas = 0;
    let incorrectas = 0;
    let enBlanco = 0;
    
    preguntas.forEach((pregunta, idx) => {
      const respuesta = respuestas[idx];
      if (respuesta === undefined || respuesta === null) {
        enBlanco++;
      } else if (Number(respuesta) === Number(pregunta.respuestaCorrecta)) {
        correctas++;
      } else {
        incorrectas++;
      }
    });

    const tiempoEmpleado = TIEMPO_TOTAL - tiempoRestante;
    const notaFinal = correctas; // Sin penalización por fallo
    const porcentaje = ((correctas / preguntas.length) * 100).toFixed(1);

    const preguntasDetalladas = preguntas.map((p, idx) => ({
      id: p.id,
      pregunta: p.pregunta,
      respuestaUsuario: respuestas[idx],
      respuestaCorrecta: p.respuestaCorrecta,
      opciones: p.opciones,
      explicacion: p.explicacion,
      categoria: p.categoria,
      subcategoria: p.subcategoria,
      dificultad: p.dificultad
    }));

    const resultadoParaGuardar = {
      fecha: new Date().toISOString(),
      fechaTest: versionTest === '17' ? '17/10/2025' : '24/10/2025',
      tiempoEmpleado,
      correctas,
      incorrectas,
      enBlanco,
      notaFinal: notaFinal.toFixed(2),
      porcentaje,
      preguntas: preguntasDetalladas,
    };

    const resultadoParaSummary = {
      ...resultadoParaGuardar,
      aciertos: correctas,
      respuestas,
      preguntas,
      respuestasTexto: [],
      configuracion: {
        modo: 'simulacro',
        categoria: 'Farmacia Hospitalaria',
        subcategoria: 'todas',
        dificultad: 'Varias',
        mezclarDificultades: true,
      },
      tiempoTotal: TIEMPO_TOTAL,
    };

    setResultadoActual(resultadoParaSummary);

    // Guardar en Supabase
    await guardarResultadoPabloTest(resultadoParaGuardar);
    
    setEstado('resultado');
  };

  const cargarHistorial = async () => {
    const datos = await cargarResultadosPabloTest();
    setHistorial(datos);
    setEstado('historial');
  };

  // Pantalla de inicio
  if (estado === 'inicio') {
    return (
      <div className="pablo-test">
        <section className="auth auth--split pablo-test__layout">
          <div className="auth__visual pablo-test__visual">
            <div className="auth__visual-overlay pablo-test__visual-overlay" />
            <div className="auth__visual-content pablo-test__visual-content">
              <h2>Test de Pablo</h2>
              <p>
                Simulacro cronometrado de Farmacia Hospitalaria: 15 preguntas {versionTest === '17' ? 'cuidadas' : 'muy difíciles'}, sin penalización y revisión completa
                de cada respuesta.
              </p>
              <ul className="pablo-test__metrics">
                <li>
                  <strong>15</strong>
                  <span>Preguntas</span>
                </li>
                <li>
                  <strong>20&nbsp;min</strong>
                  <span>Tiempo límite</span>
                </li>
                <li>
                  <strong>+1 / 0</strong>
                  <span>Puntuación</span>
                </li>
                <li>
                  <strong>Supabase</strong>
                  <span>Guardado</span>
                </li>
              </ul>
              <div className="pablo-test__quote">
                <p>
                  «Hazlo sin iniciar sesión, guarda tu intento y repásalo cuando quieras. Ideal para medir tu ritmo en una sesión
                  rápida.»
                </p>
              </div>
            </div>
          </div>

          <div className="auth__panel pablo-test__panel">
            <header className="pablo-test__header">
              <h1>Entrena como en el examen real</h1>
              <p>
                Preguntas específicas de Farmacia Hospitalaria, con temporizador integrado y corrección automática. Todo se
                guarda para que compares tu evolución.
              </p>
            </header>

            <div className="pablo-test__highlights">
              <article className="pablo-test__highlight">
                <span className="pablo-test__highlight-icon">🎯</span>
                <div>
                  <h3>Formato del simulacro</h3>
                  <p>Una única respuesta correcta, sin penalización por fallo y feedback inmediato.</p>
                </div>
              </article>
              <article className="pablo-test__highlight">
                <span className="pablo-test__highlight-icon">⏱️</span>
                <div>
                  <h3>Control del tiempo</h3>
                  <p>Cuenta atrás visible, barra de progreso y aviso cuando el tiempo se agota.</p>
                </div>
              </article>
              <article className="pablo-test__highlight">
                <span className="pablo-test__highlight-icon">📚</span>
                <div>
                  <h3>Banco actualizado</h3>
                  <p>Casos clínicos, legislación y farmacotecnia con explicaciones breves.</p>
                </div>
              </article>
              <article className="pablo-test__highlight">
                <span className="pablo-test__highlight-icon">💾</span>
                <div>
                  <h3>Historial accesible</h3>
                  <p>Tus intentos quedan guardados en Supabase para revisarlos sin límite.</p>
                </div>
              </article>
            </div>

            <section className="pablo-test__list">
              <h3>Selecciona la versión del simulacro</h3>
              <div className="pablo-test__selector">
                <button
                  type="button"
                  className={`pablo-test__option ${versionTest === '17' ? 'pablo-test__option--selected' : ''}`}
                  onClick={() => setVersionTest('17')}
                >
                  <strong>17 de octubre</strong>
                  <span>Preguntas cuidadas</span>
                </button>
                <button
                  type="button"
                  className={`pablo-test__option ${versionTest === '24' ? 'pablo-test__option--selected' : ''}`}
                  onClick={() => setVersionTest('24')}
                >
                  <strong>24 de octubre</strong>
                  <span>Preguntas muy difíciles</span>
                </button>
              </div>
            </section>

            <div className="pablo-test__actions">
              <button type="button" onClick={iniciarTest} className="pablo-test__primary">
                🚀 Comenzar test ahora
              </button>
              <button type="button" onClick={cargarHistorial} className="pablo-test__secondary">
                📊 Ver historial guardado
              </button>
              <button type="button" onClick={onVolver} className="pablo-test__ghost">
                ← Volver al inicio principal
              </button>
            </div>

            <p className="pablo-test__footnote">
              Resultados almacenados en Supabase sin necesidad de autenticación. Perfecto para repasos rápidos antes de la OPE
              2025.
            </p>
          </div>
        </section>
      </div>
    );
  }

  // Pantalla del test
  if (estado === 'test') {
    const preguntaActual = preguntas[indiceActual] ?? null;
    const respondidas = respuestas.filter((valor) => valor !== null && valor !== undefined).length;

    if (!preguntaActual) {
      return null;
    }

    return (
      <div className="pablo-test pablo-test--runner">
        <div className="pablo-test__runner-shell">
          <header className="pablo-test__runner-top">
            <div>
              <span className="pablo-test__tag">{versionTest === '17' ? '17 de octubre' : '24 de octubre'}</span>
              <h1>Simulacro en progreso</h1>
              <p>
                Pregunta {indiceActual + 1} de {preguntas.length}. Recuerda: +1 correcta, 0 incorrecta.
              </p>
            </div>
            <div className="pablo-test__runner-meta">
              <article>
                <span>Respondidas</span>
                <strong>
                  {respondidas} / {preguntas.length}
                </strong>
              </article>
              <article>
                <span>Restantes</span>
                <strong>{Math.max(preguntas.length - respondidas, 0)}</strong>
              </article>
            </div>
          </header>

          <TestRunner
            pregunta={preguntaActual}
            indiceActual={indiceActual}
            totalPreguntas={preguntas.length}
            respuestaSeleccionada={respuestas[indiceActual] ?? null}
            onSeleccionRespuesta={(indice) => seleccionarRespuesta(indice)}
            onSiguiente={() => irSiguiente()}
            onAnterior={() => irAnterior()}
            esPrimera={indiceActual === 0}
            esUltima={indiceActual === preguntas.length - 1}
            onFinalizar={finalizarTest}
            tiempoRestante={tiempoRestante}
            tiempoTotal={TIEMPO_TOTAL}
          />

          <p className="pablo-test__runner-note">
            Al pulsar “Finalizar test” guardaremos automáticamente tus resultados en Supabase.
          </p>
        </div>
      </div>
    );
  }

  // Pantalla de resultados
  if (estado === 'resultado' && resultadoActual) {
    return (
      <div className="pablo-test pablo-test--resultado">
        <div className="pablo-test__resultado-shell">
          <header className="pablo-test__resultado-header">
            <span className="pablo-test__tag">{versionTest === '17' ? '17 de octubre' : '24 de octubre'}</span>
            <h1>Resumen del simulacro</h1>
            <p>Revisa tus respuestas, descarga el informe y vuelve a intentarlo cuando quieras.</p>
          </header>

          <Summary
            resultado={resultadoActual}
            onRestart={() => {
              setEstado('inicio');
              setResultadoActual(null);
            }}
          />

          <footer className="pablo-test__resultado-footer">
            <button type="button" className="pablo-test__secondary" onClick={cargarHistorial}>
              📊 Ver historial guardado
            </button>
            <button
              type="button"
              className="pablo-test__primary"
              onClick={() => {
                setEstado('inicio');
                setResultadoActual(null);
              }}
            >
              🔄 Repetir simulacro
            </button>
          </footer>
        </div>
      </div>
    );
  }

  // Pantalla de historial
  if (estado === 'historial') {
    return (
      <div className="pablo-test pablo-test--history">
        <section className="pablo-history">
          <header className="pablo-history__header">
            <div>
              <span className="pablo-history__tag">Historial guardado</span>
              <h1>Resultados del Test de Pablo</h1>
              <p>
                Consulta tus simulacros anteriores, revisa la evolución de tu nota y compara tiempos. Todo se guarda automáticamente
                tras finalizar cada intento.
              </p>
            </div>
            <button type="button" className="pablo-history__back" onClick={() => setEstado('inicio')}>
              ← Volver al inicio
            </button>
          </header>

          <section className="pablo-history__summary">
            <article>
              <span>Total de intentos</span>
              <strong>{historialStats.intentos}</strong>
            </article>
            <article>
              <span>Nota media</span>
              <strong>{historialStats.notaMedia}</strong>
            </article>
            <article>
              <span>Mejor nota</span>
              <strong>{historialStats.mejorNota}</strong>
            </article>
            <article>
              <span>% aciertos medio</span>
              <strong>
                {historialStats.porcentajeMedio === '--' ? '--' : `${historialStats.porcentajeMedio}%`}
              </strong>
            </article>
            <article>
              <span>Tiempo medio</span>
              <strong>{historialStats.tiempoMedio}</strong>
            </article>
          </section>

          {historial.length === 0 ? (
            <div className="pablo-history__empty">
              <h2>No hay intentos guardados</h2>
              <p>Completa tu primer simulacro para empezar a registrar tus resultados aquí.</p>
              <button type="button" onClick={() => setEstado('inicio')}>
                🚀 Ir al test de Pablo
              </button>
            </div>
          ) : (
            <ul className="pablo-history__list">
              {historial.map((intento, idx) => {
                const numeroIntento = historial.length - idx;
                const fecha = new Date(intento.fecha);
                const tiempo = formatearTiempo(intento.tiempoEmpleado ?? 0);

                return (
                  <li key={`${intento.fecha}-${idx}`} className="pablo-history__item">
                    <div className="pablo-history__item-header">
                      <div>
                        <span className="pablo-history__item-index">Intento #{numeroIntento}</span>
                        <time dateTime={fecha.toISOString()}>{fecha.toLocaleString('es-ES')}</time>
                      </div>
                      <div className="pablo-history__item-score">
                        <strong>{intento.notaFinal}</strong>
                        <span>Nota final</span>
                      </div>
                    </div>

                    <div className="pablo-history__item-grid">
                      <div className="pablo-history__badge pablo-history__badge--success">
                        <strong>{intento.correctas}</strong>
                        <span>Correctas</span>
                      </div>
                      <div className="pablo-history__badge pablo-history__badge--error">
                        <strong>{intento.incorrectas}</strong>
                        <span>Incorrectas</span>
                      </div>
                      <div className="pablo-history__badge">
                        <strong>{intento.enBlanco}</strong>
                        <span>En blanco</span>
                      </div>
                      <div className="pablo-history__badge">
                        <strong>{tiempo}</strong>
                        <span>Tiempo</span>
                      </div>
                      <div className="pablo-history__badge">
                        <strong>{intento.porcentaje}%</strong>
                        <span>% aciertos</span>
                      </div>
                    </div>
                  </li>
                );
              })}
            </ul>
          )}
        </section>
      </div>
    );
  }

  return null;
};

export default PabloTest17Oct;
