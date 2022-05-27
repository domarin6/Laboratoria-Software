import React from "react";
import imagenes from "./assets/imagenes";
import styles from  '../css/createUser.module.css'
import { useForm } from './hooks/useForm';
import { startRegister } from './Functions/registerFunction'

function Register1(){

    const [ formValues, handleInputChange ] = useForm({
        id: '',
        name: '',
        lastName:'',
        birthDate:'',
        genre:'',
        tel:'',
        userName:'',
        password:''
    });

    const { id, name, lastName, birthDate, genre, tel, userName, password } = formValues;

    const handleRegister = (e) =>{
        e.preventDefault();
        startRegister( id , name, lastName, birthDate, genre, tel, userName, password );
    }


    return (
        <div className={styles.register}>

            <div className={styles.container1}>
                <img src={imagenes.src_volatus_logo} alt="logo_volatus" className={styles.logoMain}/>
                <div className={styles.cuadro}>
                    <h1>Crear Cuenta</h1>
                    <img src={imagenes.src_user_logo} alt="logo_user" className={styles.logoUser} />
                </div>
            </div>


            <div className={styles.container2}>
                <div className={styles.info}>
                            
                    <form onSubmit={ handleRegister } className={styles.form}>
                        <h3 className={styles.text1}>¿Quien eres?</h3>
                        <div className={ styles.parte1}>
                            <span className={styles.form}>
                                <label for="document" className={styles.label}>Documento</label>
                                <input type="text" id="document" className={styles.input} value={ id } onChange={ handleInputChange }></input>
                            </span>
                            <span className={styles.form}>
                                <label for="name" className={styles.label}>Nombres</label>
                                <input type="text" id="name" className={styles.input}value={ name } onChange={ handleInputChange }></input>
                            </span>
                            <span className={styles.form}>
                                <label for="last-name" className={styles.label}>Apellidos</label>
                                <input type="text" id="last-name" className={styles.input} value={ lastName } onChange={ handleInputChange }></input>
                            </span>
                            <span className={styles.form}>
                                <label for="date" className={styles.label}>Fecha de Nacimiento</label>
                                <input type="date" id="date" className={styles.input}value={ birthDate } onChange={ handleInputChange }></input>
                            </span>
                            <span className={styles.form}>
                                <label for="last-name" className={styles.label}>Genero</label>
                                <input type="text" id="last-name" className={styles.input} value={ genre } onChange={ handleInputChange }></input>
                            </span>
                        </div>

                        <div className={styles.parte2}>
                            <h1 className="text2">¿Como podemos contactarte?</h1>
                            <span className={styles.form}>
                                <label for="tel" className={styles.label}>Teléfono</label>
                                <input type="text" id="tel" className={styles.input} value={ tel } onChange={ handleInputChange }></input>
                            </span>
                        </div>

                        <div className={styles.parte3}>
                        
                            <span className={styles.form}>
                                <label for="username" className={styles.label}>Nombre de Usuario: </label>
                                <input type="text" id="username" className={styles.input} value={ userName } onChange={ handleInputChange }></input>
                            </span>

                            <span className={styles.form}>
                                <label for="password" className={styles.label}>Contraseña</label>
                                <input type="password" id="password" className={styles.input} value={ password } onChange={ handleInputChange }></input>
                            </span>
                                                        
                        </div>                          
                        


                    </form>
                    
                    <span className={styles.buttonLogin}>
                        <button type="submit" className={styles.primaryButton}>Confirmar</button>
                        <button className={styles.primaryButton}>Volver</button>
                    </span>
                </div>
            </div>
        </div>
    );
}
export default Register1