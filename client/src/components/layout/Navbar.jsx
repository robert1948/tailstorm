import { Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function NavBar() {
  const navigate = useNavigate();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    setIsLoggedIn(!!token);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsLoggedIn(false);
    navigate("/login");
  };

  return (
    <nav className="bg-blue-700 text-white px-4 py-3 flex justify-between items-center shadow-md">
      <Link to="/" className="text-xl font-bold">
        CapeControl
      </Link>
      <div className="space-x-4 text-sm sm:text-base">
        {!isLoggedIn ? (
          <>
            <Link to="/login" className="hover:underline">
              Login
            </Link>
            <Link to="/register" className="hover:underline">
              Register
            </Link>
          </>
        ) : (
          <>
            <Link to="/dashboard" className="hover:underline">
              Dashboard
            </Link>
            <button onClick={handleLogout} className="hover:underline">
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  );
}
