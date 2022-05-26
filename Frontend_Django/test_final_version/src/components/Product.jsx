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
import { AddShoppingCart } from '@mui/icons-material'

import imagenes from './assets/imagenes';

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
}));

export default function RecipeReviewCard() {
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardHeader
        // avatar={
        //   <Avatar sx={{ bgcolor: red[500] }} aria-label="recipe">
        //     R
        //   </Avatar>
        // }
        action={
            <Typography className={ClassNames.action} variant='h5' color='textSecondary'>{'$850.000'}</Typography>
        }
        title="San Andres"
        subheader="Islas paradisiacas de Colombia"
      />
      <CardMedia
        component="img"
        height="194"
        // image={imagenes.src_pub1}
        image = 'https://i.ytimg.com/vi/vPJS2moVUFA/maxresdefault.jpg'
        alt="Paella dish"
      />
      <CardContent>
        <Typography variant="body2" color="text.secondary">
            San Andrés es una isla colombiana del mar Caribe, frente a la costa de Nicaragua. Es conocida por los arrecifes de coral y la música reggae.
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        <IconButton aria-label="add to shopping card">
          <AddShoppingCart />
        </IconButton>
        <IconButton>
            {Array(4)
              .fill()
              .map((_, i) => (
                  <p>&#11088;</p>
              ))
            }
        </IconButton>

        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          <Typography paragraph>Method:</Typography>
          <Typography paragraph>
            Nothing
          </Typography>
          <Typography paragraph>
            La encendida playa Spratt Bight tiene un paseo costero bordeado de palmeras. En el litoral está el Parque Johnny Cay, una pequeña isla con mangles de cocos y playas de arena blanca. El Parque Regional de Mangle Old Point es un santuario de vida silvestre con cangrejos, iguanas y aves.
          </Typography>
        </CardContent>
      </Collapse>
    </Card>
  );
}
