import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {PageEvent} from "@angular/material/paginator";


const baseUrl = 'http://localhost:8000/api/dish/';
const headers = new HttpHeaders({'Authorization': 'Token fed08596034ae7fe1ba752a85deeb19a37dae4b2'})

@Injectable({
  providedIn: 'root'
})
export class DishService {
  constructor(private http: HttpClient) {
  }

  getDetail(id: string | undefined) {
    let url = baseUrl + id;
    return this.http.get<HttpResponse<any>>(url, {headers: headers, observe:"response", responseType:"json"})
  }

  getPaginated(event: PageEvent | undefined) {
    // @ts-ignore
    let url = baseUrl + '?' + 'offset=' + event.pageSize * event.pageIndex + '&limit=' + event.pageSize
    return this.http.get<HttpResponse<any>>(url, {headers: headers, observe:"response", responseType:"json"})
      }
}



