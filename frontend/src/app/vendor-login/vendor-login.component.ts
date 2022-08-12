import { Component, OnInit } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { LoginService } from '../services/login.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-vendor-login',
  templateUrl: './vendor-login.component.html',
  styleUrls: ['./vendor-login.component.css'],
})
export class VendorLoginComponent implements OnInit {
  constructor(
    private formBuilder: UntypedFormBuilder,
    private loginService: LoginService,
    private snackBar: MatSnackBar
  ) {}

  loginForm = this.formBuilder.group({
    username: '',
    password: '',
  });

  ngOnInit(): void {}

  onSubmit() {
    if (this.loginForm.value.username.length === 0) {
      this.snackBar.open('Enter username', 'X', {
        duration: 7000,
        horizontalPosition: 'end',
      });
    } else if (this.loginForm.value.password.length === 0) {
      this.snackBar.open('Enter password', 'X', {
        duration: 7000,
        horizontalPosition: 'end',
      });
    } else {
      this.loginService.login(this.loginForm.value);
    }
  }
}
