import {Component, OnInit} from '@angular/core';
import {DishService} from "../services/dish.service";
import {DishModel} from "../models/dish.model";
import {HttpResponse} from "@angular/common/http";
import {PageEvent} from "@angular/material/paginator";


@Component({
  selector: 'app-store',
  templateUrl: './store.component.html',
  styleUrls: ['./store.component.css']
})
export class StoreComponent implements OnInit {

  constructor(private dishService: DishService) { }

  dishes?: DishModel[]

  pageIndex?:number;
  pageSize?:number;
  length?: number;

  ngOnInit(): void {
    // @ts-ignore
    this.getServerData({pageIndex: 0, pageSize:25})
  }

  getServerData(event?:PageEvent){
    console.log(event)
    this.dishService.getPaginated(event)
      .subscribe((data:HttpResponse<any>) => {
        this.dishes = data.body.results;
        this.length = data.body.count})
    return event
  }

}
