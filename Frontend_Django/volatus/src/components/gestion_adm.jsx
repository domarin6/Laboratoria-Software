//import LoginScreen from '../functions/LoginScreen'

import React from 'react';
import { Link } from "react-router-dom";
import { useDispatch } from 'react-redux';

import { useForm } from '../../hooks/useForm';
import { startLogin } from '../../actions/auth';

import '../css/iniciar_sesion.css';
import imagenes from './assets/imagenes';

function Login() {

  const dispatch = useDispatch();

  const [ formValues, handleInputChange ] = useForm({
      username: '',
      password: ''
  });

    const { username, password } = formValues;

    const handleLogin = (e) =>{
        e.preventDefault();
        dispatch( startLogin( username , password ) );
    }

    return (
      <div className="App">
        
        
      </div>
    );
}

export default Login;