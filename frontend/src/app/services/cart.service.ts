import { Injectable } from '@angular/core';
import { DishService } from './dish.service';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { LoginService } from './login.service';
import { environment } from '../../environments/environment';

const baseUrl = `${environment.HOST}/api/order/`;

@Injectable({
  providedIn: 'root',
})
export class CartService {
  // ID's and amount [{"id": 123, "amount": 2}]
  cartIdList: any[] = [];

  constructor(private dishService: DishService, private http: HttpClient, private loginService: LoginService) {
    if (localStorage.getItem('cartIdList') != null) {
      // @ts-ignore
      this.cartIdList = JSON.parse(localStorage.getItem('cartIdList'));
    }
  }
  isInCart(id: number): boolean {
    // @ts-ignore
    this.cartIdList = JSON.parse(localStorage.getItem('cartIdList'));
    return this.cartIdList.some((item) => item.id === id);
  }

  addItem(id: number) {
    // @ts-ignore
    this.cartIdList.push({
      id: id,
      amount: 1,
    });
    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  checkDiscountCode(code: string) {
    let url = `${environment.HOST}/api/discount/${code}`;
    return this.http.get<HttpResponse<any>>(url, {
      observe: 'response',
      responseType: 'json',
      headers: this.loginService.getAuthHeader(),
    });
  }

  createOrder() {
    let data = {
      details: [],
      // @ts-ignore
      ordered_by: this.loginService.getUserData()['id'],
    };
    // @ts-ignore
    this.cartIdList.forEach((x) => data['details'].push({ item: x['id'], amount: x['amount'] }));
    this.http
      .post(baseUrl, data, { observe: 'response', responseType: 'json', headers: this.loginService.getAuthHeader() })
      .subscribe();
  }

  increaseAmount(id: number) {
    let item = this.cartIdList.find((x) => x['id'] == id);
    let index = this.cartIdList.indexOf(item);
    item.amount += 1;
    this.cartIdList[index] = item;
    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  decreaseAmount(id: number) {
    let item = this.cartIdList.find((x) => x['id'] == id);
    let index = this.cartIdList.indexOf(item);
    if (item.amount != 1) {
      item.amount -= 1;
    }
    this.cartIdList[index] = item;
    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  getDataFromAPI() {
    let payload: any[] = [];
    this.cartIdList.forEach(function (x: any) {
      payload.push(x.id);
    });
    return this.dishService.getMultiple(payload);
  }

  isHaveData() {
    return this.cartIdList.length != 0;
  }

  deleteItem(id: number) {
    // @ts-ignore
    const cartIdList = JSON.parse(localStorage.getItem('cartIdList')) || [];

    // Remove any items with matching id
    const filteredCart = cartIdList.filter((item: { id: number }) => item.id !== id);

    // Write updated list back to localStorage
    localStorage.setItem('cartIdList', JSON.stringify(filteredCart));
  }

  getAmount(id: number) {
    let item = this.cartIdList.find((x) => x['id'] == id);
    return item['amount'];
  }
}
