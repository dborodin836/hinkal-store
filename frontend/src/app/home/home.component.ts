import { Component, OnInit } from '@angular/core';
import {UserModel} from "../models/user.model";
import {UserService} from "../services/user.service";
import {HttpResponse} from "@angular/common/http";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  users?: UserModel[]

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.retrieveUsers()
  }

  retrieveUsers() {
    this.userService.getAll().subscribe((data:HttpResponse<any>) => {
      console.log(data.body.results);
      this.users = data.body.results
    })
  }
}
