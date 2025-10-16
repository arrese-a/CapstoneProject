import api from "../helpers/axios";
import React, { useState, useEffect } from "react";
import imagen from "../../public/fondo-lista-compra.png";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

export default function ListaCompra(props) {
    const idUsuario = props.idUsuario;
    const [ingredientes, setIngredientes] = useState([]);

    const getListaCompra = async () => {
        try {
            const response = await api.get(`/lista-compra/obtener/${idUsuario}`);
            console.log(response);
            const ingredientesConCheck = response.data.map((ing) => ({ ...ing, checked: false }));
            setIngredientes(ingredientesConCheck);
        } catch (error) {
            console.error("Error cargando la lista de la compra", error);
        }
    };

    useEffect(() => {
        getListaCompra();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [idUsuario]);

    const checkIngrediente = (index) => {
        setIngredientes((prev) => {
            const nuevaLista = [...prev];
            nuevaLista[index] = { ...nuevaLista[index], checked: !nuevaLista[index].checked };
            nuevaLista.sort((a, b) => a.checked - b.checked);
            return nuevaLista;
        });
    };

    const eliminarIngrediente = (index) => {
        setIngredientes((prev) => prev.filter((_, i) => i !== index));
    };

    return (
        <div className="lista-compra">
            <div className="columna-izquierda">
                <h1>Lista de la compra:</h1>
                <ul>
                    {ingredientes.length > 0 ? (
                        ingredientes.map((ingrediente, index) => (
                            <div className="ingrediente" key={index}>
                                <input type="checkbox" checked={ingrediente.checked} onChange={() => checkIngrediente(index)} />
                                <span> {ingrediente.nombre}</span>
                                <span>
                                    {ingrediente.cantidad}
                                    {" "}
                                    {ingrediente.unidad} 
                                </span>
                                <button type="button" onClick={() => eliminarIngrediente(index)}>
                                    <FontAwesomeIcon icon={faTrash} />
                                </button>
                            </div>
                        ))
                    ) : (
                        <div className="sin-lista-compra">
                            <h2>No tienes ningún ingrediente en la lista de la compra</h2>
                            <p>Elige alguna receta para añadir los ingredientes que necesitas</p>
                        </div>
                    )}
                </ul>
            </div>
            <div className="columna-derecha">
                <img src={imagen} />
            </div>
        </div>
    );
}