//MODULES
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppBootstrapModule } from './app-bootstrap.module';
import 'hammerjs';
//COMPONENTS
import { AppComponent } from './app.component';
import { StartComponent } from './start/start.component';
import { HomeComponent } from './home/home.component';
import { PlannerComponent } from './planner/planner.component';
import { AboutComponent } from './about/about.component';
import { LoginDialogComponent } from './login-dialog/login-dialog.component';
import { ToolTipComponent } from './tool-tip/tool-tip.component';
import { CliffBarComponent } from './cliff-bar/cliff-bar.component';
import { ImpfromComponent } from './impfrom/impfrom.component';
import { LoginTwoComponent } from './login-two/login-two.component';
import { UsersService } from './users.service';

@NgModule({
  declarations: [
    AppComponent,
    StartComponent,
    HomeComponent,
    PlannerComponent,
    AboutComponent,
    LoginDialogComponent,
    ToolTipComponent,
    CliffBarComponent,
    ImpfromComponent,
    LoginTwoComponent
  ],
  imports: [
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
