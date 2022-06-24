import {Component, OnInit} from '@angular/core';
import {CartService} from "../services/cart.service";
import {HttpResponse} from "@angular/common/http";
import {DishModel} from "../models/dish.model";

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {

  constructor(private cartService: CartService) {
  }

  cartList: any[] = [1, 121, 12]

  listDishes: any[] = []

  ngOnInit(): void {
    if (this.cartList.length != 0) {
      this.cartService.getData(this.cartList)
        .subscribe((data: HttpResponse<any>) => {
          this.listDishes = data.body.results
          console.log(data.body.results)
        })
    }
  }

  decAmount(id: any) {
    console.log(id)
  }

  incAmount(id: any) {
    console.log(id)
  }
}
