import { Component, OnInit, ViewContainerRef } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Dish } from '../models/dish';
import { DishService } from '../services/dish.service';
import { CartService } from '../services/cart.service';
import { SnackBarMessagesService } from '../services/messages.service';
import { LoaderService } from '../services/loader.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  bestSellingDishes?: Dish[];

  constructor(
    private dishService: DishService,
    private cartService: CartService,
    private loaderService: LoaderService,
    private viewContainerRef: ViewContainerRef,
    private messagesService: SnackBarMessagesService
  ) {}

  ngOnInit(): void {
    this.getBestSellingDishes();
    this.loaderService.setRootViewContainerRef(this.viewContainerRef);
    this.loaderService.addLoader();
  }

  getBestSellingDishes() {
    this.dishService.getBestSelling().subscribe(
      (data: HttpResponse<any>) => {
        this.bestSellingDishes = data.body.results;
        this.loaderService.removeLoader();
      },
      (error) => {
        this.messagesService.errorMessage('Error happened while loading data.');
        this.loaderService.removeLoader();
      }
    );
  }

  isInCart(id: number) {
    return this.cartService.isInCart(id);
  }

  addToCart(id: number) {
    this.cartService.addItem(id);
  }
}
