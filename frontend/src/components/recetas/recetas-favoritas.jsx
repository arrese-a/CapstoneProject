import api from "../../helpers/axios";
import React, { useState, useEffect } from "react";
import RecetaItem from "./receta-item";

export default function RecetasFavoritas(props) {
    const idUsuario = props.idUsuario;
    const [recetasFavoritas, setRecetasFavoritas] = useState([]);

    const getRecetasFavoritas = async () => {
        try {
            const response = await api.get(`/favoritas/${idUsuario}`, { withCredentials: true });
            console.log(response);
            setRecetasFavoritas(response.data);
        } catch (error) {
            console.log("Error cargando recetas favoritas", error);
        }
    };

    useEffect(() => { getRecetasFavoritas(); }, [idUsuario]);

    const recetasList = recetasFavoritas.map((receta) => <RecetaItem key={receta.id} recetaItem={receta} />);

    return (
        <div>
            {recetasList.length > 0 ? (
                <div className="recetas-favoritas">
                    <h1>¡Estas son tus recetas favoritas!</h1>
                    <div className="lista-recetas">{recetasList}</div>
                </div>
            ) : (
                <div className="sin-recetas-favoritas">
                    <h2>No tienes ningún receta favorita</h2>
                    <p>Elige alguna receta añadirla a tus favoritas</p>
                </div>
            )}
        </div>
    );
}