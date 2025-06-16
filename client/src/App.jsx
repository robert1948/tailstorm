import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import { Suspense, lazy } from 'react';

// Lazy-loaded components
const Login = lazy(() => import('./pages/Login'));
const Register = lazy(() => import('./pages/Register'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Logout = lazy(() => import('./pages/Logout'));
const ProtectedRoute = lazy(() => import('./components/ProtectedRoute'));

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-900">
      <Navbar />
      <Suspense fallback={<div className="p-4 text-center">Loading...</div>}>
        <Routes>
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>
      </Suspense>
    </div>
  );
}
