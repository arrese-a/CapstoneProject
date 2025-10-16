import { NavLink } from "react-router-dom";
import recetario from "../public/recetario.png";
import cesta from "../public/cesta.png";
import favoritas from "../public/favoritas.png";
import signupImg from "../public/signup-icon.png";
import loginImg from "../public/login-icon.png";

export default function Home(props) {
  const loggedInStatus = props.loggedInStatus;

  const links = [
    { to: "/login", nombre: "Entrar", imagen: loginImg },
    { to: "/signup", nombre: "Regístrate", imagen: signupImg },
  ];
  const loggedLinks = [
    { to: "/lista-compra", nombre: "Lista de la compra", imagen: cesta },
    { to: "/recetas-favoritas", nombre: "Recetas favoritas", imagen: favoritas },
  ];

  return (
    <div className="home-wrapper">
      <div className="columna-izquierda"></div>
      <div className="columna-derecha">
        <h1>¡Bienvenidos al recetario de la abuela!</h1>
        <div className="home-img-wrapper">
          <NavLink key="/recetas" to="/recetas" className="home-img-link">
            <img src={recetario} alt="Recetas" />
            <h2> Recetas</h2>
          </NavLink>

          <div className="home-log-wrapper">
            {!loggedInStatus
              ? links.map(({ to, nombre, imagen }) => (
                  <NavLink key={to} to={to} className="home-img-link">
                    <img src={imagen} alt={nombre} />
                    <h2>{nombre}</h2>
                  </NavLink>
                ))
              : null}
          </div>

          {loggedInStatus
            ? loggedLinks.map(({ to, nombre, imagen }) => (
                <NavLink key={to} to={to} className="home-img-link">
                  <img src={imagen} alt={nombre} />
                  <h2>{nombre}</h2>
                </NavLink>
              ))
            : null}
        </div>
      </div>
    </div>
  );
}