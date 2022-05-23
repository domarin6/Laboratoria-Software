import React from "react";
import imagenes from "./assets/imagenes";

function Register2(){
    return (
        <div className="Register">
            <div className="container_register_2">
                <div className="p1_register_2">
                    <img src={imagenes.src_volatus_logo} alt="logo_volatus" className="logo_main_register"/>
                    <div className="cuadro_register">
                        <h1>Crear Cuenta</h1>
                        <img src={imagenes.src_user_logo} alt="logo_user" className="logo_user_register" />
                    </div>
                </div>
                <div className="p2_register_2">
                    <div className="container_register_2">
                        <a href="/" className="text1">Contacto</a>
                        <div className="info_register">
                            <h3 className="text2">¿Como podemos contactarte?</h3>
                            <span className="form_register">
                                <label for="document" className="label">Documento</label>
                                <input type="text" id="document" className="input input-document"></input>
                            </span>
                            <span className="form_register">
                                <label for="name" className="label">Nombres</label>
                                <input type="text" id="name" className="input input-name"></input>
                            </span>
                            <span className="form_register">
                                <label for="last-name" className="label">Apellidos</label>
                                <input type="text" id="last-name" className="input input-last-name"></input>
                            </span>
                            <span className="form_register">
                                <label for="date" className="label">Fecha de Nacimiento</label>
                                <input type="date" id="date" className="input input-date"></input>
                            </span>
                            <span className="form_register">
                                <label for="last-name" className="label">Apellidos</label>
                                <input type="text" id="last-name" className="input input-name"></input>
                            </span>
                            <span className="button_login_register">
                                <button type="submit" className="button primary_button">Confirmar</button>
                                <button className="button primary_button">Volver</button>
                            </span>

                            
                        </div>
                    </div>
                </div>

            </div>
            
        </div>
    );
}
export default Register2