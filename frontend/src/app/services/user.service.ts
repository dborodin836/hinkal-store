import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HOST } from '../conf';

const baseUrl = HOST + '/auth/users';
const headers = new HttpHeaders({ Authorization: 'Token f8893cfcd3b0e4b4be269bb647678b1ffaa0c33c' });

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}

  getAll(): Observable<HttpResponse<any>> {
    return this.http.get<HttpResponse<any>>(baseUrl, { headers: headers, observe: 'response', responseType: 'json' });
  }
}
