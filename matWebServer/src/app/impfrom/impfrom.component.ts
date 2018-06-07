import { Component, OnInit } from '@angular/core';
//import { MatInput } from '@angular/material';
import { User } from '../../objects/user';

@Component({
  selector: 'app-impfrom',
  templateUrl: './impfrom.component.html',
  styleUrls: ['./impfrom.component.scss']
})
export class ImpfromComponent implements OnInit {
  
  
  user = new User();
  constructor() { }

 
  ngOnInit() {
  }

    onSubmit(){
        
        alert("Thank youfor submitting! Data: " + JSON.stringify(this.user));
    }
}
