import {Component, OnInit} from '@angular/core';
import {DishService} from '../services/dish.service';
import {DishModel} from '../models/dish.model';
import {HttpResponse} from '@angular/common/http';
import {PageEvent} from '@angular/material/paginator';
import {CartService} from '../services/cart.service';

@Component({
  selector: 'app-store',
  templateUrl: './store.component.html',
  styleUrls: ['./store.component.css'],
})
export class StoreComponent implements OnInit {
  constructor(private dishService: DishService, private cartService: CartService) {
  }

  dishes?: DishModel[];

  pageIndex?: number;
  pageSize?: number;
  length?: number;
  filtered_category = 'all';
  ordering = 'popular';
  keyword = '';

  ngOnInit(): void {
    this.getServerData();
  }

  getServerData(event?: PageEvent) {
    if (event === undefined) {
      event = new PageEvent;
      event.pageIndex = 0;
      event.pageSize = 25;
    }

    this.dishService
      .getList(event, this.keyword, this.ordering, this.filtered_category)
      .subscribe((data: HttpResponse<any>) => {
        this.dishes = data.body.results;
        this.length = data.body.count;
      });

    return event;
  }

  onChangeCategory(event: any) {
    console.log(event.target.value);
    this.getServerData();
  }

  onChangeOrdering(event: any) {
    console.log(event.target.value);
    this.getServerData();
  }

  onChangeText(event: any) {
    console.log(event.target.value);
    this.keyword = event.target.value;
    this.getServerData();
  }

  isInCart(id: number) {
    return this.cartService.isInCart(id);
  }

  addToCart(id: number) {
    this.cartService.addItem(id);
  }
}
