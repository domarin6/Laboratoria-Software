import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'volatus';
  user_main = 'root';
  img = 'assets/volatus_logo.png';
  img_gif = 'https://i.pinimg.com/originals/ad/af/58/adaf588d53dc032d19c50481d32f60da.gif';
  nombre = 'Dorian';

  person = { //creación de un objeto.
    Tutulo : 'volatus',
    user : 'root',
    logo : 'assets/volatus_logo.png'
  }

}
