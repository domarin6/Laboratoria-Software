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
// import styles from '../css/barraNavegacion.module.css';
import { ShoppingCart, WindowSharp } from '@mui/icons-material';
import { Link } from 'react-router-dom';
import { useStateValue } from '../components/contextAPI/StateProvider'



export default function NavBar() {

  const [{ basket }, dispatch] = useStateValue();
  let saludo;
  let mostrarBoton = false;
  if (sessionStorage.getItem("name")) {
    saludo = <Typography color="textPrimary" style={{font:"oblique bold 120% cursive"}} component="p" sx={{ flexGrow: 1 }}>
      Hola {sessionStorage.getItem("name")}
    </Typography>
    mostrarBoton = true;
  } else {
    saludo = <Typography color="textPrimary" style={{font:"oblique bold 120% cursive"}} component="p" sx={{ flexGrow: 1 }}>
      Hola Invitado</Typography>
  }

  function logout() {
    sessionStorage.clear();
    mostrarBoton = false;
    window.location.href = "./"
  }

  function loginBoton() {

    if (!mostrarBoton) {
      return (
        <div className={styles.button}>
          <Link to="/signin">
            <Button variant='outlined' color='inherit' sx={{ color: "white" }}>Iniciar Sesión</Button>
          </Link>
        </div>

      );
    }
  }

  function logoutBoton() {
    if (mostrarBoton) {
      return (
        <div className={styles.button}>
          <Button variant='outlined' color='inherit' sx={{ color: "white" }} onClick={logout}>Cerrar Sesión</Button>
        </div>
      );
    }
  }

  const testStyle = {
    width: '14px',
    height: '10px',
  };

  return (
    <Box sx={{ flexGrow: 5, }} >
      <AppBar position="static" >
        <Toolbar style={{ backgroundColor: '#0C55B9', }}>
          <Link to="/">
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2, padding: '0', }}
            >
              <div>
                <img src={logo} style={{ height: '50px', width: '70px', }} alt="logo_volatus" />
              </div>
            </IconButton>
          </Link>

          {saludo}
          {mostrarBoton &&
            <Link to="/crear-vuelos">
              <Button
                color="inherit"
                variant='outlined'
                sx={{
                  color: "white"
                }}
              >Crear Vuelos
              </Button>
            </Link>
          }



          <Link to="/vuelos">
            <Button
              color="inherit"
              variant='outlined'
              sx={{
                color: "white",

              }}
            >Vuelos
            </Button>
          </Link>

          {loginBoton()}

          {logoutBoton()}


          {
            sessionStorage.getItem("username") &&
            <Link to="/checkout-page">
              <IconButton aria-label='mostrar items del carrito' color='inherit'>
                <Badge badgeContent={basket.length} color='secondary'>
                  <ShoppingCart fontSize='large' />
                </Badge>
              </IconButton>
            </Link>
          }
        </Toolbar>
      </AppBar>
    </Box>
  );
}
