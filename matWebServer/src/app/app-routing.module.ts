import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PlannerComponent } from './planner/planner.component';
import { StartComponent } from './start/start.component';


const routes: Routes = [
    {
        path: '',
        component: StartComponent,
                   
    },
    {
      path: 'home',
      component: HomeComponent,
                 
    },
    {
    path: 'planner',
    component: PlannerComponent,
               
    },
    
];

@NgModule({
    imports: [
        RouterModule.forRoot(routes)
    ],
    exports: [
        RouterModule
    ],
    declarations: []
})
export class AppRoutingModule { }
