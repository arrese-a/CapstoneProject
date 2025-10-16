import React, { useState, useRef, useEffect } from "react";
import { Link } from "react-router-dom";
import api from "../helpers/axios";
import RecetaItem from "./recetas/receta-item";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlusCircle, faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";

export default function Recetas(props) {
  const [recetaItems, setRecetaItems] = useState([]);
  const [busqueda, setBusqueda] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const getRecetas = async () => {
    setError("");
    setRecetaItems([]);
    setLoading(true);
    try {
      const response = await api.get(`/recetas?ingredientes=${busqueda}`, { withCredentials: true });
      console.log(`/recetas?ingredientes=${busqueda}`, response);
      setRecetaItems(response.data);
    } catch (error) {
      setError("No se ha encontrado ninguna receta con ese ingrediente");
    } finally {
      setLoading(false);
    }
  };

  const hacerBusquda = (evento) => {
    if (evento.key === "Enter") {
      evento.preventDefault();
      getRecetas();
    }
  };

  const handleChange = (event) => {
    setBusqueda(event.target.value);
  };

  useEffect(() => { getRecetas(); }, []);

  const recetas = recetaItems.map((receta) => <RecetaItem key={receta.id} recetaItem={receta} />);

  return (
    <div className="receta-container">
      <div className="encabezado-receta">
        <h1>Recetas</h1>
        <div className="encabezado-derecha">
          <div className="buscador-ingredientes">
            <button className="lupa-buscador" onClick={getRecetas}>
              <FontAwesomeIcon icon={faMagnifyingGlass} />
            </button>
            <input type="text" name="busqueda" placeholder="ej: cebolla, harina" value={busqueda} onChange={handleChange} onKeyDown={hacerBusquda} />
          </div>
          {props.loggedInStatus ? (
            <div className="btn-agregar">
              <Link to="/crear-receta">
                <FontAwesomeIcon icon={faPlusCircle} />
                <span className="helper">Añdir una receta nueva</span>
              </Link>
            </div>
          ) : null}
        </div>
      </div>
      <div className="lista-recetas">{recetas}</div>
      <div className="loader">
        {loading ? "Cargando más recetas..." : null}
      </div>
       {error && <p className="error-msg">{error}</p>}
    </div>
  );
}