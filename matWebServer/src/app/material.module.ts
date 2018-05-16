import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

//Components, button component
import { MatButtonModule, MatToolbarModule, MatInputModule,MatProgressSpinnerModule, MatCardModule,
     MatDialogModule, MatSidenavModule, MatIconModule, MatTooltipModule, MatSnackBarModule,  } from '@angular/material';

@NgModule({
    //imports property, by name and object.
  imports: [MatButtonModule, MatToolbarModule, MatInputModule,MatProgressSpinnerModule,
     MatCardModule,MatDialogModule,MatSidenavModule,MatIconModule,MatTooltipModule, MatSnackBarModule ],
  
     exports: [MatButtonModule, MatToolbarModule, MatInputModule,MatProgressSpinnerModule,
     MatCardModule,MatDialogModule,MatSidenavModule, MatIconModule,MatTooltipModule, MatSnackBarModule  ],
})
export class MaterialModule { }

