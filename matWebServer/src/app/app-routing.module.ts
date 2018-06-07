import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PlannerComponent } from './planner/planner.component';
import { StartComponent } from './start/start.component';
import { ProfileComponent } from './profile/profile.component';
import { AboutComponent } from './about/about.component';
import { LoginDialogComponent } from './login-dialog/login-dialog.component';
import { ToolTipComponent } from './tool-tip/tool-tip.component';
import { CliffBarComponent } from './cliff-bar/cliff-bar.component';
import { ImpfromComponent } from './impfrom/impfrom.component';
import { LoginTwoComponent } from './login-two/login-two.component';
import { ClassesComponent } from './classes/classes.component';
import { ScheduleComponent } from './schedule/schedule.component';
import { scheduleMicroTask } from '@angular/core/src/util';
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
        path: 'profile',
        component: ProfileComponent,
        children: [
            {
                path: 'schedule', component: ScheduleComponent,
            },
            {
                path: 'classes', component: ClassesComponent,
            },
            {
                path: 'planner',component: PlannerComponent,
                           
            },
        ]
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
export const routingComponents = [ 
    ClassesComponent,
    ScheduleComponent,
    StartComponent,
    HomeComponent,
    PlannerComponent,
    AboutComponent,
    LoginDialogComponent,
    ToolTipComponent,
    CliffBarComponent,
    ImpfromComponent,
    LoginTwoComponent,
    ProfileComponent ]