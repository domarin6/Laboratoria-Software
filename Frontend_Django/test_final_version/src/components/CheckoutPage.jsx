<<<<<<< HEAD
import React from 'react';
// import { makeStyles} from "@material-ui/core/styles";
=======
<<<<<<< HEAD
import React from 'react';
import { makeStyles } from '@mui/material/styles';
import Grid from "@material-ui/cor/Grid";
import Typography from '@mui/material/Typography';
import CheckoutCard from "./CheckoutCard";
import products from "../components/Functions/info-product"

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        padding: "2rem",
    },
}));
=======
// import React from 'react';
// // import { makeStyles} from "@material-ui/core/styles";
>>>>>>> f2c7ee016732521b2adbf436b429ada5baf3b733
// import { makeStyles } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
// import { Typography } from '@mui/material/Typography';
import Typography from '@mui/material/Typography';
import CheckoutCard from "./CheckoutCard";
import products from "../components/Functions/info-product";
import styles from '../css/checkoutPage.module.css'
import Total from './Total';

// const useStyles = makeStyles((theme) => ({
//     root: {
//         flexGrow: 1,
//         padding: "2rem",
//     },
// }));
>>>>>>> 1e58c5d9caa8e7f6c4d72f661477be7de7a457bb

const CheckoutPage = () => {
    // const classes = useStyles();

    function FormRow() {
        return (
            <React.Fragment>
                {products.map((item) => (
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
                        Total
                    </Typography>
                </Grid>
            </Grid>
        </div>
    );
};

export default CheckoutPage;