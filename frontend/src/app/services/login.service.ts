import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { UserModel } from '../models/user.model';
import { MatSnackBar } from '@angular/material/snack-bar';
import { HOST } from '../conf';

const baseUrl = HOST + '/auth/';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private auth_token = '';
  private user: UserModel = {};

  constructor(private http: HttpClient, private router: Router, private snackBar: MatSnackBar) {}

  getToken(): string | undefined {
    return this.auth_token;
  }

  getAuthHeader() {
    return new HttpHeaders({ Authorization: 'Token ' + this.getToken() });
  }

  logout() {
    // @ts-ignore
    let promise = new Promise((resolve, reject) => {
      this.http
        .post(baseUrl + 'token/logout/', '', { headers: this.getAuthHeader() })
        .toPromise()
        .then(
          () => {
            this.auth_token = '';
            this.user = {};
            this.router.navigate(['']);
            this.openSnackBar('You are logged out.', 'X');
          },
          () => {
            this.openSnackBar('Service unavailable. Try again later.', 'X');
          }
        );
    });
    return promise;
  }

  login(data: { username: any; password: any }) {
    let promise = new Promise((resolve, reject) => {
      this.http
        .post<any>(baseUrl + 'token/login/', data)
        .toPromise()
        .then((res) => {
          this.auth_token = res.auth_token;
          console.log(res.auth_token);
          this.getUser();
        });
    });
    return promise;
  }

  isAuthorized(): boolean {
    return this.auth_token != '';
  }

  getUser() {
    let promise = new Promise((resolve, reject) => {
      let url = baseUrl + 'users/me/';
      this.http
        .get(url, { observe: 'response', responseType: 'json', headers: this.getAuthHeader() })
        .toPromise()
        .then((res) => {
          // @ts-ignore
          this.user = res.body;
        });
    });
    return promise;
  }

  getUserData() {
    return this.user;
  }

  openSnackBar(message: string, action: string) {
    this.snackBar.open(message, action, {
      duration: 7000,
      horizontalPosition: 'end',
    });
  }

  register(username: string, password: string, email: string) {
    let promise: any = new Promise((resolve, reject) => {
      let url = baseUrl + 'users/';
      this.http
        .post(
          url,
          { username: username, password: password, email: email },
          {
            observe: 'response',
            responseType: 'json',
          }
        )
        .toPromise()
        .then(
          () => {
            this.openSnackBar('Success!', 'X');
            this.router.navigate(['account-activation']);
          },
          (error) => {
            if (error.error.username && error.error.password) {
              this.openSnackBar('User already exists and password is too weak or unacceptable symbols', 'X');
            } else if (error.error.password) {
              this.openSnackBar('Password is too weak or unacceptable symbols', 'X');
            } else if (error.error.username || error.error.email) {
              this.openSnackBar('User already exists or unacceptable symbols', 'X');
            } else {
              this.openSnackBar('Service unavailable. Try again later.', 'X');
            }
          }
        );
    });
    return promise;
  }
}
