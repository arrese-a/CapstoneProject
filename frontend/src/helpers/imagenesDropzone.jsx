import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faImage } from "@fortawesome/free-solid-svg-icons";

function ImagenUrlInput({ onUrlSelected }) {
  const [url, setUrl] = useState("");
  const [preview, setPreview] = useState(null);

  const handleChange = (e) => {
    const value = e.target.value;
    setUrl(value);
    setPreview(value);
    onUrlSelected(value); // enviar al padre
  };

  return (
    <div
      style={{
        border: "2px dashed #ccc",
        borderRadius: "10px",
        padding: "1rem",
        textAlign: "center",
      }}
    >
      <input
        type="text"
        placeholder="Ingresa la URL de la imagen"
        value={url}
        onChange={handleChange}
        style={{
          width: "80%",
          padding: "0.5rem",
          borderRadius: "5px",
          border: "1px solid #ccc",
        }}
      />
      {preview ? (
        <img
          src={preview}
          alt="Vista previa"
          style={{ maxWidth: "200px", marginTop: "1rem", borderRadius: "10px" }}
          onError={() => setPreview(null)} // Si la URL no carga, quita la vista previa
        />
      ) : (
        <div style={{ marginTop: "1rem" }}>
          <p>Ingresa una URL para ver la vista previa</p>
          <FontAwesomeIcon icon={faImage} style={{ fontSize: "2em" }} />
        </div>
      )}
    </div>
  );
}

export default ImagenUrlInput;
