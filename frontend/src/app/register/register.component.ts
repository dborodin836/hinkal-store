import { Component, OnInit } from '@angular/core';
import {FormBuilder} from "@angular/forms";
import {LoginService} from "../services/login.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(private formBuilder: FormBuilder,
              private loginService: LoginService,
              private router: Router) {}

  registerForm = this.formBuilder.group({
    username: '',
    password: '',
    password_repeat: '',
  })

  ngOnInit(): void {
  }

  onSubmit() {
    this.loginService.register(this.registerForm.value.username, this.registerForm.value.password)
  }

}
