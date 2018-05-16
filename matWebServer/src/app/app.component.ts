import { Component } from '@angular/core';
import { MatDialog } from '@angular/material';
import { LoginTwoComponent } from './login-two/login-two.component';
import { UsersService } from './users.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
 
  users$;

  dialogResult: string;
  constructor(public dialog: MatDialog, private usersService: UsersService){}
 
  ngOnInit(){
  }
  
  openDialog(){
    let dialogRef = this.dialog.open(LoginTwoComponent, {
      width: '600px',
      data: 'This text is passed into the dialog'
    });
  
    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog closed: ${result}`);
      this.dialogResult = result;
    })
  }

  fetchUsers(){
    this.users$ = this.usersService.fetchUsers();
  }
}
