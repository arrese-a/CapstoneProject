import React, { useState, useEffect } from "react";
import api from "../../helpers/axios";
import ReactPlayer from "react-player";
import MostrarRichText from "../../helpers/rich-txt-mostrar";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBasketShopping, faStar as faStarSolid } from "@fortawesome/free-solid-svg-icons";
import { faStar, faClock } from "@fortawesome/free-regular-svg-icons";
import { useParams } from "react-router-dom";

export default function RecetaCompleta(props) {
  const params = useParams();
  const idReceta = params?.slug;
  const idUsuario = props.idUsuario;

  const [recetaCompleta, setRecetaCompleta] = useState({});
  const [recetaFavorita, setRecetaFavorita] = useState(false);

  const getRecetaCompleta = async () => {
    try {
      const response = await api.get(`/recetas/${idReceta}`);
      console.log(response);
      setRecetaCompleta(response.data);
    } catch (error) {
      console.log("Error cargando receta", error);
    }
  };

  const getFavorita = async () => {
    try {
      const response = await api.get(`/favoritas/favorita-check/${idUsuario}/${idReceta}`, {
        withCredentials: true,
      });
      console.log("responseGetFav", response);
      setRecetaFavorita(Boolean(response.data.es_favorita));
    } catch (error) {
      console.log("login error", error);
    }
  };

  const agregarFavoritos = async () => {
    try {
      const response = await api.post(`/favoritas/${idUsuario}/${idReceta}`, null, {
        withCredentials: true,
      });
      console.log("response agregarFavoritos", response);
      if (response.status === 200) {
        setRecetaFavorita(true);
      } else {
        console.log("Error al añadir a favoritos");
      }
    } catch (error) {
      console.log("login error", error);
    }
  };

  const quitarFavoritos = async () => {
    try {
      const response = await api.delete(`/favoritas/${idUsuario}/${idReceta}`, {
        withCredentials: true,
      });
      console.log("response quitarFavoritos", response);
      if (response.status === 200) {
        setRecetaFavorita(false);
      } else {
        console.log("Error al eliminar de favoritos");
      }
    } catch (error) {
      console.log("login error", error);
    }
  };

  const agregarListaCompra = async () => {
    try {
      const response = await api.post(
        `/lista-compra/agregar?usuario_id=${idUsuario}&receta_id=${idReceta}`,
        null,
        { withCredentials: true }
      );
      console.log("response", response);
      if (response.status === 200) {
        console.log(response.data.usuario_id);
      } else {
        console.log("Error al añadir lista de la compra");
      }
    } catch (error) {
      console.log("login error", error);
    }
  };

  useEffect(() => {
    getRecetaCompleta();
    getFavorita();
  }, [idReceta, idUsuario]);

  const {
    nombre,
    ingredientes,
    tiempo_preparacion,
    preparacion,
    imagen_url,
    video_url,
  } = recetaCompleta;

  return (
    <div className="receta-completa">
      <div className="encabezado-receta">
        <div className="titulo">
          <h1>{nombre}</h1>
        </div>
        <div className="botones-receta">
          {idUsuario ? (
            <button onClick={agregarListaCompra} data-helper="Añadir a la lista de la compra">
              <FontAwesomeIcon icon={faBasketShopping} />
            </button>
          ) : null}

          {idUsuario ? (
            recetaFavorita ? (
              <button onClick={quitarFavoritos}>
                <FontAwesomeIcon icon={faStarSolid} className="favorito-activado" />
              </button>
            ) : (
              <button onClick={agregarFavoritos}>
                <FontAwesomeIcon icon={faStar} className="favorito-desactivado" />
              </button>
            )
          ) : null}
        </div>
      </div>

      <div className="tiempo-prep">
        <FontAwesomeIcon icon={faClock} className="tiempo-icono" />
        {tiempo_preparacion}
      </div>
      <div className="bloque-ing-img">
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
        <div className="imagen-receta">{imagen_url ? <img src={imagen_url} alt={nombre} /> : null}</div>
      </div>

      <div className="preparacion">
        <h3>Preparación:</h3>
        {preparacion ? <MostrarRichText html={preparacion} /> : <p>Cocinando la receta...</p>}
      </div>
      <div className="video-wrapper">
        {video_url ? (
          <div>
            <h3>Video de la receta:</h3>
            <div className="reproductor">
              <ReactPlayer
                src={video_url}
                controls={true}
                width="40%" 
                height="360px"
                autoPlay={false}
                loop={false}
                muted={false}
              >
                <h3>No se puede reproducir el video</h3>
              </ReactPlayer>
            </div>
          </div>
        ) : null}
      </div>
    </div>
  );
}