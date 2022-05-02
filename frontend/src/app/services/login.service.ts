import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";

const baseUrl = 'http://localhost:8000/auth/token/login/';
const headers = new HttpHeaders({'Authorization': 'Token f8893cfcd3b0e4b4be269bb647678b1ffaa0c33c'})

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private response: any;

  constructor(private http: HttpClient) { }

  login(data: { username: any; password: any; }) {
    this.http.post<any>(baseUrl, data, {headers: headers})
      .subscribe(data => {
      this.response = data
    })
    console.log(this.response)
    return this.response
  }
}
