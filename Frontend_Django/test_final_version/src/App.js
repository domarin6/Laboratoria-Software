import { ShoppingCart } from "@mui/icons-material";
import { IconButton } from "@mui/material";
import Badge from '@mui/material/Badge';

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
import Manage_ADM from "./components/Manage_ADM";
// import Product from "./components/Product";
import Products from "./components/Products";
import Register1 from "./components/Register1";
import Vuelos from "./components/Vuelos";
// import CheckoutPage from "./components/CheckoutPage";

// const useStyles = makeStyles((theme) =>({
//     root: {
//         flexGrow:1,
//     },
//     grow: {
//         flexGrow:1,
//     }
// }));

function App() {
//   const classes = useStyles;
  return (
    <Router>
            <div className="container mt-3">
                <div className="btn-group">
                    <NavLink to="/" className='btn btn-dark' activeClassName='active'>Inicio</NavLink>
                    <NavLink to="/productos" className="btn btn-dark" activeClassName="active">Vuelos</NavLink>
                    <NavLink to="/contacto" className="btn btn-dark" activeClassName="active">Contacto</NavLink>
                </div>

                <div className="btn-group">
                    <NavLink to="/gestionar-adm" className='btn btn-dark' activeClassName='active'> Gestionar Admin </NavLink>
                </div>

                <div className="btn-group">
                    <NavLink to="/iniciar-sesion" className="btn btn-dark" activeClassName="active">Iniciar Sesión</NavLink>
                    <NavLink to="/registro" className="btn btn-dark" activeClassName="active">Registrarse</NavLink>
                </div>

                <IconButton aria-label="show cart items" color='inherit'>
                    <Badge badgeContent={2} color='secondary'>
                        <ShoppingCart fontSize="large" color="primary"/>
                        {/* <CheckoutPage/> */}

                    </Badge>
                </IconButton>
                
                <hr />
                <Routes>
                    <Route path="/contacto" element={<Contacto />} />
                    <Route path="/vuelos" element={<Vuelos />} />
                    <Route path="/iniciar-sesion" element={<Login />} />
                    <Route path="/registro" element={<Register1 />} />
                    {/* <Route path="/productos" element={<Product />} /> */}
                    <Route path="/productos" element={<Products/>} />
                    <Route path="/gestionar-adm" element={<Manage_ADM />} />
                    <Route path="/"  element={<Inicio />} />
                </Routes>
            </div>
        </Router>
  );
}

export default App;