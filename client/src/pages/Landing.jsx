import { Link, useNavigate } from 'react-router-dom';
import { useEffect, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

export default function Landing() {
  const { user } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (user) navigate('/dashboard');
  }, [user, navigate]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-100 to-white text-gray-800">
      <h1 className="text-4xl font-bold mb-4">Welcome to CapeControl</h1>
      <p className="text-lg mb-8">
        Your intelligent assistant for business clarity, powered by AI.
      </p>
      <div className="space-x-4">
        <Link to="/login">
          <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
            Login
          </button>
        </Link>
        <Link to="/register">
          <button className="bg-gray-200 text-gray-800 px-4 py-2 rounded hover:bg-gray-300 transition">
            Register
          </button>
        </Link>
      </div>
    </div>
  );
}
