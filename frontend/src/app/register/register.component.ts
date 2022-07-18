import {Component, OnInit} from '@angular/core';
import {FormBuilder} from "@angular/forms";
import {LoginService} from "../services/login.service";
import {Router} from "@angular/router";
import {MatSnackBar} from "@angular/material/snack-bar";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(private formBuilder: FormBuilder,
              private loginService: LoginService,
              private router: Router,
              private snackBar: MatSnackBar) {
  }

  registerForm = this.formBuilder.group({
    username: '',
    password: '',
    password_repeat: '',
  })

  ngOnInit(): void {
  }

  onSubmit() {
    if (this.registerForm.value.password === this.registerForm.value.password_repeat) {
      this.loginService.register(this.registerForm.value.username, this.registerForm.value.password)
    } else {
      this.snackBar.open("Password do not match.", "X", {
        duration: 7000,
        horizontalPosition: "end"
      })
    }
  }

}
