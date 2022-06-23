import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CartService {

  cartList = []

  constructor(private http: HttpClient) { }

  addItem(id: number) {
    // @ts-ignore
    this.cartList.push(id)
  }

  createOrder() {
    this.http.post()
  }
}
