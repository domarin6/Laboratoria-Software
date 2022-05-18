import React from 'react'

import { notification } from "./alert";
import { fetchWithToken } from './fetch';

export const createAdminFunction = async ( { DNI, username, name, password } ) => {

  const response = await fetchWithToken(
                              'crudRoot/administradores-list/',
                              { DNI, username, name, password },
                              'POST' );
  const body = await response.json();


  if ( response.status === 201 ){
      notification("Felicidades",body.message,'success');

  }else{
      notification("ERROR",body.error.description,'error');
  }
}
