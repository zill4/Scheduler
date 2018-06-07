import { Component } from '@angular/core';
import { MatDialog } from '@angular/material';
import { LoginTwoComponent } from './login-two/login-two.component';
import { UsersService } from './users.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
 
  users$;

  dialogResult: string;
  constructor(public dialog: MatDialog, private usersService: UsersService, private router: Router){}
 
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

  openProfile(){
    this.router.navigate(['/profile']);
  }
  fetchUsers(){
    this.users$ = this.usersService.fetchUsers();
  }
}
