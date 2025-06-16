import { Link, useNavigate } from 'react-router-dom';
import { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

export default function Navbar() {
  const navigate = useNavigate();
  const { user, logout } = useContext(AuthContext);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  // Preload route modules on hover
  const preloadDashboard = () => import('../pages/Dashboard');
  const preloadLogout = () => import('../pages/Logout');

  return (
    <nav className="bg-white shadow mb-6">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <div className="text-lg font-bold text-blue-600">CapeControl</div>
        <div className="space-x-4 flex items-center">
          <Link
            to="/"
            className="text-gray-700 hover:text-blue-600 transition"
            onMouseEnter={preloadDashboard}
          >
            Dashboard
          </Link>

          {!user && (
            <>
              <Link to="/login" className="text-gray-700 hover:text-blue-600 transition">Login</Link>
              <Link to="/register" className="text-gray-700 hover:text-blue-600 transition">Register</Link>
            </>
          )}

          {user && (
            <>
              <span className="text-sm text-gray-600">Hi, {user.email}</span>
              <button
                onClick={handleLogout}
                onMouseEnter={preloadLogout}
                className="text-red-600 hover:text-red-800 transition"
              >
                Logout
              </button>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
