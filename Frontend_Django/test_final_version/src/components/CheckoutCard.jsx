import * as React from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardActions from '@mui/material/CardActions';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { ClassNames } from '@emotion/react';
import styles from '../css/checkoutCard.module.css'
import DeleteIcon from '@mui/icons-material/Delete';
import { actionTypes } from './contextAPI/reducer';
import { useStateValue } from '../components/contextAPI/StateProvider';
import accounting from 'accounting';


export default function CheckoutCard({product:{id, img, destination, rating, price, description, full_description} }) {

  const [{basket}, dispatch] = useStateValue();

  const removeItem = () => dispatch({
    type: actionTypes.REMOVE_ITEM,
    id:id,
  })

  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardHeader
        action={
            <Typography className={ClassNames.action} variant='h5' color='textSecondary'>{accounting.formatMoney(price,"$", 0)}</Typography>
        }
        title={destination}
        subheader="DESTINO"
      />
      <CardMedia
        component="img"
        height="194"
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
        <IconButton fontSize='large' onClick={removeItem}>
            <DeleteIcon/>
        </IconButton>
        
      </CardActions>
    </Card>
  );
}
