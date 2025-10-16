import { useState, useContext } from "react";
import { AuthContext } from "./auth";

export default function Login() {
  const { login } = useContext(AuthContext);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      await login(email, password);
    } catch (err) {
      setError("Parece que el email o la contraseña son incorrectos");
    }
  };

  return (
    <div className="login-wrapper">
      <div className="columna-izquierda-login">
        <form onSubmit={handleSubmit}>
          <h1 className="titulo-form">Iniciar Sesión</h1>
          <div className="input-wrapper">
            <input
              placeholder="Email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <input
              placeholder="Contraseña"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button className="btn-login" type="submit">
              Entrar
            </button>

            {error && <p className="error-msg">{error}</p>}

            <div className="signup-desde-login">
              <a href="/signup">
                ¿No tienes cuenta?
                <span
                  style={{ textDecoration: "underline", marginLeft: "5px" }}
                >
                  Regístrate
                </span>
              </a>
            </div>
          </div>
        </form>
      </div>
      <div className="columna-izquierda"></div>
    </div>
  );
}
