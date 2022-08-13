import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VendorLoginComponent } from './vendor-login.component';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';
import { MatSnackBarModule } from '@angular/material/snack-bar';

describe('VendorLoginComponent', () => {
  let component: VendorLoginComponent;
  let fixture: ComponentFixture<VendorLoginComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [VendorLoginComponent],
      imports: [
        BrowserModule,
        HttpClientTestingModule,
        ReactiveFormsModule,
        FormsModule,
        RouterTestingModule,
        MatSnackBarModule,
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(VendorLoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
