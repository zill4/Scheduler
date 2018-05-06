import { Component, Inject } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  onUpdate(id, text){
    this.session.update(id,text);
  }

  constructor(@Inject('session') private session){}
}
