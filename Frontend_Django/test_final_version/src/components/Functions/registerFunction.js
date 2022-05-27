
import { notification, timerNotification } from "./alert";
import { fetchWithoutToken, fetchWithToken } from "./fetch";


export const startRegister = async (id, name, lastName, birthDate, genre, tel, userName, password) => {
  
  const create = "";

  const response = await fetchWithoutToken(
                          'crudRoot/cliente',
                          { id, name, lastName, birthDate, genre, tel, userName, password, create },
                          'POST'
                      );
  const body = await response.json();


  if ( response.status === 200 ||  response.status === 201 ){

      timerNotification( 'Creación Exitosa!' );
      window.location.href="./inicio";

  }else{
      notification( 'ERROR',body.error,'error' );
  }
}
