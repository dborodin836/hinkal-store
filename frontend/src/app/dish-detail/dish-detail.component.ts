import { Component, OnInit } from '@angular/core';
import { DishService } from '../services/dish.service';
import { Dish } from '../models/dish';
import { Router } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { CartService } from '../services/cart.service';

@Component({
  selector: 'app-dish-detail',
  templateUrl: './dish-detail.component.html',
  styleUrls: ['./dish-detail.component.scss'],
})
export class DishDetailComponent implements OnInit {
  constructor(private dishService: DishService, private router: Router, private cartService: CartService) {}

  public id?: string;

  dish: Dish = {
    title: '...',
    description: '...',
    id: 'id',
    image: '',
    is_active: true,
    price: 0,
  };

  ngOnInit(): void {
    let routerUrl = this.router.url;
    this.id = routerUrl.split('/').at(-1);

    if (this.id !== undefined) this.getDetailedData(this.id);
  }

  getDetailedData(id: string) {
    this.dishService.getDetail(id).subscribe((data: HttpResponse<any>) => {
      this.dish = data.body;
    });
  }

  addToCart(id: any) {
    this.cartService.addItem(id);
  }
}
