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
import Product from "./components/Product";
import Register1 from "./components/Register1";
import Vuelos from "./components/Vuelos";

function App() {
  return (
    <Router>
            <div className="container mt-3">
                <div className="btn-group">
                    <NavLink to="/" className='btn btn-dark' activeClassName='active'>Inicio</NavLink>
                    <NavLink to="/productos" className="btn btn-dark" activeClassName="active">Vuelos</NavLink>
                    <NavLink to="/contacto" className="btn btn-dark" activeClassName="active">Contacto</NavLink>
                </div>

                <div className="btn-group">
                    <NavLink to="/iniciar-sesion" className="btn btn-dark" activeClassName="active">Iniciar Sesión</NavLink>
                    <NavLink to="/registro" className="btn btn-dark" activeClassName="active">Registrarse</NavLink>
                </div>
                <hr />
                <Routes>
                    <Route path="/contacto" element={<Contacto />} />
                    <Route path="/vuelos" element={<Vuelos />} />
                    <Route path="/iniciar-sesion" element={<Login />} />
                    <Route path="/registro" element={<Register1 />} />
                    <Route path="/productos" element={<Product />} />
                    <Route path="/"  element={<Inicio />} />
                </Routes>
            </div>
        </Router>
  );
}

export default App;
