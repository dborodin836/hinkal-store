import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {Observable} from "rxjs";
import {PageEvent} from "@angular/material/paginator";


const baseUrl = 'http://localhost:8000/api/dish/';
const headers = new HttpHeaders({'Authorization': 'Token 17ebb91980233f271fc7da6109701a72a9ef687d'})

@Injectable({
  providedIn: 'root'
})
export class DishService {
  constructor(private http: HttpClient) {
  }

  getAll(): Observable<HttpResponse<any>>{
    return this.http.get<HttpResponse<any>>(baseUrl, {headers: headers, observe: 'response', responseType: 'json'});
  }

  // @ts-ignore
  getPaginated(event: PageEvent | undefined) {
    // @ts-ignore
    let url = baseUrl + '?' + 'offset=' + event.pageSize * event.pageIndex + '&limit=' + event.pageSize
    return this.http.get<HttpResponse<any>>(url, {headers: headers, observe:"response", responseType:"json"})
      }
}



