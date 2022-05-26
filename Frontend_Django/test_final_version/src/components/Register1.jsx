import React from "react";
import imagenes from "./assets/imagenes";
import styles from  '../css/createUser.module.css'

function Register1(){
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
                <a href="./registro" className={styles.text1}>¿Quien eres?</a>
                <div className={styles.p2}>
                    <div className={styles.info}>
                        <h3 className={styles.text2}>¿Quien eres?</h3>
                        <span className={styles.form}>
                            <label for="document" className={styles.label}>Documento</label>
                            <input type="text" id="document" className={styles.input}></input>
                        </span>
                        <span className={styles.form}>
                            <label for="name" className={styles.label}>Nombres</label>
                            <input type="text" id="name" className={styles.input}></input>
                        </span>
                        <span className={styles.form}>
                            <label for="last-name" className={styles.label}>Apellidos</label>
                            <input type="text" id="last-name" className={styles.input}></input>
                        </span>
                        <span className={styles.form}>
                            <label for="date" className={styles.label}>Fecha de Nacimiento</label>
                            <input type="date" id="date" className={styles.input}></input>
                        </span>
                        <span className={styles.form}>
                            <label for="last-name" className={styles.label}>Genero</label>
                            <input type="text" id="last-name" className={styles.input}></input>
                        </span>
                        <span className={styles.buttonLogin}>
                            <button type="submit" className={styles.primaryButton}>Confirmar</button>
                            <button className={styles.primaryButton}>Volver</button>
                        </span>
                    </div>
                </div>
            </div>
            
        </div>
    );
}
export default Register1