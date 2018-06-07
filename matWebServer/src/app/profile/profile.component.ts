import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  constructor( private route: ActivatedRoute, private router: Router) { }

  ngOnInit() {
  }
  openPlanner(){
    this.router.navigate(['planner'], {relativeTo: this.route});
  }
  openSchedule(){
    this.router.navigate(['schedule'], {relativeTo: this.route});
  }
  openClasses(){
    this.router.navigate(['classes'], {relativeTo: this.route});
  }
 
}
