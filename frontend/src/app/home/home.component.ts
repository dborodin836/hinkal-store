import { Component, OnInit } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { DishModel } from '../models/dish.model';
import { DishService } from '../services/dish.service';
import { CartService } from '../services/cart.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  bestSellingDishes?: DishModel[];

  constructor(private dishService: DishService, private cartService: CartService) {}

  ngOnInit(): void {
    this.getBestSellingDishes();
  }

  getBestSellingDishes() {
    this.dishService.getBestSelling().subscribe((data: HttpResponse<any>) => {
      this.bestSellingDishes = data.body.results;
    });
  }

  addToCart(id: number) {
    this.cartService.addItem(id);
  }
}
