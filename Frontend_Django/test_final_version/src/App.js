import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Link,
    Routes
} from "react-router-dom";
import Contacto from "./components/Contacto";
import Inicio from "./components/Inicio";
import Login from "./components/Login";
import Register from "./components/Register";
import Vuelos from "./components/Vuelos";

function App() {
  return (
    <Router>
            <div className="container mt-3">
                <div className="btn-group">
                    <Link to="/vuelos" className="btn btn-dark">Vuelos</Link>
                    <Link to="/contacto" className="btn btn-outline-dark">Contacto</Link>
                </div>

                <div className="btn-group">
                    <Link to="/iniciar-sesion" className="btn btn-outline-dark">Login</Link>
                    <Link to="/registro" className="btn btn-outline-dark">Register</Link>
                </div>
                <hr />
                <Routes>
                    <Route path="/contacto" element={<Contacto />} />
                    <Route path="/vuelos" element={<Vuelos />} />
                    <Route path="/iniciar-sesion" element={<Login />} />
                    <Route path="/registro" element={<Register />} />
                    <Route path="/"  element={<Inicio />} />
                </Routes>
            </div>
        </Router>
  );
}

export default App;
