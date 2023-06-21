import {Injectable} from '@angular/core';
import {HttpClient, HttpResponse} from '@angular/common/http';
import {PageEvent} from '@angular/material/paginator';
import {environment} from '../../environments/environment';
import {of} from 'rxjs';

const baseUrl = new URL(`${environment.HOST}/api/dish/`);

@Injectable({
  providedIn: 'root',
})
export class DishService {
  constructor(private http: HttpClient) {
  }

  getMultiple(list: any) {
    let url = `${baseUrl}?id=${list.join(',')}`;
    return this.http.get<HttpResponse<any>>(url, {observe: 'response', responseType: 'json'});
  }

  getDetail(id: string) {
    let url = baseUrl + id + '/';
    return this.http.get<HttpResponse<any>>(url, {observe: 'response', responseType: 'json'});
  }

  getList(event: PageEvent | undefined, keyword: string, ordering: string, filtered_category: string) {
    if (event === undefined) {
      return of(new HttpResponse<any>({body: {count: 0, results: []}}))
    }

    let offset = event.pageSize * event.pageIndex
    baseUrl.searchParams.append("offset", offset.toString());
    baseUrl.searchParams.append("limit", event.pageSize.toString());

    if (keyword != '')
      baseUrl.searchParams.append("query_keyword", keyword);

    if (ordering != 'popular')
      baseUrl.searchParams.append("ordering", ordering);

    if (filtered_category != 'all')
      baseUrl.searchParams.append("filtered_category", filtered_category);

    console.log(baseUrl.toString())
    return this.http.get<HttpResponse<any>>(baseUrl.toString(), {observe: 'response', responseType: 'json'});
  }

  getBestSelling() {
    return this.http.get<HttpResponse<any>>(baseUrl.toString(), {observe: 'response', responseType: 'json'});
  }
}
