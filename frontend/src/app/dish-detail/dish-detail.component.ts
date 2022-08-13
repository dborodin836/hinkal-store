import { Component, OnInit } from '@angular/core';
import { DishService } from '../services/dish.service';
import { DishModel } from '../models/dish.model';
import { Router } from '@angular/router';
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-dish-detail',
  templateUrl: './dish-detail.component.html',
  styleUrls: ['./dish-detail.component.scss'],
})
export class DishDetailComponent implements OnInit {
  constructor(private dishService: DishService, private router: Router) {}

  public id?: string;

  dish: DishModel = {
    title: '...',
    description: '...',
    id: 'id',
    image: '',
    is_active: true,
    price: 0,
  };

  ngOnInit(): void {
    this.id = this.router.url[this.router.url.length - 1];
    this.getDetailedData(this.id);
  }

  getDetailedData(id: string) {
    this.dishService.getDetail(id).subscribe((data: HttpResponse<any>) => {
      this.dish = data.body;
    });
  }
}
