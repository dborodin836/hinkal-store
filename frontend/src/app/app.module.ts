import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { Routes, RouterModule } from '@angular/router';
import { MatPaginatorModule } from '@angular/material/paginator';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { AboutComponent } from './about/about.component';
import { StoreComponent } from './store/store.component';
import { DishDetailComponent } from './dish-detail/dish-detail.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ContactComponent } from './contact/contact.component';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SuccessComponent } from './success/success.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CheckoutComponent } from './checkout/checkout.component';
import { RegisterComponent } from './register/register.component';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { AccountActivationComponent } from './account-activation/account-activation.component';
import { ForbiddenComponent } from './forbidden/forbidden.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'store', component: StoreComponent },
  { path: 'store/:id', component: DishDetailComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'success', component: SuccessComponent },
  { path: 'cart', component: CheckoutComponent },
  { path: 'account-activation', component: AccountActivationComponent },
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
    DashboardComponent,
    SuccessComponent,
    CheckoutComponent,
    RegisterComponent,
    AccountActivationComponent,
    ForbiddenComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    ReactiveFormsModule,
    HttpClientXsrfModule,
    BrowserAnimationsModule,
    MatPaginatorModule,
    FormsModule,
    MatSnackBarModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
