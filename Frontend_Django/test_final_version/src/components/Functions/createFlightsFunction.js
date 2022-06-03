import { fetchWithoutToken, fetchWithToken } from "./fetch";


export const startLogin = async(username, password) => {
    const response = await fetchWithoutToken(
        'crudRoot/Login/', { username, password },
        'POST'
    );
    const body = await response.json();


    if (response.status === 200 || response.status === 201) {

        // set user info
        // localStorage.setItem('token', body.token);
        sessionStorage.setItem('username', body.user.username);
        sessionStorage.setItem('DNI', body.user.DNI);
        sessionStorage.setItem('name', body.user.nombre);

        // sessionStorage.setItem

        timerNotification('Inicio de Sesion Exitoso!');
        window.location.href = "./vuelos";

    } else {
        notification('ERROR', body.error, 'error');
    }
}