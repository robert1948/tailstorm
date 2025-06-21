import { useEffect, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

export default function Landing() {
  const { user } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (user) navigate('/dashboard');
  }, [user, navigate]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-100 to-white text-gray-800 px-4">
      <h1 className="text-5xl font-bold mb-6 text-blue-700 text-center">
        Welcome to CapeControl
      </h1>
      <p className="text-lg mb-10 max-w-xl text-center">
        Your intelligent assistant for business clarity, powered by AI.
      </p>
      <div className="flex flex-col sm:flex-row items-center space-y-4 sm:space-y-0 sm:space-x-6">
        <Link to="/login">
          <button className="w-40 px-6 py-3 bg-blue-600 text-white font-semibold rounded-xl shadow hover:bg-blue-700 transition">
            Log In
          </button>
        </Link>
        <Link to="/register">
          <button className="w-40 px-6 py-3 border border-blue-600 text-blue-600 font-semibold rounded-xl shadow hover:bg-blue-100 transition">
            Register
          </button>
        </Link>
      </div>
    </div>
  );
}
