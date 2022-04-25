import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Login from './components/Login';

function RoutesVolatus() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default RoutesVolatus;
