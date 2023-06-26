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
  cartIdList?: { id: number; amount: number }[] = [];

  constructor(private dishService: DishService, private http: HttpClient, private loginService: LoginService) {
    let cartIDListStorage: string | null = localStorage.getItem('cartIdList');
    if (cartIDListStorage != null) this.cartIdList = JSON.parse(cartIDListStorage);
  }

  isInCart(id: number): boolean {
    let cartIDListStorage: string | null = localStorage.getItem('cartIdList');
    if (cartIDListStorage == null) return false;

    this.cartIdList = JSON.parse(cartIDListStorage);

    return this.cartIdList ? this.cartIdList.some((item) => item.id === id) : false;
  }

  addItem(id: number) {
    if (this.cartIdList == null) return;

    this.cartIdList.push({
      id: id,
      amount: 1,
    });
    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  checkDiscountCode(code: string) {
    let url = `${environment.HOST}/api/code/${code}`;
    return this.http.get<any>(url, {
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

  increaseAmount(id: number): void {
    if (this.cartIdList == null) return;

    let item = this.cartIdList.find((x) => x['id'] == id);
    if (item == null) return;

    let index = this.cartIdList.indexOf(item);
    item.amount += 1;
    this.cartIdList[index] = item;

    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  decreaseAmount(id: number): void {
    if (this.cartIdList == null) return;

    let item = this.cartIdList.find((x) => x['id'] == id);
    if (item == null) return;

    let index = this.cartIdList.indexOf(item);
    if (item.amount != 1) {
      item.amount -= 1;
    }
    this.cartIdList[index] = item;

    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  getDataFromAPI() {
    if (this.cartIdList == null) return;

    let payload: any[] = [];

    this.cartIdList.forEach(function (x: any) {
      payload.push(x.id);
    });
    return this.dishService.getMultiple(payload);
  }

  isHaveData(): boolean {
    if (this.cartIdList == null) return false;
    return this.cartIdList.length != 0;
  }

  deleteItem(id: number) {
    let cartIDListStorage: string | null = localStorage.getItem('cartIdList');
    if (cartIDListStorage == null) return;

    const cartIdList = JSON.parse(cartIDListStorage) || [];

    // Remove any items with matching id
    const filteredCart = cartIdList.filter((item: { id: number }) => item.id !== id);

    // Write updated list back to localStorage
    localStorage.setItem('cartIdList', JSON.stringify(filteredCart));
  }

  getAmount(id: number) {
    if (this.cartIdList == null) return 0;

    let item = this.cartIdList.find((x) => x['id'] == id);
    if (item == null) return 0;

    return item['amount'];
  }
}
