import {Component, OnInit, Output} from '@angular/core';
import {DishService} from "../services/dish.service";
import {DishModel} from "../models/dish.model";
import {HttpResponse} from "@angular/common/http";
import {PageEvent} from "@angular/material/paginator";
import {PaginatedResponseModel} from "../models/paginator.model";


@Component({
  selector: 'app-store',
  templateUrl: './store.component.html',
  styleUrls: ['./store.component.css']
})
export class StoreComponent implements OnInit {

  constructor(private dishService: DishService) { }

  dishes?: DishModel[]

  pageEvent: PageEvent | undefined;
  datasource?: null;
  pageIndex?:number;
  pageSize?:number;
  length?:number;

  ngOnInit(): void {
    this.retrieveDishes();
  }

  retrieveDishes() {
    this.dishService.getAll().subscribe((data:HttpResponse<any>) => {
      console.log(data.body.results);
      this.dishes = data.body.results
    })
      }


  public getServerData(event?:PageEvent){
    let response = this.dishService.getPaginated(event)
    // @ts-ignore
    this.datasource = response.results;
    this.pageIndex = event?.pageIndex;
    this.pageSize = event?.pageSize;
    // @ts-ignore
    this.length = response.count;
    console.log(event)
    return event
  }

}
