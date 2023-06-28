import {Injectable} from '@angular/core';
import {DishService} from './dish.service';
import {HttpClient} from '@angular/common/http';
import {IUser, LoginService} from './login.service';
import {environment} from '../../environments/environment';
import {SnackBarMessagesService} from './messages.service';
import {Router} from '@angular/router';

const baseUrl = `${environment.HOST}/api/order/`;

interface IOrderItem {
  amount: number;
  item: number;
}

interface ICartIDsList {
  id: number;
  amount: number;
}

@Injectable({
  providedIn: 'root',
})
export class CartService {
  cartIdList?: Array<ICartIDsList> = [];

  constructor(
    private dishService: DishService,
    private http: HttpClient,
    private loginService: LoginService,
    private snackBar: SnackBarMessagesService,
    private router: Router
  ) {
    let cartIDListStorage: string | null = localStorage.getItem('cartIdList');
    if (cartIDListStorage != null) this.cartIdList = JSON.parse(cartIDListStorage);
  }

  isInCart(id: number): boolean {
    let cartIDListStorage: string | null = localStorage.getItem('cartIdList');
    if (cartIDListStorage == null) return false;

    this.cartIdList = JSON.parse(cartIDListStorage);

    return this.cartIdList ? this.cartIdList.some((item) => item.id === id) : false;
  }

  addItem(id: number) {
    if (this.cartIdList == null) return;

    this.cartIdList.push({
      id: id,
      amount: 1,
    });
    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  checkDiscountCode(code: string) {
    let url = `${environment.HOST}/api/discount/${code}`;
    return this.http.get<any>(url, {
      observe: 'response',
      responseType: 'json',
    });
  }

  createOrder() {
    let userID: number | undefined;

    // TODO: rewrite this piece of shit
    this.loginService.getUser().then((value) => {
      let user = value?.body as IUser;

      if (user === null) {
        this.snackBar.errorMessage("Couldn't fetch user data! Please try again later.");
        return;
      }
      userID = user.id;

      let data = {
        details: [] as Array<IOrderItem>,
        ordered_by: userID,
      };

      if (this.cartIdList === undefined) {
        this.snackBar.warningMessage('Your cart is empty! Please add something and try again.');
        return;
      }

      this.cartIdList.forEach((x) => {
        let orderItem = {item: x['id'], amount: x['amount']};
        data.details.push(orderItem);
      });

      if (data.details.length === 0) {
        this.snackBar.warningMessage('Your cart is empty! Please add something and try again.');
        return;
      }

      this.http.post(baseUrl, data, {
        observe: 'response',
        responseType: 'json',
        headers: this.loginService.getAuthHeader(),
      }).subscribe(
        (next) => {
          this.snackBar.successMessage('Thanks for your order!');
          this.router.navigate(['']);
        },
        (error) => {
          this.snackBar.errorMessage(
            'Error happened during order. Please contact support.');
        }
      );
    });
  }

  increaseAmount(id: number): void {
    if (this.cartIdList == null) return;

    let item = this.cartIdList.find((x) => x['id'] == id);
    if (item == null) return;

    let index = this.cartIdList.indexOf(item);
    item.amount += 1;
    this.cartIdList[index] = item;

    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  decreaseAmount(id: number): void {
    if (this.cartIdList == null) return;

    let item = this.cartIdList.find((x) => x['id'] == id);
    if (item == null) return;

    let index = this.cartIdList.indexOf(item);
    if (item.amount != 1) {
      item.amount -= 1;
    }
    this.cartIdList[index] = item;

    localStorage.setItem('cartIdList', JSON.stringify(this.cartIdList));
  }

  getDataFromAPI() {
    if (this.cartIdList == null) return;

    let payload: any[] = [];

    this.cartIdList.forEach(function (x: any) {
      payload.push(x.id);
    });
    return this.dishService.getMultiple(payload);
  }

  isHaveData(): boolean {
    if (this.cartIdList == null) return false;
    return this.cartIdList.length != 0;
  }

  deleteItem(id: number) {
    let cartIDListStorage: string | null = localStorage.getItem('cartIdList');
    if (cartIDListStorage == null) return;

    const cartIdList = JSON.parse(cartIDListStorage) || [];

    // Remove any items with matching id
    const filteredCart = cartIdList.filter((item: { id: number }) => item.id !== id);

    // Write updated list back to localStorage
    localStorage.setItem('cartIdList', JSON.stringify(filteredCart));
  }

  getAmount(id: number) {
    if (this.cartIdList == null) return 0;

    let item = this.cartIdList.find((x) => x['id'] == id);
    if (item == null) return 0;

    return item['amount'];
  }
}
