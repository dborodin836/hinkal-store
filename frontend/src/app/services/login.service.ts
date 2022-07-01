import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {Router} from "@angular/router";

const baseUrl = 'http://localhost:8000/auth/';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private auth_token = "";
  private user = {};

  constructor(private http: HttpClient,
              private router: Router) {
  }

  getToken(): string | undefined {
    return this.auth_token
  }

  getAuthHeader() {
    return new HttpHeaders({'Authorization': 'Token ' + this.getToken()})
  }

  logout() {
    // @ts-ignore
    console.log(this.auth_token)
    this.http.post(baseUrl + 'token/logout/', '', {headers: this.getAuthHeader()}).subscribe()
    this.auth_token='';
    this.router.navigate(['success'])
  }

  login(data: { username: any; password: any; }) {
    let promise = new Promise((resolve, rejectt) => {
      this.http.post<any>(baseUrl + 'token/login/', data,)
        .toPromise()
        .then(
          res => {
            this.auth_token = res.auth_token
            console.log(res.auth_token)
          }
        )
    })
  }

  isAuthorized(): boolean {
    return this.auth_token != ''
  }

  getUser() {
    let url = baseUrl + "users/me/"
    // @ts-ignore
    this.http.get<HttpResponse<any>>(url, {observe:"response", responseType:"json", headers: this.getAuthHeader()}).subscribe
  }
}
