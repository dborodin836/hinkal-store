import { Component, OnInit } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { LoginService } from '../services/login.service';
import { SnackBarService } from '../services/snack-bar.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  constructor(
    private formBuilder: UntypedFormBuilder,
    private loginService: LoginService,
    private snackBar: SnackBarService
  ) {}

  loginForm = this.formBuilder.group({
    username: '',
    password: '',
  });

  ngOnInit(): void {}

  onSubmit() {
    if (this.loginForm.value.username.length === 0) {
      this.snackBar.openSnackBar('Enter username', undefined, undefined, 'error');
    } else if (this.loginForm.value.password.length === 0) {
      this.snackBar.openSnackBar('Enter password', undefined, undefined, 'error');
    } else {
      this.loginService.login(this.loginForm.value);
    }
  }
}
