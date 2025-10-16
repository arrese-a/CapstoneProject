import { useLocation } from "react-router-dom";
import App from "../app";

export default function AppWrapper() {
  const location = useLocation();
  return <App currentPath={location.pathname} />;
}
