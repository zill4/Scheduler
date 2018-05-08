import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef } from '@angular/material';
import { MAT_DIALOG_DATA } from '@angular/material';
import { User } from '../objects/user';

@Component({
  selector: 'app-login-two',
  templateUrl: './login-two.component.html',
  styleUrls: ['./login-two.component.scss']
})
export class LoginTwoComponent implements OnInit {

  user = new User();
  constructor(public thisDialogRef: MatDialogRef<LoginTwoComponent>, @Inject(MAT_DIALOG_DATA) public data: string) { }

  ngOnInit() {
  }

  onCloseConfirm(){
    console.log("Thank youfor submitting! Data: " + JSON.stringify(this.user));
    this.thisDialogRef.close('confrim');
  }
  
  onCloseCancel(){
    this.thisDialogRef.close('cancel');
  }
  
}
