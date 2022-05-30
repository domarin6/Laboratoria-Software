import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Routes
} from "react-router-dom";
import Inicio from "./components/Inicio";
import NavBar from "./components/NavBar";
import Products from "./components/Products";
import CheckoutPage from "./components/CheckoutPage";
import SignInSide from "./components/SignIn";
import SignUp from "./components/SignUp";

// import Contacto from "./components/Contacto";
// import Login from "./components/Login";
// import Manage_ADM from "./components/Manage_ADM";
// import Product from "./components/Product";
// import Register1 from "./components/Register1";

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
                    <Route path="/signin" element={<SignInSide/>} />
                    <Route path="/signup" element={<SignUp/> } />
                    <Route path="/checkout-page" element={<CheckoutPage/>}/>
                    <Route path="/vuelos" element={<Products/>}/>
                    <Route path="/" element={<Inicio/>}/>
                </Routes>               
            </div>
        </Router>        
  );
}

export default App;