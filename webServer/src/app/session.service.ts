import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SessionService {

    messages = [
     {id: 0, text: 'hello world'},
     {id: 1, text: 'what is life'},
     {id: 2, text: 'I am alive'},
    ]
    update(id, text){
      this.messages = this.messages.map( m =>
      m.id == id
        ? {id, text}
          : m
        )
    }
  constructor() { }
}
