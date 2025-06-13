import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="bg-white shadow mb-6">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <div className="text-lg font-bold text-blue-600">CapeControl</div>
        <div className="space-x-4">
          <Link to="/" className="text-gray-700 hover:text-blue-600 transition">Dashboard</Link>
          <Link to="/login" className="text-gray-700 hover:text-blue-600 transition">Login</Link>
          <Link to="/register" className="text-gray-700 hover:text-blue-600 transition">Register</Link>
        </div>
      </div>
    </nav>
  );
}
