import { DishModel } from './dish.model';

export class PaginatedResponseModel {
  count?: number;
  next?: string;
  previous?: string;
  results?: DishModel[];
}
