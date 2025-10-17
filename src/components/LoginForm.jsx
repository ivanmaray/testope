import { useState } from 'react';
import supabase from '../lib/supabaseClient.js';

const INITIAL_MODE = 'signIn';

const LoginForm = () => {
  const [mode, setMode] = useState(INITIAL_MODE);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setMessage(null);

    try {
      if (mode === 'signIn') {
        const { error } = await supabase.auth.signInWithPassword({ email, password });
        if (error) {
          throw error;
        }
      } else {
        const { error } = await supabase.auth.signUp({ email, password });
        if (error) {
          throw error;
        }
        setMessage('Revisa tu correo para confirmar la cuenta si es necesario.');
      }
    } catch (error) {
      setMessage(error.message ?? 'No se pudo completar la operación.');
    } finally {
      setLoading(false);
    }
  };

  const alternateMode = mode === 'signIn' ? 'signUp' : 'signIn';

  return (
    <section className="auth auth--split">
      <div className="auth__visual" aria-hidden>
        <div className="auth__visual-overlay" />
        <div className="auth__visual-content">
          <span className="auth__badge">OPE SESPA · Farmacia Hospitalaria 2025</span>
          <h2>Tu plataforma de entrenamiento para la OPE del SESPA.</h2>
          <p>Practica con preguntas tipo test de legislación y parte específica, simulacros cronometrados y análisis de resultados. Llega al examen con confianza y precisión.</p>
        </div>
      </div>

      <div className="auth__panel">
        <header className="auth__header">
          <h1>Preparación OPE SESPA · Farmacia Hospitalaria</h1>
          <p>Accede o crea tu cuenta para guardar tu progreso y seguir tu entrenamiento desde cualquier dispositivo.</p>
          <div className="auth__countdown" style={{marginTop:'0.5rem', fontSize:'0.9rem'}}>
            {(() => {
              const EXAM_START = new Date('2025-11-30T10:00:00+01:00');
              const now = new Date();
              const diff = EXAM_START - now;
              if (diff <= 0) return <strong>¡Hoy es el examen! 🏆</strong>;
              const days = Math.floor(diff / (1000 * 60 * 60 * 24));
              const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
              const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
              return <span>⏳ Quedan <strong>{days} días</strong> y {hours}h {minutes}m para el examen</span>;
            })()}
          </div>
        </header>

        <form className="auth__form" onSubmit={handleSubmit}>
          <label className="auth__field">
            <span>Email</span>
            <input
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
              autoComplete="email"
              placeholder="tu@email.com"
            />
          </label>

          <label className="auth__field">
            <span>Contraseña</span>
            <input
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
              minLength={6}
              autoComplete={mode === 'signIn' ? 'current-password' : 'new-password'}
            />
          </label>

          {message && <div className="auth__message">{message}</div>}

          <button type="submit" className="auth__submit" disabled={loading}>
            {loading ? 'Procesando…' : mode === 'signIn' ? 'Entrar' : 'Crear cuenta'}
          </button>
        </form>

        <footer className="auth__footer">
          <button
            type="button"
            className="auth__toggle"
            onClick={() => {
              setMode(alternateMode);
              setMessage(null);
            }}
          >
            {mode === 'signIn' ? '¿No tienes cuenta? Regístrate' : '¿Ya tienes cuenta? Inicia sesión'}
          </button>
        </footer>
      </div>
    </section>
  );
};

export default LoginForm;
