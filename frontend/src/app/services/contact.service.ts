import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UntypedFormGroup } from '@angular/forms';
import { environment } from '../../environments/environment';

const baseUrl = `${environment.HOST}/api/contact/`;
const headers = new HttpHeaders({ Authorization: 'Token f8893cfcd3b0e4b4be269bb647678b1ffaa0c33c' });

@Injectable({
  providedIn: 'root',
})
export class ContactService {
  private response: any;

  constructor(private http: HttpClient) {}

  sendPost(userData: UntypedFormGroup): Observable<HttpResponse<any>> {
    this.http.post<any>(baseUrl, userData, { headers: headers }).subscribe((data) => {
      this.response = data;
    });
    return this.response;
  }
}
