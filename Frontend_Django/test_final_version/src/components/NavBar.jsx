import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import Badge from '@mui/material/Badge';
import logo from '../components/assets/img/volatus_logo_removebg.png';
import styles from '../css/nav.module.css';
import { ShoppingCart } from '@mui/icons-material';
import { Link } from 'react-router-dom';


export default function NavBar() {
  
  return (
    <Box sx={{ flexGrow: 5 }} className={styles.root}>
      <AppBar position="static" className={styles.cuadro}>
        <Toolbar>

          <Link to="/">
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
            >
              <img src={logo} className={styles.image} alt="logo_volatus" />
            </IconButton>
          </Link>

          <Typography variant="h6" color="textPrimary" component="p" sx={{ flexGrow: 1 }}>
            Hola Invitado
          </Typography>
          <div className={styles.grow}/>

          <Link to="/vuelos">
            <Button color="inherit" variant='outlined'> <strong>Vuelos</strong></Button>
          </Link>

          <div className={styles.button}>
            <Button variant='outlined' color='inherit'>Crear Cuenta</Button>
          </div>

          <Button color="inherit" variant='outlined'>Iniciar Sesión</Button>
          
          
          <Link to="/checkout-page">
            <IconButton aria-label='mostrar items del carrito' color='inherit'>
              <Badge badgeContent={2} color='secondary'>
                <ShoppingCart fontSize='large'/>  
              </Badge>
            </IconButton>
          </Link>
        
        </Toolbar>
      </AppBar>
    </Box>
  );
}
