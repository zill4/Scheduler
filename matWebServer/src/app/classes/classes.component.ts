import { Component, OnInit } from '@angular/core';
import {FormControl} from '@angular/forms';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

export class State {
  constructor(public name: string, public population: string, public flag: string) { }
}
export class Subject{
constructor( public name: string, public initials: string, public courses: Course[]) {}
}
export class Course{
constructor(public crn: string, public crse: string, public sec: string, public cmp: string, public cred: string, public title:string, public days: string, public time: string,
public cap:string, public act:string, public wl_cap:string, public wl_act:string, public instructor:string, public date:string, public location:string, public attribute: string,
public lab_days: string, public lab_time: string, public lab_instructor:string, public lab_date:string, public lab_location:string ){}
}
/*
  private  String crn;
    private  String crse;
    //Id number for map look up.
    private  String sec; //idk if this is necessary.
    private  String cmp;
    private String cred;
    private  String title;
    private  String days; //Also probably should make a map accessible day object.
    private  String time; //Probably should make a time object.
    private String cap;
    private String act; //idk if this is necessary.
    private String wl_cap;
    private String wl_act; //idk if this is necessary.
    private  String instructor; //need to link with RMP
    private  String date; //Should include in time object.
    private  String location; //Would be cool if we could make a location/GPS/Map based obj.
    private  String attribute; //This is like a message, about the class;
    private  String lab_days;
    private  String lab_time;
    private  String lab_instructor;
    private  String lab_date;
    private  String lab_location;

*/
@Component({
  selector: 'app-classes',
  templateUrl: './classes.component.html',
  styleUrls: ['./classes.component.scss']
})



export class ClassesComponent implements OnInit {
  courseControl: FormControl;
  filteredSubjects: Observable<any[]>;

  subjects: Subject[];

  constructor(private http: HttpClient) { 
    this.courseControl = new FormControl();
    this.filteredSubjects = this.courseControl.valueChanges
      .pipe(
        startWith(''),
        map(subject => subject ? this.filterSubjects(subject) : this.subjects.slice())
      );
    }
    filterSubjects(name: string) {
      return this.subjects.filter(subject =>
        subject.name.toLowerCase().indexOf(name.toLowerCase()) === 0);
    }
    //http://athena.us-west-1.elasticbeanstalk.com/subjects/all
    //http://localhost:8181/subjects/all
  ngOnInit() {
    this.getSubjects()
    .subscribe(data => this.subjects = data )
  }
  getSubjects(): Observable<Subject[]>{
    return this.http.get<Subject[]>('http://localhost:8181/subjects/all');
  }
  panelOpenState: boolean = false;







}
