import {Component, OnInit} from '@angular/core';
import {CartService} from '../services/cart.service';
import {HttpClient, HttpResponse} from '@angular/common/http';
import {LoginService} from "../services/login.service";
import {Router} from "@angular/router";
import {MatSnackBar} from "@angular/material/snack-bar";
import {environment} from "../../environments/environment";

const baseUrl = `${environment.HOST}/auth/`;

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
    private snackBar: MatSnackBar
    ) { }

  listDishes: any[] = [];

  ngOnInit(): void {
    if (this.cartService.isHaveData()) {
      this.cartService.getDataFromAPI().subscribe((data: HttpResponse<any>) => {
        this.listDishes = data.body.results;
        console.log(data.body.results);
      });
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
    let index = this.listDishes.indexOf(item);
    if (index != -1) {
      this.listDishes.splice(index, 1);
    }
  }

  getAmount(id: number) {
    return this.cartService.getAmount(id);
  }

  createOrder() {
    if (!this.loginService.isAuthorized()) {
      this.router.navigate(['login']);
      this.snackBar.open('Please login or register.', 'X', {
        duration: 7000,
        horizontalPosition: 'end',
      });
    }
    this.cartService.createOrder();
  }

  checkDiscountCode() {
    // this.http.get()
  }

  getTotalPrice() {
    let accumulator = 0;
    this.listDishes.forEach((x) => (accumulator += Number(x.price) * this.cartService.getAmount(x.id)));
    return accumulator;
  }

  getSubPrice(id: number) {
    let item = this.listDishes.find((x) => x['id'] == id);
    return item.price * this.cartService.getAmount(item.id);
  }
}
