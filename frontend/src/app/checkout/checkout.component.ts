import {Component, OnInit} from '@angular/core';
import {CartService} from "../services/cart.service";
import {HttpResponse} from "@angular/common/http";

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {

  constructor(private cartService: CartService) {
  }


  listDishes: any[] = []

  ngOnInit(): void {
    if (this.cartService.isHaveData()) {
      this.cartService.getDataFromAPI()
        .subscribe((data: HttpResponse<any>) => {
          this.listDishes = data.body.results
          console.log(data.body.results)
        })
    }
  }

  decAmount(id: number) {
    this.cartService.decreaseAmount(id)
  }

  incAmount(id: number) {
    this.cartService.increaseAmount(id)
  }

  delItem(id: number) {
    this.cartService.deleteItem(id)
    let item = this.listDishes.find(x => x["id"] == id)
    let index = this.listDishes.indexOf(item)
    if (index != -1) {
      this.listDishes.splice(index, 1)
    }
  }
}
