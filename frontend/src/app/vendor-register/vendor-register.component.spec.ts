import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VendorRegisterComponent } from './vendor-register.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';
import { MatSnackBarModule } from '@angular/material/snack-bar';

describe('VendorRegisterComponent', () => {
  let component: VendorRegisterComponent;
  let fixture: ComponentFixture<VendorRegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [VendorRegisterComponent],
      imports: [HttpClientTestingModule, ReactiveFormsModule, FormsModule, RouterTestingModule, MatSnackBarModule],
    }).compileComponents();

    fixture = TestBed.createComponent(VendorRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
