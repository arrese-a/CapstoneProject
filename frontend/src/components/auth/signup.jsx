import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../helpers/axios";
import { AuthContext } from "./auth";

export default function SignUpUsuario(props) {
  const auth = useContext(AuthContext);

  const [nombreUsuario, setNombreUsuario] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorText, setErrorText] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (event) => {
    const { name, value } = event.target;
    if (name === "nombreUsuario") setNombreUsuario(value);
    else if (name === "email") setEmail(value);
    else if (name === "password") setPassword(value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setErrorText(null);

    try {
      await api.post(
        "/sesion/signup",
        {
          username: nombreUsuario,
          email: email,
          password: password,
        },
        {
          withCredentials: true,
          headers: { "Content-Type": "application/json" },
        },
      );
      if (auth && auth.fetchUser) {
        await auth.fetchUser();
      }
      navigate("/");
    } catch (error) {
      const detalle = error.response.data.detail || "Error al registrar";
      setErrorText(detalle);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="signup-wrapper">
      <div className="columna-izquierda"></div>
      <div className="columna-derecha-signup">
        <form onSubmit={handleSubmit} className="signup-form-wrapper">
          <h1 className="titulo-form">Regístrate</h1>

          <div className="input-wrapper">
            Nombre de usuario
            <input
              type="text"
              name="nombreUsuario"
              placeholder="Tu nombre de usuario"
              value={nombreUsuario}
              onChange={handleChange}
            />
          </div>

          <div className="input-wrapper">
            Email
            <input
              type="email"
              name="email"
              placeholder="Tu email"
              value={email}
              onChange={handleChange}
            />
          </div>

          <div className="input-wrapper">
            Contraseña
            <input
              type="password"
              name="password"
              placeholder="Tu contraseña"
              value={password}
              onChange={handleChange}
            />
          </div>

          <button className="btn" type="submit" disabled={loading}>
            Registrar
          </button>
          {errorText && <p className="error-msg">{errorText}</p>}
        </form>
      </div>
    </div>
  );
}
