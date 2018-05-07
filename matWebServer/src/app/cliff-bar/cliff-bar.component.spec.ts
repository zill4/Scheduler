import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CliffBarComponent } from './cliff-bar.component';

describe('CliffBarComponent', () => {
  let component: CliffBarComponent;
  let fixture: ComponentFixture<CliffBarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CliffBarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CliffBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
