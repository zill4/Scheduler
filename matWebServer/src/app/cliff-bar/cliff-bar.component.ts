import { Component, OnInit, Inject } from '@angular/core';
import { MatSnackBar } from '@angular/material';

@Component({
  selector: 'app-cliff-bar',
  templateUrl: './cliff-bar.component.html',
  styleUrls: ['./cliff-bar.component.scss']
})
export class CliffBarComponent implements OnInit {

  constructor( public snackBar: MatSnackBar) { }

  ngOnInit() {
  }
  
  openSnackBar(){
    this.snackBar.open("This is a cliff bar message!", "Got it!");
  }
}
