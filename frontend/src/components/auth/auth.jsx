import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../helpers/axios";

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [loggedInStatus, setLogging] = useState(null);
  const navigate = useNavigate();


const fetchUser = async () => {
    try {
      const res = await api.get("/sesion/check-login", { withCredentials: true });
      setUser(res.data); 
      res.data.user ? setLogging(true) : setLogging(false);
    } catch (err) {
    setUser(null);
    setLogging(false) 
    } finally {
    setLoading(false);
    }
};
  const login = async (email, password) => {
  await api.post(`/sesion/login`, { email, password }, { withCredentials: true });

    await fetchUser(); 
    navigate("/");
  };

  const logout = async () => {
    await api.post(`/sesion/logout`, {}, { withCredentials: true });
    setUser(null);
    setLogging(false);
  };

  useEffect(() => {
    fetchUser();
  }, []);

  return (
    <AuthContext.Provider value={{ user, login, logout, loading, loggedInStatus, fetchUser }}>
      {children}
    </AuthContext.Provider>
  );
}
