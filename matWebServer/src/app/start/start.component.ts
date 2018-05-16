import { Component, OnInit, Inject } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { MatDialog } from '@angular/material';
import { LoginDialogComponent } from '../login-dialog/login-dialog.component';

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.scss']
})
export class StartComponent implements OnInit {

  dialogResult: string;
  constructor(public dialog: MatDialog){}
 
  ngOnInit(){
  }
  
  openDialog(){
    let dialogRef = this.dialog.open(LoginDialogComponent, {
      width: '600px',
      data: 'This text is passed into the dialog'
    });
  
    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog closed: ${result}`);
      this.dialogResult = result;
    })
  }
}

