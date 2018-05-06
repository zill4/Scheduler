import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { SessionService } from './session.service';
import { StartComponent } from './start/start.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    StartComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
  ],
  providers: [{provide:'session',useClass:SessionService},
              {provide:'api', useValue:'http://localhost:8000/'}],
  bootstrap: [AppComponent]
})
export class AppModule { }
