import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Product from "../components/Product"
import products from "../components/Functions/info-product"

const Item = styled(Paper)(({ theme }) => ({
  root:{
      flexGrow:1,
      padding: theme.spacing(3),
  },


  
}));

export default function Products() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={2}>

          {
              products.map(product =>(
                <Grid item xs={12} sm={6} md={4} lg={3}>
                    <Product key={product.id} product={product}/>
                </Grid>
              ))
          }
      </Grid>
    </Box>
  );
}
