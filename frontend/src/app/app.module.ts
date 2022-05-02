import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from "@angular/common/http";
import {Routes, RouterModule} from '@angular/router';


import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { AboutComponent } from './about/about.component';
import { StoreComponent } from "./store/store.component";
import {DishDetailComponent} from "./dish-detail/dish-detail.component";
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ContactComponent } from './contact/contact.component';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';


const appRoutes: Routes =[
  { path: '', component: HomeComponent},
  { path: 'about', component: AboutComponent},
  { path: 'store', component: StoreComponent},
  { path: 'contact', component: ContactComponent},
  { path: 'login', component: LoginComponent},
  { path: 'dashboard', component: DashboardComponent},
  { path: '**', component: NotFoundComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NotFoundComponent,
    AboutComponent,
    StoreComponent,
    DishDetailComponent,
    FooterComponent,
    HeaderComponent,
    NavbarComponent,
    ContactComponent,
    LoginComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    ReactiveFormsModule,
    HttpClientXsrfModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
