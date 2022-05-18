// import React from "react";

// const Login = () => {
//     return (
//         <div>
//             login
//         </div>
//     );
// }
// export default Login

//import LoginScreen from '../functions/LoginScreen'

import React from 'react'

import '../css/iniciar_sesion.css';
import imagenes from './assets/imagenes';

import { useForm } from './hooks/useForm';
import { startLogin } from './Functions/loginFunction';


function Login() {
  const [ formValues, handleInputChange ] = useForm({
        username: '',
        password: ''
    });

    const { username, password } = formValues;

    const handleLogin = (e) =>{
        e.preventDefault();
        startLogin( username , password );
    }

    return (
      <div className="App">
        <div className="main">
            <div className="p1">
                <div className="logo">
                    <img src={imagenes.src_volatus_logo} className="logo_main img">
                    </img>
                </div>
                <div className="cuadro">
                    <h1>Iniciar Sesión</h1>
                    <img src={imagenes.src_user_logo} alt="logo_user" className="img logo_user">
                    </img>
                </div>
            </div>
            <div className="p2">
                <div className="datos1">
                    <img src={imagenes.src_ref} alt="my_pub" className="img my_pub">
                    </img>
                    <p className="p_ref">Texto de referencia sobre algún producto.</p>
                </div>
                <form onSubmit={ handleLogin } className="form">
                    <label htmlFor="email" className="label">Usuario</label>
                    <input
                      type="text"
                      placeholder="example_123"
                      id="email"
                      className="input input-user"
                      name="username"
                      value={ username }
                      onChange={ handleInputChange } />
                    <label htmlFor="password" className="label">Contraseña</label>
                    <input
                      type="password"
                      placeholder="*********"
                      id="password"
                      className="input input-password"
                      name="password"
                      value={ password }
                      onChange={ handleInputChange } />
                    <a href="/" className="forgot_password">Olvide mi contraseña</a>
                    <div className="button">
                        <span className="button_login">
                            <button type="submit" className="button primary_button">Confirmar</button>
                            <button className="button primary_button">Volver</button>
                        </span>
                    </div>
                </form>
                <div className="pub">
                    <img src={imagenes.src_pub1} alt="pub" className="img_pub">
                    </img>
                </div>
            </div>
        </div>
      </div>
    );
}

export default Login;