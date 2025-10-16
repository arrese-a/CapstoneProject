import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../helpers/axios";
import RichTextEditor from "../../helpers/rich-tx-editor";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlusCircle, faCircleMinus, faImage } from "@fortawesome/free-solid-svg-icons";

export default function RecetaCrear(props) {
  const [titulo, setTitulo] = useState("");
  const [ingredientes, setIngredientes] = useState([{ nombre: "", cantidad: "", unidad: "" }]);
  const [tiempoPreparacion, setTiempoPreparacion] = useState("");
  const [preparacion, setPreparacion] = useState("");
  const [imagenUrl, setImagenUrl] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (event) => {
    const { name, value } = event.target;
    if (name === "titulo") setTitulo(value);
    else if (name === "tiempo_preparacion") setTiempoPreparacion(value);
    else if (name === "video_url") setVideoUrl(value);
    else if (name === "imagen_url") setImagenUrl(value);
  };

  const agregarIngrediente = () => {
    setIngredientes((prev) => [...prev, { nombre: "", cantidad: "", unidad: "" }]);
  };

  const eliminarIngrediente = (index) => {
    setIngredientes((prev) => prev.filter((_, i) => i !== index));
  };

  const handleIngredienteChange = (index, event) => {
    const { name, value } = event.target;
    setIngredientes((prev) => {
      const copia = [...prev];
      copia[index] = { ...copia[index], [name]: value };
      return copia;
    });
  };

  const handleSubmit = async () => {
    setError("");
    try {
      const response = await api.post(
        `/recetas`,
        {
          nombre: titulo,
          preparacion: preparacion,
          tiempo_preparacion: tiempoPreparacion,
          video_url: videoUrl || "",
          ingredientes: ingredientes,
          imagen_url: imagenUrl || "",
        },
        {
          withCredentials: true,
          headers: { "Content-Type": "application/json" },
        }
      );
        navigate("/recetas");
    } catch (error) {
      setError("Parece que falta algún campo por rellenar, por favor rellena todos los campos necesarios");
    }
  };

  const handleRichTextEditorChange = (content) => {
    setPreparacion(content);
  };

  return (
    <div className="crear-wrapper">
      <div className="titulo-pagina">
        <h1>Crea tu receta</h1>
      </div>
      <form className="crear-receta-form" onSubmit={(e) => e.preventDefault()}>
        <div className="form-content">
          <div className="dos-columnas bloque">
            <div className="campo">
              <h3>Título de la receta <span style={{ color: 'darkred' }}>*</span></h3>
              <input type="text" name="titulo" placeholder="Título de la receta" value={titulo} onChange={handleChange} required />
            </div>
            <div className="campo">
              <h3>Tiempo receta <span style={{ color: 'darkred' }}>*</span></h3>
              <input type="text" name="tiempo_preparacion" placeholder="ej: 1h" value={tiempoPreparacion} onChange={handleChange} required />
            </div>
          </div>
          <div className="section-divider"></div>

          <div className="campo bloque">
            <h3>Ingredientes <span style={{ color: 'darkred' }}>*</span></h3>
            <div id="ingredientes-lista">
              {Array.isArray(ingredientes) &&
                ingredientes.map((ingrediente, index) => (
                  <div className="tres-columnas" key={index}>
                    <input type="text" name="nombre" placeholder="Nombre" value={ingrediente.nombre} onChange={(e) => handleIngredienteChange(index, e)} required />
                    <input type="number" name="cantidad" placeholder="Cantidad" value={ingrediente.cantidad} onChange={(e) => handleIngredienteChange(index, e)} required />
                    <input type="text" name="unidad" placeholder="Ud (ej: gr)" value={ingrediente.unidad} onChange={(e) => handleIngredienteChange(index, e)} />

                    {ingredientes.length > 1 && (
                      <button type="button" onClick={() => eliminarIngrediente(index)}>
                        <FontAwesomeIcon icon={faCircleMinus} />
                      </button>
                    )}
                  </div>
                ))}
            </div>

            <button type="button" onClick={agregarIngrediente} className="agregar-ingrediente">
              <FontAwesomeIcon icon={faPlusCircle} />
            </button>
          </div>
          <div className="section-divider"></div>
          <div className="dos-columnas bloque">
            <div className="campo-url-video">
              <h3>Url video receta</h3>
              <input type="url" name="video_url" placeholder="video_url" value={videoUrl} onChange={handleChange} />
            </div>
            <div className="campo-url-imagen">
              <h3>Url imagen receta</h3>
              <input type="url" name="imagen_url" placeholder="imagen_url" value={imagenUrl} onChange={handleChange} />
            </div>
          </div>
          <div className="section-divider"></div>

          <div className="campo-preparacion una-columna bloque">
            <h3>Preparación de la receta <span style={{ color: 'darkred' }}>*</span></h3>
            <RichTextEditor value={preparacion} onChange={(content) => handleRichTextEditorChange(content)} />
          </div>

          <button type="button" onClick={handleSubmit} className="btn-guardar">
            Guardar
          </button>
          {error && <p className="error-msg">{error}</p>}

        </div>
      </form>
    </div>
  );
}