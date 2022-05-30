import * as React from 'react';
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { red } from '@mui/material/colors';
import ShareIcon from '@mui/icons-material/Share';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { ClassNames } from '@emotion/react';
import imagenes from './assets/imagenes';
import accounting from 'accounting';
import styles from '../css/checkoutCard.module.css'
import DeleteIcon from '@mui/icons-material/Delete';

// const ExpandMore = styled((props) => {
//   const { expand, ...other } = props;
//   return <IconButton {...other} />;
// })(({ theme, expand }) => ({
//   transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
//   marginLeft: 'auto',
//   transition: theme.transitions.create('transform', {
//     duration: theme.transitions.duration.shortest,
//   }),
// }));

export default function CheckoutCard({product:{id, img, destination, rating, price, description, full_description} }) {


  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardHeader
        // avatar={
        //   <Avatar sx={{ bgcolor: red[500] }} aria-label="recipe">
        //     R
        //   </Avatar>
        // }
        action={
            <Typography className={ClassNames.action} variant='h5' color='textSecondary'>{price}</Typography>
        }
        title={destination}
        subheader="TEXTO DE EJEMPLO"
      />
      <CardMedia
        component="img"
        height="194"
        // image={imagenes.src_pub1}
        image = {img}
        alt="Destino"
      />
      
      <CardActions disableSpacing className={styles.cardActions}>
        
        <div className={styles.cardRating}>
            {Array(rating)
              .fill()
              .map((_, i) => (
                  <p>&#11088;</p>
              ))
            }
        </div>
        <IconButton>
            <DeleteIcon/>
        </IconButton>
        
      </CardActions>
    </Card>
  );
}
