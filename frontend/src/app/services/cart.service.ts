import { Injectable } from '@angular/core';
import {DishService} from "./dish.service";

@Injectable({
  providedIn: 'root'
})
export class CartService {

  constructor(private dishService: DishService) { }

  addItem(id: number) {
    // @ts-ignore
    this.cartList.push(id)
  }

  createOrder() {
    // this.http.post()
  }

  getData(list: any) {
    return this.dishService.getMultiple(list)
  }
}
