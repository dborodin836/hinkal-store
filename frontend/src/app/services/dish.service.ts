import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { PageEvent } from '@angular/material/paginator';
import { environment } from '../../environments/environment';
import { of } from 'rxjs';

const baseUrl = new URL(`${environment.HOST}/api/dish/`);

@Injectable({
  providedIn: 'root',
})
export class DishService {
  constructor(private http: HttpClient) {}

  getMultiple(list: any) {
    let url = `${baseUrl}?id=${list.join(',')}`;
    return this.http.get<HttpResponse<any>>(url, { observe: 'response', responseType: 'json' });
  }

  getDetail(id: string) {
    let url = baseUrl + id + '/';
    return this.http.get<HttpResponse<any>>(url, { observe: 'response', responseType: 'json' });
  }

  getList(event: PageEvent | undefined, keyword: string, ordering: string, filtered_category: string) {
    if (event === undefined) {
      return of(new HttpResponse<any>({ body: { count: 0, results: [] } }));
    }

    let url = new URL(baseUrl)
    let offset = event.pageSize * event.pageIndex;

    url.searchParams.append('offset', offset.toString());
    url.searchParams.append('limit', event.pageSize.toString());

    if (keyword != '') url.searchParams.append('query_keyword', keyword);

    if (ordering != 'popular') url.searchParams.append('ordering', ordering);

    if (filtered_category != 'all') url.searchParams.append('filtered_category', filtered_category);

    console.log(url.toString());
    return this.http.get<HttpResponse<any>>(url.toString(), { observe: 'response', responseType: 'json' });
  }

  getBestSelling() {
    return this.http.get<HttpResponse<any>>(baseUrl.toString(), { observe: 'response', responseType: 'json' });
  }
}
