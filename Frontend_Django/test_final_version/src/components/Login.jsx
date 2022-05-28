import React from 'react'

import styles from '../css/login.module.css';
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
      <div className={styles.App}>
        <div className={styles.main}>
            <div className={styles.p1}>
                <div className={styles.logo}>
                    <img src={imagenes.src_volatus_logo} alt="logo" className={styles.logo_main} img>
                    </img>
                </div>
                <div className={styles.cuadro}>
                    <h1>Iniciar Sesión</h1>
                    <img src={imagenes.src_user_logo} alt="logo_user" className={styles.logo_user}>
                    </img>
                </div>
            </div>
            <div className={styles.p2}>
                <div className={styles.datos1}>
                    <img src="https://content.r9cdn.net/rimg/dimg/a1/98/0d5f3612-city-10076-177d80eab0a.jpg?crop=true&width=1366&height=768&xhint=3300&yhint=1766" alt="my_pub" className= {styles.my_pub}>
                    </img>
                    <p className={styles.p_ref}>Santa Marta es una ciudad ubicada en el mar Caribe, en el departamento de Magdalena en el norte de Colombia.</p>
                </div>
                <form onSubmit={ handleLogin } className={styles.form}>
                    <label htmlFor="email" className={styles.label}>Usuario</label>
                    <input
                      type="text"
                      placeholder="example_123"
                      id="email"
                      className={styles.input}
                      name="username"
                      value={ username }
                      onChange={ handleInputChange } />
                    <label htmlFor="password" className={styles.label}>Contraseña</label>
                    <input
                      type="password"
                      placeholder="*********"
                      id="password"
                      className={styles.input}
                      name="password"
                      value={ password }
                      onChange={ handleInputChange } />
                    <a href="/" className={styles.forgot_password}>Olvide mi contraseña</a>
                    <div className={styles.button}>
                        <span className={styles.button_login}>
                            <button type="submit" className={styles.primary_button}>Confirmar</button>
                            <button className={styles.primary_button}>Volver</button>
                        </span>
                    </div>
                </form>
                <div className={styles.pub}>
                    <img src={imagenes.src_pub1} alt="pub" className={styles.img_pub}/>
                </div>
            </div>
        </div>
      </div>
    );
}

export default Login;