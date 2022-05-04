import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {Observable} from "rxjs";
import {PageEvent} from "@angular/material/paginator";
import {LoginService} from "./login.service";
import {PaginatedResponseModel} from "../models/paginator.model";


const baseUrl = 'http://localhost:8000/api/dish/';
const headers = new HttpHeaders({'Authorization': 'Token f8893cfcd3b0e4b4be269bb647678b1ffaa0c33c'})

@Injectable({
  providedIn: 'root'
})
export class DishService {
  constructor(private http: HttpClient,
              private loginService: LoginService) {
  }

  getAll(): Observable<HttpResponse<any>>{
    return this.http.get<HttpResponse<any>>(baseUrl, {headers: headers, observe: 'response', responseType: 'json'});
  }

  // @ts-ignore
  getPaginated(event: PageEvent | undefined): PaginatedResponseModel {
    // @ts-ignore
    let url = baseUrl + '?' + 'offset=' + event.pageSize * event.pageIndex + '&limit=' + event.pageSize
    let headers = this.loginService.getAuthHeader()
      .set('observe', 'response')
      .set('responseType', 'json')
    console.log(headers)
    console.log(url)

    this.http.get<HttpResponse<any>>(url, {headers: headers})
      .subscribe((data:HttpResponse<any>) => {
        console.log(data.body.results);
        return data.body
      })
  }
}



