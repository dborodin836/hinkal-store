export interface Dish {
  id: any;
  title: string;
  added_by?: string;
  price: number;
  image: string;
  category?: string;
  description?: string;
  is_active?: boolean;
}
