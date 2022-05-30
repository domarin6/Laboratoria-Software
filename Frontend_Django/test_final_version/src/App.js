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
        <Router>
            <NavBar/>
            <div className="App">
                <Routes>
                    <Route path="/checkout-page" element={<CheckoutPage/>}/>
                    <Route path="/vuelos" element={<Products/>}/>
                    <Route path="/" element={<Inicio/>}/>
                </Routes>               
            </div>
        </Router>        
  );
}

export default App;