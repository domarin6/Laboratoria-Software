import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Login from './components/Login';
import ManageAdmin from './components/ManageAdmin';
import { CreateAdmin } from './components/CreateAdmin';

function RoutesVolatus() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/gestionar-admin" element={<ManageAdmin/>} />
        <Route path="/gestionar-admin/create" element= <CreateAdmin/> />
      </Routes>
    </BrowserRouter>
  );
}

export default RoutesVolatus;
