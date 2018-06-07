//MODULES
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppBootstrapModule } from './app-bootstrap.module';

import 'rxjs';
import 'hammerjs';
//COMPONENTS
import { AppComponent } from './app.component';
import { routingComponents } from './app-routing.module'
import { LoginTwoComponent } from './login-two/login-two.component';
import { LoginDialogComponent } from './login-dialog/login-dialog.component';
//SERVICES
import { UsersService } from './users.service';
import { ClassesComponent } from './classes/classes.component';
import { ScheduleComponent } from './schedule/schedule.component';

@NgModule({
  declarations: [
    AppComponent,
    routingComponents,
    ClassesComponent,
    ScheduleComponent
  ],
  imports: [
    ReactiveFormsModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule,
    AppBootstrapModule,
    HttpClientModule
  ],
  providers: [UsersService],
  entryComponents: [LoginDialogComponent, LoginTwoComponent],
  bootstrap: [AppComponent]
})
export class AppModule {


}
