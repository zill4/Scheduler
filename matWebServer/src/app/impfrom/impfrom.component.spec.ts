import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ImpfromComponent } from './impfrom.component';

describe('ImpfromComponent', () => {
  let component: ImpfromComponent;
  let fixture: ComponentFixture<ImpfromComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ImpfromComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ImpfromComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
