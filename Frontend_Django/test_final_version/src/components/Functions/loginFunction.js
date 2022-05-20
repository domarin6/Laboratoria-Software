
import { notification, timerNotification } from "./alert";
import { fetchWithoutToken, fetchWithToken } from "./fetch";


export const startLogin = async (username, password) => {
  console.log("hola")
  const response = await fetchWithoutToken(
                          'crudRoot/Login/',
                          { username, password },
                          'POST'
                      );
  const body = await response.json();


  if ( response.status === 200 ||  response.status === 201 ){

      // set user info
      localStorage.setItem('token',body.token);
      localStorage.setItem('username',body.user.username);
      localStorage.setItem('DNI',body.user.DNI);
      localStorage.setItem('name',body.user.nombre);

      timerNotification( 'Inicio de Sesion Exitoso!' );
      window.location.href="./gestionar-admin";

  }else{
      notification( 'ERROR',body.error,'error' );
  }
}
