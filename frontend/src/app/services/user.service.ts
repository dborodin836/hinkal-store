import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HOST } from '../app.module';

const baseUrl = HOST + '/auth/users';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}

  getAll(): Observable<HttpResponse<any>> {
    return this.http.get<HttpResponse<any>>(baseUrl, { observe: 'response', responseType: 'json' });
  }
}
