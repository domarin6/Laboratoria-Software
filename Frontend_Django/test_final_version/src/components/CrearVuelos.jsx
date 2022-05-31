import * as React from 'react';
import {useState} from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import ConnectingAirportsIcon from '@mui/icons-material/ConnectingAirports';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import {Link as RouteLink} from 'react-router-dom';
import { startRegister } from './Functions/registerFunction';
import { Calendar } from 'primereact/calendar';




// function Copyright(props) {
//   return (
//     <Typography variant="body2" color="text.secondary" align="center" {...props}>
//       {'Copyright © '}
//       <Link color="inherit" href="https://mui.com/">
//         Your Website
//       </Link>{' '}
//       {new Date().getFullYear()}
//       {'.'}
//     </Typography>
//   );
// }

const theme = createTheme();

export default function SignUp() {
  // const handleSubmit = (event) => {
  //   event.preventDefault();
  //   const data = new FormData(event.currentTarget);
  //   console.log({
  //     email: data.get('email'),
  //     password: data.get('password'),
  //   });
  // };

  const [origen, setorigen] = useState("");
  const [destino, setdestino] = useState("");
  const [costo_economico, setcosto_economico] = useState("");
  const [costo_primera_clase, setcosto_primera_clase] = useState("");
  const [description, setdescription] = useState("");
  const [tipo, settipo] = useState("");
  const [full_description, setfull_description] = useState("");
  const [rating, setrating] = useState("");
  const [imagen, setimagen] = useState("");
  const [fecha, setfecha] = useState("");
  const [hora, sethora] = useState("");

  const signup = (e) =>{
    e.preventDefault();
    startRegister(origen, destino, costo_economico, costo_primera_clase, description, tipo, full_description, rating, imagen, fecha, hora);
  }

  const [fechaSeleccionada, cambiarFechaSeleccionada] = useState(new Date());
  
  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <ConnectingAirportsIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Crear Vuelo
          </Typography>
          {/* onSubmit={handleSubmit} */}
          <Box component="form" noValidate sx={{ mt: 3 }}>
            <Grid container spacing={2}>

              <Grid item xs={12} sm={6}>
                <TextField
                  value={origen}
                  onChange={e => setorigen(e.target.value)}
                  name="origen"
                  required
                  fullWidth
                  id="origen"
                  label="Origen"
                  autoFocus
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  value={destino}
                  onChange={e => setdestino(e.target.value)}
                  name="destino"
                  required
                  fullWidth
                  id="destino"
                  label="Destino"
                  autoFocus
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  value={costo_economico}
                  onChange={e => setcosto_economico(e.target.value)}
                  name="costo_economico"
                  required
                  fullWidth
                  id="costo_economico"
                  label="Precio Clase Económica"
                  autoFocus
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  value={costo_primera_clase}
                  onChange={e => setcosto_primera_clase(e.target.value)}
                  name="costo_primera_clase"
                  required
                  fullWidth
                  id="costo_primera_clase"
                  label="Precio Primera Clase"
                  autoFocus
                />
              </Grid>

{/* 
              <Grid item xs={12}>
                <TextField
                  value={correo_electronico}
                  onChange={e => setcorreo_electronico(e.target.value)}
                  required
                  fullWidth
                  id="email"
                  label="Correo Electrónico"
                  name="email"
                />
              </Grid>

              <Grid item xs={12}>
                <TextField
                  value={username}
                  onChange={e => setusername(e.target.value)}
                  required
                  fullWidth
                  id="user"
                  label="Usuario"
                  name="user"
                />
              </Grid>

              <Grid item xs={12}>
                <TextField
                  value={password}
                  onChange={e => setpassword(e.target.value)}
                  required
                  fullWidth
                  name="password"
                  label="Contraseña"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                />
              </Grid> */}
              
            <Grid item xs={12}>
                  <label htmlFor="fecha" style={{marginRight:"10px", color:"gray"}}>Fecha</label>
                  <Calendar 
                  id="fecha" 
                  value={fecha} 
                  onChange={(e) => setfecha(e.value)} />
              </Grid>
            </Grid>


            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              onClick={signup}
            >
              Crear Vuelo
            </Button>            
          </Box>
        </Box>
        {/* <Copyright sx={{ mt: 5 }} /> */}
      </Container>
    </ThemeProvider>
  );
}