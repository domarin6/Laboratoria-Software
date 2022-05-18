import {BrowserRouter, Routes, Route} from 'react-router-dom';
import App from './App';
import Login from './components/Login';
import ManageAdmin from './components/ManageAdmin';
import { CreateAdmin } from './components/CreateAdmin';

function RoutesVolatus() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App/>} />
        {/* Ingresar ruta de login...... */}
        <Route path="/gestionar-admin" element={<ManageAdmin/>} />
        <Route path="/gestionar-admin/create" element= <CreateAdmin/> />
      </Routes>
    </BrowserRouter>
  );
}

export default RoutesVolatus;
