import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {PageEvent} from "@angular/material/paginator";


const baseUrl = 'http://localhost:8000/api/dish/';

@Injectable({
  providedIn: 'root'
})
export class DishService {
  constructor(private http: HttpClient) {
  }

  getDetail(id: string | undefined) {
    let url = baseUrl + id;
    return this.http.get<HttpResponse<any>>(url, {observe:"response", responseType:"json"})
  }

  getPaginated(event: PageEvent | undefined) {
    // @ts-ignore
    let url = baseUrl + '?' + 'offset=' + event.pageSize * event.pageIndex + '&limit=' + event.pageSize
    return this.http.get<HttpResponse<any>>(url, {observe:"response", responseType:"json"})
      }
}



