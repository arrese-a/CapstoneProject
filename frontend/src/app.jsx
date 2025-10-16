import React, { useContext } from "react";
import { Routes, Route } from "react-router-dom";
import NavigationBar from "./components/navigation-bar";
import Home from "./home";
import Recetas from "./components/recetas-container";
import RecetaCompleta from "./components/recetas/receta-completa";
import NoEncontrado from "./helpers/no-encontrado";
import ListaCompra from "./components/lista_compra";
import LoginUsuario from "./components/auth/login";
import SignUpUsuario from "./components/auth/signup";
import RecetaCrear from "./components/recetas/receta-crear";
import RecetasFavoritas from "./components/recetas/recetas-favoritas";
import { AuthContext } from "./components/auth/auth";

export default function App() {
  const { user, logout, loading, loggedInStatus } = useContext(AuthContext);

  const userId = user ? user.user : null;

  return (
    <div className="base">
      <NavigationBar loggedInStatus={loggedInStatus} idUsuario={user} handleSuccessfulLogout={logout} />
      <Routes>
        <Route path="/" element={<Home loggedInStatus={loggedInStatus} />} />
        <Route path="/login" element={<LoginUsuario />} />
        <Route path="/signup" element={<SignUpUsuario />} />
        <Route path="/recetas" element={<Recetas loggedInStatus={loggedInStatus} />} />
        <Route path="/r/:slug" element={<RecetaCompleta idUsuario={userId} />} />
        {user && (
          <>
            <Route path="/lista-compra" element={<ListaCompra idUsuario={userId} />} />
            <Route path="/crear-receta" element={<RecetaCrear />} />
            <Route path="/recetas-favoritas" element={<RecetasFavoritas idUsuario={userId} />} />
          </>
        )}
        <Route path="*" element={<NoEncontrado />} />
      </Routes>
    </div>
  );
}