import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { environment } from '../../environments/environment';
import { SnackBarMessagesService } from './messages.service';

const baseUrl = `${environment.HOST}/auth/`;

interface ICredentials {
  username: string;
  password: string;
}

export interface IUser {
  email: string;
  id: number;
  username: string;
}

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  constructor(private http: HttpClient, private router: Router, private snackBar: SnackBarMessagesService) {}

  getToken(): string | null {
    return localStorage.getItem('auth_token');
  }

  getAuthHeader() {
    return new HttpHeaders({ Authorization: `Token ${this.getToken()}` });
  }

  logout() {
    return new Promise<HttpResponse<any>>((resolve, reject) => {
      this.http
        .post(`${baseUrl}token/logout/`, '', { headers: this.getAuthHeader() })
        .toPromise()
        .then(
          () => {
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user');
            this.router.navigate(['']);
            this.snackBar.successMessage('You are logged out.');
          },
          () => {
            this.snackBar.errorMessage('Service unavailable. Try again later.');
          }
        );
    });
  }

  login(credentials: ICredentials) {
    return new Promise<HttpResponse<any>>((resolve, reject) => {
      this.http
        .post<any>(`${baseUrl}token/login/`, credentials)
        .toPromise()
        .then(
          (res) => {
            localStorage.setItem('auth_token', res.auth_token);
            this.router.navigate(['dashboard/']);
            this.snackBar.successMessage('You are logged in.');
          },
          (error) => {
            if (error.error.username) {
              this.snackBar.warningMessage('User does not exists');
            } else if (error.error.password) {
              this.snackBar.warningMessage('Wrong password');
            } else {
              this.snackBar.errorMessage('Service unavailable. Try again later.');
            }
          }
        );
    });
  }

  isAuthorized(): boolean {
    return localStorage.getItem('auth_token') != null;
  }

  getUser() {
    let url = `${baseUrl}users/me/`;
    return this.http.get(url, { observe: 'response', responseType: 'json', headers: this.getAuthHeader() }).toPromise();
  }

  getUserData(): IUser | null {
    let userLocal: string | null = localStorage.getItem('user');
    // @ts-ignore
    console.log(userLocal.toString());
    if (userLocal !== null) return JSON.parse(userLocal) as IUser;

    return null;
  }

  private register(username: string, password: string, email: string, apiUrl: string) {
    let promise: any = new Promise((resolve, reject) => {
      let url = environment.HOST + apiUrl;
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
            this.snackBar.successMessage('Success!');
            this.router.navigate(['account-activation']);
          },
          (error) => {
            if (error.error.username && error.error.password) {
              this.snackBar.warningMessage('User already exists and password is too weak or unacceptable symbols');
            } else if (error.error.password) {
              this.snackBar.warningMessage('Password is too weak or unacceptable symbols');
            } else if (error.error.username || error.error.email) {
              this.snackBar.warningMessage('User already exists or unacceptable symbols');
            } else {
              this.snackBar.errorMessage('Service unavailable. Try again later.');
            }
          }
        );
    });
    return promise;
  }

  registerCustomer(username: string, password: string, email: string) {
    this.register(username, password, email, '/api/customers/');
  }
}
