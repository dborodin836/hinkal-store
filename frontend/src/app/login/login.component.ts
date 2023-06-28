import { Component, OnInit } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { LoginService } from '../services/login.service';
import { SnackBarMessagesService } from '../services/messages.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  constructor(
    private formBuilder: UntypedFormBuilder,
    private loginService: LoginService,
    private snackBar: SnackBarMessagesService
  ) {}

  loginForm = this.formBuilder.group({
    username: '',
    password: '',
  });

  ngOnInit(): void {}

  onSubmit() {
    if (this.loginForm.value.username.length === 0) {
      this.snackBar.errorMessage('Enter username');
    } else if (this.loginForm.value.password.length === 0) {
      this.snackBar.errorMessage('Enter password');
    } else {
      this.loginService.login(this.loginForm.value);
    }
  }
}
