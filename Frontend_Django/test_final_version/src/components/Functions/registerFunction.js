
import { notification, timerNotification } from "./alert";
import { fetchWithoutToken, fetchWithToken } from "./fetch";
import {Link} from 'react-router-dom';


export const startRegister = async ( DNI, nombre, apellido, correo_electronico, username, password) => {
  
  const imagen_de_usuario = "";

  const response = await fetchWithoutToken(
                          'crudRoot/administradores-list/',
                          {DNI, nombre, apellido, correo_electronico, username, password, imagen_de_usuario},
                          'POST'
                      );
  const body = await response.json();


  if ( response.status === 200 ||  response.status === 201 ){

      timerNotification( 'Creación Exitosa!' );
      window.location.href="/signin";
  }else{
      notification( 'ERROR',body.error,'error' );
  }
}
