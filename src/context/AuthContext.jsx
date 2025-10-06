import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react';
import supabase from '../lib/supabaseClient.js';

const AuthContext = createContext({
  session: null,
  user: null,
  loading: true,
  signOut: async () => {},
  focusMode: false,
  toggleFocusMode: () => {},
});

export const AuthProvider = ({ children }) => {
  const [session, setSession] = useState(null);
  const [loading, setLoading] = useState(true);
  const [focusMode, setFocusMode] = useState(false);

  useEffect(() => {
    try {
      const stored = window.localStorage.getItem('simuped-focus-mode');
      setFocusMode(stored ? stored === 'true' : false);
    } catch (error) {
      setFocusMode(false);
    }
  }, []);

  useEffect(() => {
    let mounted = true;

    const initSession = async () => {
      const { data, error } = await supabase.auth.getSession();
      if (error) {
        // eslint-disable-next-line no-console
        console.error('Error obteniendo la sesión', error);
      }
      if (!mounted) return;
      setSession(data?.session ?? null);
      setLoading(false);
    };

    initSession();

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, nuevaSesion) => {
      if (!mounted) return;
      setSession(nuevaSesion);
      setLoading(false);
    });

    return () => {
      mounted = false;
      subscription.unsubscribe();
    };
  }, []);

  const signOut = useCallback(async () => {
    const { error } = await supabase.auth.signOut();
    if (error) {
      // eslint-disable-next-line no-console
      console.error('No se pudo cerrar sesión', error);
    }
  }, []);

  const toggleFocusMode = useCallback(() => {
    setFocusMode((prev) => {
      const next = !prev;
      try {
        window.localStorage.setItem('simuped-focus-mode', String(next));
      } catch (error) {
        // eslint-disable-next-line no-console
        console.warn('No se pudo persistir el modo enfoque', error);
      }
      return next;
    });
  }, []);

  const value = useMemo(
    () => ({
      session,
      user: session?.user ?? null,
      loading,
      signOut,
      focusMode,
      toggleFocusMode,
    }),
    [session, loading, signOut, focusMode, toggleFocusMode],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);

export default AuthContext;
