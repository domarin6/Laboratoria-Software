import { Button } from "@mui/material";
import React from "react";
import { accounting } from "accounting";
import styles from '../css/total.module.css'
import { getBasketTotal } from "./contextAPI/reducer";
import { useStateValue } from "./contextAPI/StateProvider";


export default function Total() {

    const [{basket}, dispatch] = useStateValue();

    return(
        <div className={styles.root}>
            <h5>Total Vuelos: {basket.length}</h5>
            <h5>{accounting.formatMoney(getBasketTotal(basket), "$")}</h5>
            <Button className={styles.button} variant='contained' color='secondary'>
                Pagar
            </Button>

        </div>
    )
}
