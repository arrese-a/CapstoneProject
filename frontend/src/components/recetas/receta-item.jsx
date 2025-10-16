import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faClock } from "@fortawesome/free-regular-svg-icons";
import imagenPlato from "../../../public/plato.png";

export default function RecetaItem({ recetaItem }) {
  const { id, nombre, ingredientes, tiempo_preparacion, imagen_url } = recetaItem;

  return (
    <div className="receta-todo">
      <Link to={`/r/${id}`}>
        <div className="imagen-receta">{imagen_url ? <img src={imagen_url} /> : <img src={imagenPlato} />}</div>
        <div className="titulo-receta">
          <h2>{nombre}</h2>
          <div className="tiempo-receta">
            <FontAwesomeIcon icon={faClock} className="tiempo-icono" />
            {tiempo_preparacion}
          </div>
        </div>

        <div className="bloque-receta">
          <div className="ingredientes">
            <h3>Ingredientes:</h3>
            <ul>
              {ingredientes &&
                ingredientes.map((ingrediente, index) => (
                  <li key={index}>
                    {ingrediente.nombre} - {ingrediente.cantidad} {ingrediente.unidad}
                  </li>
                ))}
            </ul>
          </div>
        </div>
      </Link>
    </div>
  );
}