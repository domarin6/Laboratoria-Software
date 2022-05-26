import React from 'react'
import { Link } from 'react-router-dom'

import '../css/crud_root.css';
import imagenes from './assets/imagenes';

function ManageAdmin() {
  return(
    <div className="main_root">
        <div className="p1">
            <div className="logo">
                <img src={imagenes.src_volatus_logo} alt="logo_main" className="logo_main img" />
            </div>
            <div className="cuadro">
                <h1>Gestionar Administrador</h1>
                <img src={imagenes.src_adm_logo} alt="logo_user" className="img logo_user" />
            </div>
        </div>
        <div className="p2_root">
            <span><Link to="/gestionar-admin/create" className="link_root">Crear</Link> </span>
            <span><Link to="/backend/volatus/Frontend/modificar_adm.html" className="link_root">Editar</Link></span>
            <span><Link to="/backend/volatus/Frontend/eliminar_adm.html" className="link_root">Eliminar</Link></span>
        </div>

        <div className="p3_root">
            <p>Otro cuadro xD</p>
        </div>
    </div>
  );
}

export default ManageAdmin;
