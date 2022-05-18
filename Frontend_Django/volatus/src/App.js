import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Link,
    Routes
} from "react-router-dom";

function App(){

    return(
        // <div>
        //     <h1>titulo....?</h1>
        // </div>
        <Router>
            <div className="container">
                <h1>Prueba....</h1>
                <hr />
                <Routes>
                    <Route path="/contacto">
                        Que pasa aqui....
                    </Route>
                    <Route path="/vuelos"></Route>
                    <Route path="/iniciar-sesion"></Route>
                    <Route path="/"></Route>
                </Routes>
            </div>
        </Router>
    );

}

export default App;