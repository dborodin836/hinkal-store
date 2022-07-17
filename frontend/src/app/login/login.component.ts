import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { LoginService } from '../services/login.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  constructor(private formBuilder: FormBuilder, private loginService: LoginService, private router: Router) {}

  loginForm = this.formBuilder.group({
    username: '',
    password: '',
  });

  ngOnInit(): void {}

  onSubmit() {
    console.log(this.loginForm.value);
    this.loginService.login(this.loginForm.value);
    this.router.navigate(['dashboard/']);
  }
}
