import React from "react";
import { NavLink } from "react-router-dom";
import api from "../helpers/axios";
import imagenFondo from "../../public/fondo-nav.png";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSignOutAlt } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";

export default function NavigationBar(props) {
    const navigate = useNavigate();

    const dynamicLink = (route, key, linkText) => (
        <div className="nav-link-wrapper">
            <NavLink key={key} to={route} className={({ isActive }) => (isActive ? "nav-link-active" : "nav-link")}>
                {linkText}
            </NavLink>
        </div>
    );

        const handleSignOut = async () => {
            try {
                const response = await api.post("/sesion/logout", {}, { withCredentials: true });
                if (response.status === 200) {
                    navigate("/");
                    props.handleSuccessfulLogout();
                }
                return response.data;
            } catch (error) {
                console.log("Error signing out", error);
            }
        };

    const loggedInStatus = props.loggedInStatus;

    return (
        <div
            className="nav-bar-wrapper"
            style={{
                background: "url(" + imagenFondo + ")  no-repeat",
                backgroundSize: "cover",
                backgroundPosition: "center",
            }}
        >
            <input type="checkbox" id="menu-toggle" className="menu-checkbox" />
            <label htmlFor="menu-toggle" className="menu-toggle">
                ☰
            </label>
            <div className="columna-izquierda">
                <NavLink key="home" to="/" className={({ isActive }) => (isActive ? "nav-link-active" : "nav-link")}>
                    Home
                </NavLink>
                <NavLink key="recetas" to="/recetas" className={({ isActive }) => (isActive ? "nav-link-active" : "nav-link")}>
                    Recetas
                </NavLink>

                {loggedInStatus ? dynamicLink("/lista-compra", "listaCompra", "Lista Compra") : null}
                {loggedInStatus ? dynamicLink("/recetas-favoritas", "favoritas", "Recetas favoritas") : null}
            </div>
            <div className="columna-derecha">
                {loggedInStatus ? (
                    <div className="nav-link">
                        <a onClick={handleSignOut}>
                            {/* UserName??  */}
                            Salir <FontAwesomeIcon icon={faSignOutAlt} style={{ marginLeft: "10px" }} />
                        </a>
                    </div>
                ) : (
                    <div>
                        <NavLink to="/login" className={({ isActive }) => (isActive ? "nav-link-active" : "nav-link")}>
                            Entrar
                            <FontAwesomeIcon icon={faSignOutAlt} style={{ marginLeft: "10px" }} />
                        </NavLink>
                    </div>
                )}
            </div>
        </div>
    );
}