import { Component, OnInit } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { LoginService } from '../services/login.service';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-vendor-register',
  templateUrl: './vendor-register.component.html',
  styleUrls: ['./vendor-register.component.css'],
})
export class VendorRegisterComponent implements OnInit {
  constructor(
    private formBuilder: UntypedFormBuilder,
    private loginService: LoginService,
    private router: Router,
    private snackBar: MatSnackBar
  ) {}

  registerForm = this.formBuilder.group({
    username: '',
    email: '',
    password: '',
    password_repeat: '',
  });

  ngOnInit(): void {}

  onSubmit() {
    if (this.registerForm.value.username.length === 0) {
      this.snackBar.open('Enter username.', 'X', {
        duration: 7000,
        horizontalPosition: 'end',
      });
      return;
    }
    if (this.registerForm.value.email.length === 0) {
      this.snackBar.open('Enter Email.', 'X', {
        duration: 7000,
        horizontalPosition: 'end',
      });
      return;
    }
    if (this.registerForm.value.password.length === 0) {
      this.snackBar.open('Enter Password.', 'X', {
        duration: 7000,
        horizontalPosition: 'end',
      });
      return;
    }
    if (this.registerForm.value.password === this.registerForm.value.password_repeat) {
      this.loginService.registerVendor(
        this.registerForm.value.username,
        this.registerForm.value.password,
        this.registerForm.value.email
      );
    } else {
      this.snackBar.open('Password do not match.', 'X', {
        duration: 7000,
        horizontalPosition: 'end',
      });
    }
  }
}
