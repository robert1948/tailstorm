import { createContext, useState, useEffect } from 'react';
import { getCurrentUser } from '../api/user';
import { getToken } from '../utils/token';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initializeUser = async () => {
      const token = getToken();
      if (token) {
        try {
          const currentUser = await getCurrentUser();
          setUser(currentUser);
        } catch (err) {
          console.warn('Auto-login failed:', err.message);
          setUser(null);
        }
      }
      setLoading(false);
    };

    initializeUser();
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};
