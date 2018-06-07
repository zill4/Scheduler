import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

//Components, button component
import { MatButtonModule, MatToolbarModule, MatInputModule,MatProgressSpinnerModule, MatCardModule,
     MatDialogModule, MatSidenavModule, MatIconModule, MatTooltipModule, MatSnackBarModule, MatListModule, MatExpansionModule, MatSlideToggleModule  } from '@angular/material';
import {MatAutocompleteModule} from '@angular/material/autocomplete';

@NgModule({
    //imports property, by name and object.
  imports: [MatButtonModule, MatToolbarModule, MatInputModule,MatProgressSpinnerModule,
     MatCardModule,MatDialogModule,MatSidenavModule,MatIconModule,MatTooltipModule, MatSnackBarModule, MatListModule, MatAutocompleteModule, MatExpansionModule, MatSlideToggleModule ],
  
     exports: [MatButtonModule, MatToolbarModule, MatInputModule,MatProgressSpinnerModule,
     MatCardModule,MatDialogModule,MatSidenavModule, MatIconModule,MatTooltipModule, MatSnackBarModule,MatListModule, MatAutocompleteModule, MatExpansionModule, MatSlideToggleModule  ],
})
export class MaterialModule { }

