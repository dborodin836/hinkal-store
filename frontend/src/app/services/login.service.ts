import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Router} from "@angular/router";

const baseUrl = 'http://localhost:8000/auth/';
// let headers = new HttpHeaders({'Authorization': 'Token f8893cfcd3b0e4b4be269bb647678b1ffaa0c33c'})

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private response: any;
  private token = "";

  constructor(private http: HttpClient,
              private router: Router) {
  }

  getToken(): string | undefined {
    return this.token
  }

  getAuthHeader() {
    return new HttpHeaders({'Authorization': 'Token ' + this.getToken()})
  }

  logout() {
    // @ts-ignore
    let headers = new HttpHeaders({'Authorization': 'Token ' + this.token})
    this.http.post(baseUrl + 'token/logout/', '', {headers: headers})
    this.token='';
    this.router.navigate(['success'])
  }

  login(data: { username: any; password: any; }) {
    this.http.post<any>(baseUrl + 'token/login/', data,)
      .subscribe(data => {
        console.log(data.auth_token)
        this.token = data.auth_token
      })
    console.log(this.response)
    return this.response
  }

  isAuthorized(): boolean {
    return this.token != ''
  }
}
