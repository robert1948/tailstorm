import React, { createContext, useState, useEffect } from 'react';
import { getCurrentUser } from '../api/user';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(undefined); // 'undefined' means "checking"

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      getCurrentUser()
        .then(setUser)
        .catch(() => {
          localStorage.removeItem('token');
          setUser(null);
        });
    } else {
      setUser(null);
    }
  }, []);

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, setUser, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
