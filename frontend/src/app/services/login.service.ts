import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {Router} from "@angular/router";
import { UserModel } from '../models/user.model';

const baseUrl = 'http://localhost:8000/auth/';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private auth_token = "";
  private user: UserModel = {};

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
    this.user = {}
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
            this.getUser()
          }
        )
    })
    return promise
  }

  isAuthorized(): boolean {
    return this.auth_token != ''
  }

  getUser() {
    let promise = new Promise((resolve, rejectt) => {
      let url = baseUrl + "users/me/"
      this.http.get(url, {observe:"response", responseType:"json", headers: this.getAuthHeader()})
        .toPromise()
        .then(
          res => {
            // @ts-ignore
            this.user = res.body
          }
        )
    })
    return promise
  }

  getUserData() {
    return this.user
  }

  register(username: string, password: string) {
    let url = baseUrl + "users/"
    this.http.post(url, {"username": username, "password": password}, {observe:"response", responseType:"json", headers: this.getAuthHeader()})
  }
}
