import { createAdminFunction } from './Functions/manageAdminFunction';
import { useForm } from './hooks/useForm';
import '../css/crud_root.css';
import imagenes from './assets/imagenes';

export const CreateAdmin = () => {

  const [ formValues, handleInputChange ] = useForm({
      DNI: '',
      username: '',
      nombre: '',
      password: ''
  });

  const { DNI, username, nombre, password } = formValues;

  const handleCreate = (e) =>{
      e.preventDefault();
      createAdminFunction( { DNI, username, nombre, password } );
  }

  return (
    <div className="main">
        <div className="p1">
            <div className="logo">
                <img src={imagenes.src_volatus_logo} alt="logo_main" className="logo_main img" />
            </div>
            <div className="cuadro">
                <h1>Crear Administrador</h1>
                <img src={imagenes.src_user_logo} alt="logo_user" className="img logo_user" />
            </div>
        </div>
        <div className="p2">
            <div className="profile_picture">
                <img src={imagenes.src_incognito} alt="profile_picture" className="img_profile" />
                <button className="button primary_button">Subir imagen</button>
            </div>

            <form onSubmit={ handleCreate }>
                <div className="info_adm">
                    <span className="form">
                        <label htmlFor="name" className="label">Nombre</label>
                        <input
                            type="text"
                            id="name"
                            className="input input-name"
                            value = { nombre }
                            onChange={ handleInputChange } />
                    </span>

                    <span className="form">
                        <label htmlFor="document" className="label">Documento</label>
                        <input
                            type="text"
                            id="document"
                            className="input input-doc"
                            value = { DNI }
                            onChange={ handleInputChange } />
                    </span>

                    <span className="form">
                        <label htmlFor="user" className="label">Usuario</label>
                        <input
                            type="text"
                            id="user"
                            className="input input-user"
                            value = { username }
                            onChange={ handleInputChange } />
                    </span>

                    <span className="form">
                        <label htmlFor="password" className="label">Contraseña</label>
                        <input
                            type="password"
                            id="password"
                            placeholder="**********"
                            className="input input-name"
                            value = { password }
                            onChange={ handleInputChange } />
                    </span>

                    <span className="interact">
                        <button type="submit" className="button primary_button">Crear</button>
                        <button className="button primary_button">Volver</button>
                    </span>
                </div>
            </form>
        </div>
    </div>
  );

}
