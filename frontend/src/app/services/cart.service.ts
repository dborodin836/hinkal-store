import {Injectable} from '@angular/core';
import {DishService} from "./dish.service";
import {HttpClient} from "@angular/common/http";

const baseUrl = "http://localhost:8000/api/dish/"

@Injectable({
  providedIn: 'root'
})
export class CartService {

  // ID's and amount [{"id": 123, "amount": 2}]
  cartIdList: any[] = []

  constructor(private dishService: DishService,
              private http: HttpClient) {
  }

  addItem(id: number) {
    // @ts-ignore
    this.cartIdList.push({
      "id": id,
      "amount": 1
    })

    console.log("Added item w/ id:" + id)
  }

  createOrder() {
    // this.http.post()
  }

  increaseAmount(id: number) {
    let item = this.cartIdList.find(x => x["id"] == id)
    let index = this.cartIdList.indexOf(item)
    item.amount += 1
    this.cartIdList[index] = item
  }

  decreaseAmount(id: number) {
    let item = this.cartIdList.find(x => x["id"] == id)
    let index = this.cartIdList.indexOf(item)
    if (item.amount != 1) {
      item.amount -= 1
    }
    this.cartIdList[index] = item
  }

  getDataFromAPI() {
    let payload: any[] = []
    this.cartIdList.forEach(function (x: any) {
      payload.push(x.id)
    })
    return this.dishService.getMultiple(payload)
  }

  isHaveData () {
    return this.cartIdList.length != 0
  }

  deleteItem(id: number) {
    let item = this.cartIdList.find(x => x["id"] == id)
    let index = this.cartIdList.indexOf(item)
    if (index != -1) {
      this.cartIdList.splice(index, 1)
    }
  }

  getAmount(id: number) {
    let item = this.cartIdList.find(x => x["id"] == id)
    return item["amount"]
  }
}
