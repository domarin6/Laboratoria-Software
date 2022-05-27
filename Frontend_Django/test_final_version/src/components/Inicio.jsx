import React from "react"; 
import styles from '../css/main.module.css'; 
import cx from 'classnames'; 

export default function Inicio(){ 
    return (
        <div className="container">
            {/* className={cx(styles.carousel, styles.slide)} */}

            <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false">
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="https://i.ytimg.com/vi/vPJS2moVUFA/maxresdefault.jpg" class="d-block w-100" alt="..." />
                        <div class="carousel-caption d-none d-md-block">
                            <h5 className={styles.colorLetra}>
                                <strong>San Andres</strong>
                            </h5>
                            <p className={styles.colorLetra}>
                                <strong>San Andrés es una isla colombiana del mar Caribe, frente a la costa de Nicaragua. Es conocida por los arrecifes de coral y la música reggae</strong>
                            </p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://www.ibaguelimpia.com/assets/media/photo-ibague.jpg" class="d-block w-100" alt="..." />
                        <div class="carousel-caption d-none d-md-block">
                            <h5 className={styles.colorLetra1}>
                                <strong>Ibagué</strong> 
                            </h5>
                            <p className={styles.colorLetra1}>
                                <strong>Ibagué es una ciudad del oeste de Colombia conocida por su patrimonio musical</strong>
                            </p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://la.network/wp-content/uploads/2020/10/WhatsApp-Image-2020-09-30-at-1.08.29-PM-1.jpg" class="d-block w-100" alt="Barranquilla" />
                        <div class="carousel-caption d-none d-md-block">
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
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>

            div.


        </div>
    );
}