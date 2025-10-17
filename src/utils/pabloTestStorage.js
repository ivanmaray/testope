import { supabase } from '../lib/supabaseClient.js';

/**
 * Guarda el resultado de un intento del Test de Pablo en Supabase
 * @param {Object} resultado - Objeto con los datos del intento
 * @returns {Promise<Object>} - Resultado de la operación
 */
export const guardarResultadoPabloTest = async (resultado) => {
  try {
    const { data, error } = await supabase
      .from('pablo_test_results')
      .insert([
        {
          fecha: resultado.fecha,
          tiempo_empleado: resultado.tiempoEmpleado,
          correctas: resultado.correctas,
          incorrectas: resultado.incorrectas,
          en_blanco: resultado.enBlanco,
          nota_final: parseFloat(resultado.notaFinal),
          porcentaje: parseFloat(resultado.porcentaje),
          preguntas: resultado.preguntas
        }
      ])
      .select();

    if (error) {
      console.error('Error al guardar resultado en Supabase:', error);
      throw error;
    }

    console.log('✅ Resultado guardado en Supabase:', data);
    return { success: true, data };
  } catch (error) {
    console.error('Error en guardarResultadoPabloTest:', error);
    return { success: false, error };
  }
};

/**
 * Carga todos los resultados del Test de Pablo desde Supabase
 * @returns {Promise<Array>} - Array de resultados ordenados por fecha (más reciente primero)
 */
export const cargarResultadosPabloTest = async () => {
  try {
    const { data, error } = await supabase
      .from('pablo_test_results')
      .select('*')
      .order('fecha', { ascending: false });

    if (error) {
      console.error('Error al cargar resultados desde Supabase:', error);
      throw error;
    }

    // Transformar los datos al formato que espera el componente
    const resultados = data.map(item => ({
      fecha: item.fecha,
      tiempoEmpleado: item.tiempo_empleado,
      correctas: item.correctas,
      incorrectas: item.incorrectas,
      enBlanco: item.en_blanco,
      notaFinal: item.nota_final.toString(),
      porcentaje: item.porcentaje.toString(),
      preguntas: item.preguntas
    }));

    console.log(`✅ Cargados ${resultados.length} resultados desde Supabase`);
    return resultados;
  } catch (error) {
    console.error('Error en cargarResultadosPabloTest:', error);
    return [];
  }
};

/**
 * Obtiene las estadísticas generales del Test de Pablo
 * @returns {Promise<Object>} - Objeto con estadísticas
 */
export const obtenerEstadisticasPabloTest = async () => {
  try {
    const resultados = await cargarResultadosPabloTest();
    
    if (resultados.length === 0) {
      return {
        totalIntentos: 0,
        notaMedia: 0,
        mejorNota: 0,
        porcentajePromedio: 0
      };
    }

    const totalIntentos = resultados.length;
    const notaMedia = resultados.reduce((sum, r) => sum + parseFloat(r.notaFinal), 0) / totalIntentos;
    const mejorNota = Math.max(...resultados.map(r => parseFloat(r.notaFinal)));
    const porcentajePromedio = resultados.reduce((sum, r) => sum + parseFloat(r.porcentaje), 0) / totalIntentos;

    return {
      totalIntentos,
      notaMedia: notaMedia.toFixed(2),
      mejorNota: mejorNota.toFixed(2),
      porcentajePromedio: porcentajePromedio.toFixed(1)
    };
  } catch (error) {
    console.error('Error en obtenerEstadisticasPabloTest:', error);
    return {
      totalIntentos: 0,
      notaMedia: 0,
      mejorNota: 0,
      porcentajePromedio: 0
    };
  }
};
