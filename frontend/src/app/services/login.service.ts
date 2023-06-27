import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from '@angular/common/http';
import {Router} from '@angular/router';
import {environment} from '../../environments/environment';
import {SnackBarService} from "./snack-bar.service";

const baseUrl = `${environment.HOST}/auth/`;

interface ICredentials {
  username: string,
  password: string
}

export interface IUser {
  email: string,
  id: number,
  username: string
}

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  constructor(
    private http: HttpClient,
    private router: Router,
    private snackBar: SnackBarService
  ) {
  }

  getToken(): string | null {
    return localStorage.getItem('auth_token');
  }

  getAuthHeader() {
    return new HttpHeaders({Authorization: `Token ${this.getToken()}`});
  }

  logout() {
    return new Promise<HttpResponse<any>>((resolve, reject) => {
      this.http
        .post(`${baseUrl}token/logout/`, '', {headers: this.getAuthHeader()})
        .toPromise()
        .then(
          () => {
            localStorage.removeItem('auth_token');
            localStorage.removeItem('user');
            this.router.navigate(['']);
            this.snackBar.openSnackBar('You are logged out.', undefined, undefined, "success");
          },
          () => {
            this.snackBar.openSnackBar('Service unavailable. Try again later.', undefined, undefined, "error");
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
            this.snackBar.openSnackBar('You are logged in.', undefined, undefined, "success");
          },
          (error) => {
            if (error.error.username) {
              this.snackBar.openSnackBar('User does not exists', undefined, undefined, "warning");
            } else if (error.error.password) {
              this.snackBar.openSnackBar('Wrong password', undefined, undefined, "warning");
            } else {
              this.snackBar.openSnackBar('Service unavailable. Try again later.', undefined, undefined, "error");
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
    return this.http.get(url, {observe: 'response', responseType: 'json', headers: this.getAuthHeader()}).toPromise()
  }

  getUserData(): IUser | null {
    let userLocal: string | null = localStorage.getItem('user');
    // @ts-ignore
    console.log(userLocal.toString());
    if (userLocal !== null)
      return JSON.parse(userLocal) as IUser;

    return null
  }

  private register(username: string, password: string, email: string, apiUrl: string) {
    let promise: any = new Promise((resolve, reject) => {
      let url = environment.HOST + apiUrl;
      this.http
        .post(
          url,
          {username: username, password: password, email: email},
          {
            observe: 'response',
            responseType: 'json',
          }
        )
        .toPromise()
        .then(
          () => {
            this.snackBar.openSnackBar('Success!', undefined, undefined, "success");
            this.router.navigate(['account-activation']);
          },
          (error) => {
            if (error.error.username && error.error.password) {
              this.snackBar.openSnackBar('User already exists and password is too weak or unacceptable symbols', undefined, undefined, "warning");
            } else if (error.error.password) {
              this.snackBar.openSnackBar('Password is too weak or unacceptable symbols', undefined, undefined, "warning");
            } else if (error.error.username || error.error.email) {
              this.snackBar.openSnackBar('User already exists or unacceptable symbols', undefined, undefined, "warning");
            } else {
              this.snackBar.openSnackBar('Service unavailable. Try again later.', undefined, undefined, "error");
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
