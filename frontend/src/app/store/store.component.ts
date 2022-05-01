import { Component, OnInit } from '@angular/core';
import {DishService} from "../services/dish.service";
import {DishModel} from "../models/dish.model";
import {HttpResponse} from "@angular/common/http";


@Component({
  selector: 'app-store',
  templateUrl: './store.component.html',
  styleUrls: ['./store.component.css']
})
export class StoreComponent implements OnInit {

  constructor(private dishService: DishService) { }

  dishes?: DishModel[]

  ngOnInit(): void {
    this.retrieveDishes();
  }

  retrieveDishes() {
    this.dishService.getAll().subscribe((data:HttpResponse<any>) => {
      console.log(data.body.results);
      this.dishes = data.body.results
    })
      }

}
