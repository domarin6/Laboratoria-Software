import React from "react";
import {
    BrowserRouter as Router,
    Route,
    // Link,
    Routes,
    NavLink
} from "react-router-dom";
import Contacto from "./components/Contacto";
import Inicio from "./components/Inicio";
import Login from "./components/Login";
import Manage_ADM from "./components/Manage_ADM";
import NavBar from "./components/NavBar";
import Product from "./components/Product";
import Products from "./components/Products";
import Register1 from "./components/Register1";
import CheckoutPage from "./components/CheckoutPage";

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

        <div className="App">
            <NavBar/>
            <CheckoutPage />
            {/* <Products/> */}

            {/* <Router>
                <div className="container mt-3">
                    <div className="btn-group">
                        <NavLink to="/" className='btn btn-dark' >Inicio</NavLink>
                        <NavLink to="/productos" className="btn btn-dark" >Vuelos</NavLink>
                        <NavLink to="/contacto" className="btn btn-dark" >Contacto</NavLink>
                    </div>

                    <div className="btn-group">
                        <NavLink to="/gestionar-adm" className='btn btn-dark' > Gestionar Admin </NavLink>
                    </div>

                    <div className="btn-group">
                        <NavLink to="/iniciar-sesion" className="btn btn-dark" >Iniciar Sesión</NavLink>
                        <NavLink to="/registro" className="btn btn-dark" >Registrarse</NavLink>
                    </div>


                    <IconButton aria-label="show cart items" color='inherit'>
                        <Badge badgeContent={2} color='secondary'>
                            <ShoppingCart fontSize="large" color="primary"/>
                        </Badge>
                    </IconButton>
                    
                    <hr />
                    <Routes>
                        <Route path="/contacto" element={<Contacto />} />
                        <Route path="/iniciar-sesion" element={<Login />} />
                        <Route path="/registro" element={<Register1 />} />
                        <Route path="/productos" element={<Products/>} />
                        <Route path="/gestionar-adm" element={<Manage_ADM />} />
                        <Route path="/"  element={<Inicio />} />
                    </Routes>
                </div>
            </Router> */}

        </div>
      
        
  );
}

export default App;