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
    <section className="auth">
      <header className="auth__header">
        <h1>Simuped Onco Test</h1>
        <p>Inicia sesión o crea una cuenta para guardar tu progreso en la nube.</p>
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
    </section>
  );
};

export default LoginForm;
