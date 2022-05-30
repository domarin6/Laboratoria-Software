import { Button } from "bootstrap";
import React from "react";
import styles from '../css/total.module.css'


export default function Total() {
    return(
        <div className={styles.root}>
            <h5>Total Items: 3</h5>
            <h5>$120.000</h5>
            <Button className={styles.button} variant='contained' color='secondary'>
                Cerrar Sesión 
            </Button>

        </div>
    )
}
