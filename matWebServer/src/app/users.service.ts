import { Injectable } from "@angular/core";
import { HttpClient } from"@angular/common/http";
import { Observable } from "rxjs/Observable";

@Injectable()
export class UsersService{

    constructor(private http: HttpClient){}
    
    fetchUsers(): Observable<Object>{
       return  this.http.get('http://127.0.0.1:8000/users/');
    }
}