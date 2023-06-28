import {Dish} from "./dish";

export class PaginatedResponseModel {
  count?: number;
  next?: string;
  previous?: string;
  results?: Dish[];
}
