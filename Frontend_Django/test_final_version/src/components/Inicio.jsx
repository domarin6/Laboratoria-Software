import React from "react"; 
import styles from '../css/main.module.css'; 
// import cx from 'classnames'; 

export default function Inicio(){ 
    return (
        <div className={styles.container}>
            {/* className={cx(styles.carousel, styles.slide)} */}

            <div className={styles.carrusel}>
                <div id="carouselExampleCaptions" className="carousel slide" data-bs-ride="false">
                    <div className="carousel-indicators">
                        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div className="carousel-inner">
                        <div className="carousel-item active">
                            <img src="https://i.ytimg.com/vi/vPJS2moVUFA/maxresdefault.jpg" className="d-block w-100" alt="..." />
                            <div className="carousel-caption d-none d-md-block">
                                <h5 className={styles.colorLetra}>
                                    <strong>San Andres</strong>
                                </h5>
                                <p className={styles.colorLetra}>
                                    <strong>San Andrés es una isla colombiana del mar Caribe, frente a la costa de Nicaragua. Es conocida por los arrecifes de coral y la música reggae</strong>
                                </p>
                            </div>
                        </div>
                        <div className="carousel-item">
                            <img src="https://i0.wp.com/tolimaonline.com/wp-content/uploads/2020/08/Ibagu%C3%A9.jpg?zoom=2&resize=780%2C470&ssl=1" className="d-block w-100" alt="..." />
                            <div className="carousel-caption d-none d-md-block">
                                <h5 className={styles.colorLetra1}>
                                    <strong>Ibagué</strong> 
                                </h5>
                                <p className={styles.colorLetra1}>
                                    <strong>Ibagué es una ciudad del oeste de Colombia conocida por su patrimonio musical</strong>
                                </p>
                            </div>
                        </div>
                        <div className="carousel-item">
                            <img src="https://la.network/wp-content/uploads/2020/10/WhatsApp-Image-2020-09-30-at-1.08.29-PM-1.jpg" className="d-block w-100" alt="Barranquilla" />
                            <div className="carousel-caption d-none d-md-block">
                                <h5 className={styles.colorLetra}>
                                    <strong>Barranquilla</strong> 
                                </h5>
                                <p className={styles.colorLetra}>
                                    <strong>
                                    Barranquilla, es la capital del departamento Atlántico de Colombia y es un desbordante puerto marino, bordeado por el río Magdalena
                                    </strong> 
                                </p>
                            </div>
                        </div>
                    </div>
                    <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Previous</span>
                    </button>
                    <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                        <span className="carousel-control-next-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Next</span>
                    </button>
                </div>
            </div>

            <div className={styles.quienesSomos}>
                <div className={styles.p1}>
                    <h1> <strong> ¿Quiénes Somos? </strong></h1>
                    <p>Somos una empresa la cual busca dar una facilidad a sus clientes en el momento de comprar sus tiquetes de viaje ya sean a nivel nacional o internacional se buscará dar la mejor relación calidad precio al usuario final.</p>
                </div>
            </div>

            <div className={styles.misionVision}>
                <div className={styles.p2}>
                    <h1> <strong>Misión y Visión</strong> </h1>
                    <p>Nuestra misión es brindar un ahorro de tiempo y dinero a nuestros clientes en el momento de comprar sus tiquetes, ya que se buscará tener los mejores precios del mercado.</p>
                    <p>Para 2023 esperamos ser la aerolínea preferida por los pasajeros de aviones.</p>
                </div>
            </div>


        </div>
    );
}