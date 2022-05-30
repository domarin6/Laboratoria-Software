import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Badge from '@mui/material/Badge';
import logo from '../components/assets/img/volatus_logo_removebg.png';
// import styles from '../css/NavBar.module.css'
import styles from '../css/nav.module.css';
import { ShoppingCart } from '@mui/icons-material';


// import { makeStyles } from '@mui/styles';
// import { makeStyles } from '@mui/styled-engine-sc';
// import { makeStyles } from '@mui/material/styles';


// const useStyles = makeStyles((theme) =>({

//   root:{
//       flexGrow:1,
//       marginBottom: "7rem",
//   },
//   appBar:{
//       backgroundColor:"black",  
//       boxShadow:"none",

//   },
//   grow:{
//       flexGrow:1,
//   },
//   button:{
//       marginLeft: theme.spacing(2),
//   },
//   image:{
//       marginRight: "10px",
//       height:"1rem",
//   },
// }));

export default function NavBar() {

  // const classes = useStyles();
  return (
    <Box sx={{ flexGrow: 5 }} className={styles.root}>
      <AppBar position="static" className={styles.cuadro}>
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <img src={logo} className={styles.image} alt="logo_volatus" />
          </IconButton>
          <Typography variant="h6" color="textPrimary" component="p" sx={{ flexGrow: 1 }}>
            Hola Invitado
          </Typography>
          <div className={styles.grow}/>
          <div className={styles.button}>
            <Button variant='outlined' color='inherit'>
              Crear Cuenta
            </Button>
          </div>
          <Button color="inherit" variant='outlined'>Iniciar Sesión</Button>
          <IconButton aria-label='mostrar items del carrito' color='inherit'>
            <Badge badgeContent={2} color='secondary'>
              <ShoppingCart fontSize='large' color='snow'/>  
            </Badge>
          </IconButton>
          
          
        </Toolbar>
      </AppBar>
    </Box>
  );
}
