import { Component, OnInit } from '@angular/core';
import { DishService } from '../services/dish.service';
import { DishModel } from '../models/dish.model';
import { HttpResponse } from '@angular/common/http';
import { PageEvent } from '@angular/material/paginator';
import { CartService } from '../services/cart.service';

@Component({
  selector: 'app-store',
  templateUrl: './store.component.html',
  styleUrls: ['./store.component.css'],
})
export class StoreComponent implements OnInit {
  constructor(private dishService: DishService, private cartService: CartService) {}

  dishes?: DishModel[];

  pageIndex?: number;
  pageSize?: number;
  length?: number;
  filtered_category = 'all';
  ordering = 'popular';
  keyword = '';

  ngOnInit(): void {
    // @ts-ignore
    this.getServerData({ pageIndex: 0, pageSize: 25 });
  }

  getServerData(event?: PageEvent) {
    if (typeof event == 'undefined') {
      var myevent = { pageIndex: 0, pageSize: 25 };
    } else {
      // @ts-ignore
      var myevent = event;
    }
    // @ts-ignore
    this.dishService
      // @ts-ignore
      .getList(myevent, this.keyword, this.ordering, this.filtered_category)
      .subscribe((data: HttpResponse<any>) => {
        this.dishes = data.body.results;
        this.length = data.body.count;
      });
    console.log(this.dishes);
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

  addToCart(id: number) {
    this.cartService.addItem(id);
  }
}
