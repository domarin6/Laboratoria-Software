import React from 'react';
import Typography from '@mui/material/Typography';
import CheckoutCard from "./CheckoutCard";
import Grid from '@mui/material/Grid';
import styles from '../css/checkoutPage.module.css';
import Total from '../components/Total'
import { useStateValue } from '../components/contextAPI/StateProvider'


const CheckoutPage = () => {

    const [{basket}, dispatch] = useStateValue();

    function FormRow() {
        return (
            <React.Fragment>
                {basket.map((item) => (
                    <Grid item xs={12} sm={8} md={6} lg={4}>
                        <CheckoutCard key={item.id} product={item} />
                    </Grid>
                ))}
            </React.Fragment>
        );
    }

    return (
        <div className={styles.root}>
            <Grid container spacing={3}>
                <Grid item xs={12}>
                    <Typography align='center' gutterBottom variant='h4'>
                        Carrito de compra
                    </Typography>
                </Grid>
                <Grid item xs={12} sm={8} md={9} container spacing={2}>
                    <FormRow />
                </Grid>
                <Grid item xs={12} sm={4} md={3}>
                    <Typography align='center' gutterBottom variant='h4'>
                        <Total/>
                    </Typography>
                </Grid>                
            </Grid>
        </div>
    );
};

export default CheckoutPage;