import { Component, OnInit } from '@angular/core';
import { CartService } from '../services/cart.service';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { LoginService } from '../services/login.service';
import { Router } from '@angular/router';
import { Dish } from '../models/dish';
import { SnackBarService } from '../services/snack-bar.service';

interface Discount {
  name: string;
  description?: string;
  discount_word: string;
  discount_amount: number;
}

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css'],
})
export class CheckoutComponent implements OnInit {
  constructor(
    private cartService: CartService,
    private http: HttpClient,
    private loginService: LoginService,
    private router: Router,
    private snackBar: SnackBarService
  ) {}

  discountCode: string = '';
  discount?: Discount;

  listDishes: Array<Dish> = [];

  ngOnInit(): void {
    if (this.cartService.isHaveData()) {
      const dataObservable = this.cartService.getDataFromAPI();

      if (dataObservable === undefined) return;

      dataObservable.subscribe((data: HttpResponse<any>) => {
        this.listDishes = data.body.results;
      });

      this.discount = undefined;
    }
  }

  decAmount(id: number) {
    this.cartService.decreaseAmount(id);
  }

  incAmount(id: number) {
    this.cartService.increaseAmount(id);
  }

  delItem(id: number) {
    this.cartService.deleteItem(id);
    let item = this.listDishes.find((x) => x['id'] == id);
    if (item) {
      let index = this.listDishes.indexOf(item);
      if (index != -1) {
        this.listDishes.splice(index, 1);
      }
    }
  }

  getAmount(id: number) {
    return this.cartService.getAmount(id);
  }

  createOrder() {
    if (!this.loginService.isAuthorized()) {
      this.router.navigate(['login']);
      this.snackBar.openSnackBar('Please login or register.', undefined, undefined, 'warning');
    }
    this.cartService.createOrder();
  }

  async checkDiscountCode(event: any) {
    let response = await this.cartService.checkDiscountCode(event.target.value);
    response.subscribe(
      (data: HttpResponse<any>) => {
        if (data?.body) {
          this.discount = data.body;
        }
      },
      (error: Error) => {
        this.snackBar.openSnackBar('Promo-code is not valid.', undefined, undefined, 'error');
      }
    );
  }

  getTotalPrice() {
    let accumulator = 0;
    this.listDishes.forEach((x) => (accumulator += Number(x.price) * this.cartService.getAmount(x.id)));
    return accumulator;
  }

  getSubPrice(id: number) {
    let item = this.listDishes.find((x) => x['id'] == id);
    if (item) return item.price * this.cartService.getAmount(item.id);
    return -1;
  }
}
