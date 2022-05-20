import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Link,
    Routes,
    NavLink
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
                    <NavLink to="/vuelos" className="btn btn-dark" activeClassName="active">Vuelos</NavLink>
                    <NavLink to="/contacto" className="btn btn-dark" activeClassName="active">Contacto</NavLink>
                </div>

                <div className="btn-group">
                    <NavLink to="/iniciar-sesion" className="btn btn-dark" activeClassName="active">Login</NavLink>
                    <NavLink to="/registro" className="btn btn-dark" activeClassName="active">Register</NavLink>
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
