import React from 'react'
// import styles from '../css/crudRoot.module.css'
import imagenes from './assets/imagenes';

function Manage_ADM(){
    
    return (
        <div className="Manage_ADM">
            <div className="main_root">
                <div className="p1">
                    <div className="logo">
                        <img src={imagenes.src_volatus_logo} alt="logo_main" className="logo_main img"/>
                    </div>
                    <div className="cuadro">
                        <h1 >Gestionar Administrador</h1>
                        <img src={imagenes.src_adm_logo} alt="logo_user" className="img logo_user"/>
                    </div>
                </div>
                <div className="p2_root">
                    <span><a href="/backend/volatus/Frontend/crear_adm.html" className="link_root">Crear</a> </span>
                    <span><a href="/backend/volatus/Frontend/modificar_adm.html" className="link_root">Editar</a></span>
                    <span><a href="/backend/volatus/Frontend/eliminar_adm.html" className="link_root">Eliminar</a></span>
                </div>

                <div class="p3_root">
                    <p>Otro cuadro xD</p>
                </div>
            </div>

        </div>
      );

}

export default Manage_ADM;

