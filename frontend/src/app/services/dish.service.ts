import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { PageEvent } from '@angular/material/paginator';

const baseUrl = 'http://localhost:8000/api/dish/';

@Injectable({
  providedIn: 'root',
})
export class DishService {
  constructor(private http: HttpClient) {}

  getMultiple(list: any) {
    let url = baseUrl + '?id=' + list.join(',');
    return this.http.get<HttpResponse<any>>(url, { observe: 'response', responseType: 'json' });
  }

  getDetail(id: string | undefined) {
    let url = baseUrl + id;
    return this.http.get<HttpResponse<any>>(url, { observe: 'response', responseType: 'json' });
  }

  getPaginated(event: PageEvent | undefined) {
    // @ts-ignore
    let url = baseUrl + '?' + 'offset=' + event.pageSize * event.pageIndex + '&limit=' + event.pageSize;
    return this.http.get<HttpResponse<any>>(url, { observe: 'response', responseType: 'json' });
  }

  getList(event: PageEvent | undefined, keyword: string, ordering: string, filtered_category: string) {
    // @ts-ignore
    let url = baseUrl + '?' + 'offset=' + event.pageSize * event.pageIndex + '&limit=' + event.pageSize;
    console.log(keyword);
    if (keyword != '') {
      url += '&query_keyword=' + keyword;
    }
    if (ordering != 'popular') {
      url += '&ordering=' + ordering;
    }
    if (filtered_category != 'all') {
      url += '&filtered_category=' + filtered_category;
    }
    console.log(url);
    return this.http.get<HttpResponse<any>>(url, { observe: 'response', responseType: 'json' });
  }

  getBestSelling() {
    return this.http.get<HttpResponse<any>>(baseUrl, { observe: 'response', responseType: 'json' });
  }
}
